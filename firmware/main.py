import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()


rgb = RGB(
    pixel_pin=board.A0,
    num_pixels=2,
    val_limit=1.0,
)
keyboard.modules.append(rgb)

rgb.pixels[0] = (255, 0, 0)  
rgb.pixels.show()


PINS = [
    board.D6,  # SW1  shift
    board.D7,  # SW2  left arrow
    board.D0,  # SW3  d
    board.A1,  # SW4  f
    board.A2,  # SW5  space
    board.A3,  # SW6  right arrow
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


keyboard.keymap = [
    [
        KC.LSHIFT,  # SW1
        KC.LEFT,    # SW2
        KC.D,       # SW3
        KC.F,       # SW4
        KC.SPACE,   # SW5
        KC.RIGHT,   # SW6
    ]
]

# --------------------
# LED update function for spacebar
# --------------------
def on_spacebar_update(keys_pressed):
    if keys_pressed[4]:
        rgb.pixels[1] = (0, 0, 255) 
    else:
        rgb.pixels[1] = (0, 0, 0)    
    rgb.pixels.show()

keyboard.on_presses.append(on_spacebar_update)

if __name__ == '__main__':
    keyboard.go()

