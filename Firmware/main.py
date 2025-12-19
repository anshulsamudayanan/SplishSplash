from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.split import Split

keyboard = KMKKeyboard()

keyboard.col_pins = (
    'P0.02',
    'P0.03',
    'P0.28',
    'P0.29',
    'P0.04',
)

keyboard.row_pins = (
    'P1.11',
    'P1.10',
    'P0.05',
    'P0.06',
    'P0.07',
)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

split = Split(
    split_type=Split.SplitType.BLE,
    split_side=None,
)

keyboard.modules.append(split)

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN,
        KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,
        KC.LCTL, KC.LALT, KC.LGUI, KC.SPC, KC.ENT,
        KC.BSPC, KC.RGUI, KC.RALT, KC.RCTL, KC.TAB,
        KC.NO, KC.NO, KC.MO(1), KC.NO, KC.NO,
        KC.NO, KC.NO, KC.MO(1), KC.NO, KC.NO,
    ],
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9,
        KC.TILD, KC.EXLM, KC.AT, KC.HASH, KC.DLR,
        KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.DEL,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.TRNS, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.TRNS, KC.NO, KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()
