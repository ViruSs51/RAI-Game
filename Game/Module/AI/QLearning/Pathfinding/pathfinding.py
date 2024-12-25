import numpy as np
import random
from copy import deepcopy


class Obstacle:
    def __init__(self, pos, size):
        self.pos = pos  # Poziția obstacolului (x, y)
        self.size = size  # Dimensiunea obstacolului (lățime, înălțime)


class QLearningGame:
    def __init__(self, grid_size, player_pos, obstacles):
        self.grid_size = grid_size  # Dimensiunea hărții (lățime, înălțime)
        self.player_pos = player_pos  # Poziția jucătorului (x, y)
        self.data_path = (
            f"pathfinding_map({self.grid_size[0]})({self.grid_size[1]}).npy"
        )
        self.obstacles = obstacles  # Listă de obstacole (obiecte de tip Obstacle)
        self.q_table = np.zeros(
            (int(grid_size[0]), int(grid_size[1]), 4)
        )  # Q-Table pentru 4 acțiuni
        self.learning_rate = 0.1
        self.discount_factor = 0.3
        self.epsilon = 0.2  # Rata de explorare
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # sus, jos, stânga, dreapta
        self.obstacle_map = self._generate_obstacle_map()

    def _generate_obstacle_map(self):
        """Creează o hartă binară cu obstacole."""
        obstacle_map = np.zeros(
            [int(self.grid_size[0]), int(self.grid_size[1])], dtype=int
        )
        for obj in self.obstacles:
            x, y = obj.pos
            width, height = obj.size
            # print(obj.pos, obj.size, self.grid_size)
            obstacle_map[int(x) : int(x + width), int(y) : int(y + height)] = 1
        return obstacle_map

    async def _agenerate_obstacle_map(self):
        """Creează o hartă binară cu obstacole."""
        obstacle_map = np.zeros(
            [int(self.grid_size[0]), int(self.grid_size[1])], dtype=int
        )
        for obj in self.obstacles:
            x, y = obj.pos
            width, height = obj.size
            # print(obj.pos, obj.size, self.grid_size)
            obstacle_map[int(x) : int(x + width), int(y) : int(y + height)] = 1
        return obstacle_map

    async def _is_valid_position(self, pos):
        """Verifică dacă poziția este validă (în grid și nu este obstacol)."""
        x, y = pos
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1]:
            return self.obstacle_map[x, y] == 0
        return False

    async def get_next_state(self, pos, action):
        """Determină următoarea stare validă în funcție de acțiune."""
        next_pos = (pos[0] + action[0], pos[1] + action[1])
        if await self._is_valid_position(next_pos):
            return next_pos
        return pos  # Rămâne pe loc dacă lovim un obstacol sau ieșim din hartă

    async def train(self, monster_pos, episodes=1000, max_steps=100):
        """Antrenează monstrul folosind Q-Learning."""
        for episode in range(episodes):
            state = monster_pos
            total_reward = 0

            for step in range(max_steps):  # Limităm numărul de pași per episod
                # Alegem acțiunea: explorare sau exploatare
                if np.random.rand() < self.epsilon:
                    action_idx = np.random.randint(4)
                else:
                    action_idx = np.argmax(self.q_table[state[0], state[1]])

                action = self.actions[action_idx]
                next_state = await self.get_next_state(state, action)

                # Calculăm recompensa
                if next_state == self.player_pos:
                    reward = 10  # Recompensă mare pentru atingerea jucătorului
                elif next_state == state:
                    reward = -1  # Penalizare pentru coliziuni sau rămânerea pe loc
                else:
                    # Mic bonus pentru mișcare validă
                    reward = -0.1 + (
                        1
                        / (
                            1
                            + np.linalg.norm(
                                np.array(next_state) - np.array(self.player_pos)
                            )
                        )
                    )

                total_reward += reward

                # Actualizăm Q-Value
                self.q_table[state[0], state[1], action_idx] += self.learning_rate * (
                    reward
                    + self.discount_factor
                    * np.max(self.q_table[next_state[0], next_state[1]])
                    - self.q_table[state[0], state[1], action_idx]
                )

                state = next_state

                # Oprim episodul dacă jucătorul este găsit
                if state == self.player_pos:
                    break

            # Reducem epsilon (explorare) în timp
            self.epsilon = max(0.1, self.epsilon * 0.995)

            # Afișăm progresul
            # if (episode + 1) % 100 == 0:
            #    print(f"Episode {episode + 1}/{episodes}, Total Reward: {total_reward:.2f}, Epsilon: {self.epsilon:.4f}")

    async def reset_environment(self, grid_size, new_player_pos, new_obstacles):
        self.grid_size = grid_size
        self.player_pos = new_player_pos
        self.obstacles = new_obstacles
        self.q_table = np.zeros((int(grid_size[0]), int(grid_size[1]), 4))
        self.obstacle_map = await self._agenerate_obstacle_map()

    # Reantrenare rapidă pe noul mediu
    async def retrain(self, monster_pos, episodes=500, max_steps=100):
        """Reantrenează monstrul pentru harta și poziția player-ului actualizate."""
        for episode in range(episodes):
            state = monster_pos
            total_reward = 0

            for _ in range(max_steps):  # Limităm numărul de pași per episod
                # Alegem acțiunea: explorare sau exploatare
                if np.random.rand() < self.epsilon:
                    action_idx = np.random.randint(4)  # Explorare
                else:
                    action_idx = np.argmax(
                        self.q_table[state[0], state[1]]
                    )  # Exploatare

                action = self.actions[action_idx]
                next_state = await self.get_next_state(state, action)

                # Recompensă: pozitivă dacă ajunge la player, negativă altfel
                if next_state == self.player_pos:
                    reward = 10  # Recompensă mare pentru a ajunge la player
                    self.q_table[
                        state[0], state[1], action_idx
                    ] += self.learning_rate * (
                        reward - self.q_table[state[0], state[1], action_idx]
                    )
                    total_reward += reward
                    break  # Episod încheiat, a ajuns la player
                elif next_state == state:
                    reward = -0.1
                    total_reward += reward

                else:
                    reward = reward = -0.1 + (
                        2
                        / (
                            1
                            + np.linalg.norm(
                                np.array(next_state) - np.array(self.player_pos)
                            )
                        )
                    )  # Penalizare mică pentru fiecare pas
                    self.q_table[
                        state[0], state[1], action_idx
                    ] += self.learning_rate * (
                        reward
                        + self.discount_factor
                        * np.max(self.q_table[next_state[0], next_state[1]])
                        - self.q_table[state[0], state[1], action_idx]
                    )
                    total_reward += reward

                # Avansăm la următoarea stare
                state = next_state

            # Afișăm progresul fiecărui episod
            # print(f"Episode {episode + 1}/{episodes}, Total Reward: {total_reward}")

    async def next_action(self, monster_pos, player_pos, obstacles):
        """Determină următoarea acțiune pentru monstrul antrenat."""
        # Actualizăm obstacolele dacă acestea se schimbă
        self.obstacles = obstacles
        self.player_pos = player_pos
        self.obstacle_map = self._generate_obstacle_map()

        # Calculăm cea mai bună acțiune pentru poziția curentă
        action_idx = np.argmax(self.q_table[monster_pos[0], monster_pos[1]])
        return self.actions[action_idx]

    def display_grid(self, way=[]):
        """Afișează grid-ul cu obstacole și poziția jucătorului."""
        grid = np.full(self.grid_size, ".", dtype=str)
        for w in way:
            # print(w)
            grid[w[0], w[1]] = "*"
        for obj in self.obstacles:
            x, y = obj.pos
            width, height = obj.size
            grid[x : x + width, y : y + height] = "#"
        grid[self.player_pos] = "P"
        print("\n".join("".join(row) for row in grid))

    async def save_q_table(self, file_name: str = None):
        """Salvează Q-Table-ul într-un fișier."""
        np.save(file_name if file_name else self.data_path, self.q_table)

    async def load_q_table(self, file_name: str = None):
        """Încarcă Q-Table-ul dintr-un fișier."""
        try:
            self.q_table = np.load(file_name if file_name else self.data_path)
        except:
            return False


# Determinare acțiune optimă
# next_move = ql_game.next_action(monster_pos, player_pos, obstacles)
# print(f"Monstrul ar trebui să se miște în direcția: {next_move}")
if __name__ == "__main__":
    # Configurare inițială
    grid_size = (100, 100)
    player_pos = (random.randint(80, 99), random.randint(80, 99))
    obstacles = [
        Obstacle(
            pos=(random.randint(0, 99), random.randint(0, 99)),
            size=(random.randint(1, 1), random.randint(1, 1)),
        )
        for o in range(200)
    ]
    monster_pos = [0, 0]

    ql_game = QLearningGame(grid_size, player_pos, obstacles)

    train = 1
    for i in range(1):
        if train:
            print("_________________", i, "________________")

            player_pos = (random.randint(80, 99), random.randint(80, 99))
            obstacles = [
                Obstacle(
                    pos=(random.randint(0, 99), random.randint(0, 99)),
                    size=(random.randint(1, 1), random.randint(1, 1)),
                )
                for o in range(200)
            ]
            ql_game.load_q_table()
            ql_game.reset_environment(player_pos, obstacles)

            ql_game.train(monster_pos, episodes=2000, max_steps=500)

            new_player_pos = (random.randint(80, 99), random.randint(80, 99))
            new_obstacles = [
                Obstacle(
                    pos=(random.randint(0, 99), random.randint(0, 99)),
                    size=(random.randint(1, 1), random.randint(1, 1)),
                )
                for o in range(200)
            ]
            ql_game.reset_environment(new_player_pos, new_obstacles)

            # ql_game.display_grid()
            ql_game.retrain(monster_pos, episodes=2000, max_steps=500)
            # ql_game.save_q_table()
            print("Antrenament finalizat!")

    if not train:
        ql_game = QLearningGame(grid_size, player_pos, obstacles)
        ql_game.load_q_table()

    monster_postions = []
    for s in range(20000):
        next_move = ql_game.next_action(monster_pos, player_pos, obstacles)
        move_to = "stay"
        if next_move[0] == -1:
            move_to = "left"
            monster_pos[0] -= 1
        elif next_move[0] == 1:
            move_to = "right"
            monster_pos[0] += 1
        elif next_move[1] == -1:
            move_to = "up"
            monster_pos[1] -= 1
        elif next_move[1] == 1:
            move_to = "down"
            monster_pos[1] += 1
        monster_postions.append(deepcopy(monster_pos))
        # print(f"Move to: {move_to}")
    ql_game.display_grid(monster_postions)
