import pygame as pg


keys = {
    # Litere
    'a': pg.K_a, 'b': pg.K_b, 'c': pg.K_c, 'd': pg.K_d, 'e': pg.K_e,
    'f': pg.K_f, 'g': pg.K_g, 'h': pg.K_h, 'i': pg.K_i, 'j': pg.K_j,
    'k': pg.K_k, 'l': pg.K_l, 'm': pg.K_m, 'n': pg.K_n, 'o': pg.K_o,
    'p': pg.K_p, 'q': pg.K_q, 'r': pg.K_r, 's': pg.K_s, 't': pg.K_t,
    'u': pg.K_u, 'v': pg.K_v, 'w': pg.K_w, 'x': pg.K_x, 'y': pg.K_y, 'z': pg.K_z,
    
    # Cifre
    '0': pg.K_0, '1': pg.K_1, '2': pg.K_2, '3': pg.K_3, '4': pg.K_4,
    '5': pg.K_5, '6': pg.K_6, '7': pg.K_7, '8': pg.K_8, '9': pg.K_9,
    
    # Taste funcționale
    'f1': pg.K_F1, 'f2': pg.K_F2, 'f3': pg.K_F3, 'f4': pg.K_F4,
    'f5': pg.K_F5, 'f6': pg.K_F6, 'f7': pg.K_F7, 'f8': pg.K_F8,
    'f9': pg.K_F9, 'f10': pg.K_F10, 'f11': pg.K_F11, 'f12': pg.K_F12,
    
    # Taste speciale
    'space': pg.K_SPACE,
    'return': pg.K_RETURN,
    'backspace': pg.K_BACKSPACE,
    'tab': pg.K_TAB,
    'capslock': pg.K_CAPSLOCK,
    'escape': pg.K_ESCAPE,
    'left': pg.K_LEFT, 'right': pg.K_RIGHT, 'up': pg.K_UP, 'down': pg.K_DOWN,
    'delete': pg.K_DELETE,
    'insert': pg.K_INSERT,
    'home': pg.K_HOME,
    'end': pg.K_END,
    'pageup': pg.K_PAGEUP,
    'pagedown': pg.K_PAGEDOWN,
    
    # Taste de control
    'shift': pg.K_LSHIFT, 'ctrl': pg.K_LCTRL, 'alt': pg.K_LALT,
    'rshift': pg.K_RSHIFT, 'rctrl': pg.K_RCTRL, 'ralt': pg.K_RALT,
    
    # Simboluri
    'comma': pg.K_COMMA, 'period': pg.K_PERIOD, 'slash': pg.K_SLASH,
    'semicolon': pg.K_SEMICOLON, 'quote': pg.K_QUOTE,
    'left_bracket': pg.K_LEFTBRACKET, 'right_bracket': pg.K_RIGHTBRACKET,
    'backslash': pg.K_BACKSLASH,
    'minus': pg.K_MINUS, 'equals': pg.K_EQUALS,
    
    # Butoane de mouse (dacă sunt suportate de cod)
    'mouse_left': pg.BUTTON_LEFT,
    'mouse_middle': pg.BUTTON_MIDDLE,
    'mouse_right': pg.BUTTON_RIGHT,
    
    # Alte taste
    'print_screen': pg.K_PRINTSCREEN,
    'scroll_lock': pg.K_SCROLLOCK,
    'pause': pg.K_PAUSE,
    'menu': pg.K_MENU,
    'numlock': pg.K_NUMLOCK,
}