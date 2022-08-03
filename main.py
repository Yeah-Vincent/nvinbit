def on_pin_pressed_p0():
    global 用户光标y位置User_Type_Locationy, 用户光标x位置User_Type_Locationx, USERS_WORDS_ON_SCREEN
    if 用户光标x位置User_Type_Locationx == 12:
        if 用户光标y位置User_Type_Locationy == 3:
            OLED12864_I2C.clear()
            OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.show_string(0, 1, 当前选择字, 1)
            用户光标y位置User_Type_Locationy = 1
            用户光标x位置User_Type_Locationx += 1
        else:
            用户光标y位置User_Type_Locationy += 1
            用户光标x位置User_Type_Locationx = 0
            USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + 当前选择字]
            USERS_WORDS_ON_SCREEN = [当前选择字]
    else:
        用户光标x位置User_Type_Locationx += 1
        USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + 当前选择字]
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global 当前选择字
    if USERS_WORDS_ON_SCREEN[0] == "":
        OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            " ",
            1)
        当前选择字 = " "
    else:
        OLED12864_I2C.show_string(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
        OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            " ",
            1)
        当前选择字 = " "
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global 次数, 当前选择字
    if 次数 == 29:
        pass
    else:
        OLED12864_I2C.clear()
        OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
        if USERS_WORDS_ON_SCREEN[0] == "":
            次数 = 次数 + 1
            OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
                用户光标y位置User_Type_Locationy,
                _26个字母与符号[次数],
                1)
            当前选择字 = _26个字母与符号[次数]
        else:
            OLED12864_I2C.show_string(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
            次数 = 次数 + 1
            OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
                用户光标y位置User_Type_Locationy,
                _26个字母与符号[次数],
                1)
            当前选择字 = _26个字母与符号[次数]
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global 预备y位置, 用户光标y位置User_Type_Locationy, 判断按钮第几遍
    if 判断按钮第几遍 == 0:
        if USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0])) == "/":
            if 用户光标y位置User_Type_Locationy == 4:
                OLED12864_I2C.clear()
                OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
                预备y位置 = 1
            else:
                预备y位置 = 用户光标y位置User_Type_Locationy + 1
            if USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 2,
                len(USERS_WORDS_ON_SCREEN[0])) == "add":
                OLED12864_I2C.show_string(0, 预备y位置, "/", 1)
                用户光标y位置User_Type_Locationy += 1
                判断按钮第几遍 = 1
            else:
                pass
        else:
            用户光标y位置User_Type_Locationy += 1
    else:
        OLED12864_I2C.show_number(0, 0, int("USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 2)") -- int("USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0])"), 1)
        if USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 2) == USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0])):
            pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global 次数, 当前选择字
    if 次数 <= 0:
        pass
    else:
        OLED12864_I2C.clear()
        OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
        if USERS_WORDS_ON_SCREEN[0] == "":
            次数 = 次数 - 1
            OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
                用户光标y位置User_Type_Locationy,
                _26个字母与符号[次数],
                1)
            当前选择字 = _26个字母与符号[次数]
        else:
            OLED12864_I2C.show_string(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
            次数 = 次数 - 1
            OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
                用户光标y位置User_Type_Locationy,
                _26个字母与符号[次数],
                1)
            当前选择字 = _26个字母与符号[次数]
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

预备y位置 = 0
当前选择字 = ""
用户光标x位置User_Type_Locationx = 0
用户光标y位置User_Type_Locationy = 0
USERS_WORDS_ON_SCREEN: List[str] = []
次数 = 0
_26个字母与符号: List[str] = []
判断按钮第几遍 = 0
判断按钮第几遍 = 0
_26个字母与符号 = ["a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    ",",
    ".",
    "&",
    "/"]
次数 = 0
USERS_WORDS_ON_SCREEN = [""]
datalogger.mirror_to_serial(True)
OLED12864_I2C.init(60)
OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
OLED12864_I2C.show_string(0, 1, "a", 1)
OLEDs_word_now = "vin:bit 0.0.1"
用户光标y位置User_Type_Locationy = 1