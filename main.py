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

def 系统显示字符(要显示的字符: str, 显示的位置x: number, 显示的位置y: number):
    global USERS_WORDS_ON_SCREEN
    OLED12864_I2C.show_string(显示的位置x, 显示的位置y, 要显示的字符, 1)
    USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + 要显示的字符]

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

def 系统显示数字(显示的数字: number, 位置x: number, 位置y: number):
    global USERS_WORDS_ON_SCREEN
    OLED12864_I2C.show_number(位置x, 位置y, 显示的数字, 1)
    USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + ("" + str(显示的数字))]

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
    global 临时, 用户光标y位置User_Type_Locationy, 用户光标x位置User_Type_Locationx, 判断按钮第几遍, 循环次数, 临时a, 临时b
    if 判断按钮第几遍 == 0:
        if USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 1) == "/":
            OLED12864_I2C.clear()
            OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.show_string(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
            临时 = USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 3,
                len(USERS_WORDS_ON_SCREEN[0]) - 1)
            if 临时 == "add" or (临时 == "subtract" or (临时 == "multiply" or 临时 == "divide")):
                if 用户光标x位置User_Type_Locationx == 12:
                    if 用户光标y位置User_Type_Locationy == 4:
                        系统显示字符(":", 0, 1)
                    else:
                        用户光标y位置User_Type_Locationy += 1
                        用户光标x位置User_Type_Locationx = 0
                        系统显示字符(":", 用户光标x位置User_Type_Locationx, 用户光标y位置User_Type_Locationy)
                else:
                    系统显示字符(":",
                        用户光标x位置User_Type_Locationx + 1,
                        用户光标y位置User_Type_Locationy)
                判断按钮第几遍 = 1
            else:
                pass
        else:
            images.create_image("""
                # # . # #
                                # # . # #
                                . . . . .
                                . # # # .
                                # . . . #
            """).scroll_image(0, 500)
    else:
        循环次数 = 1
        for index in range(26):
            if parse_float(_26个字母与符号[循环次数]) == int(USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 3)):
                临时a = 循环次数
            循环次数 += 1
        循环次数 = 1
        for index2 in range(26):
            if parse_float(_26个字母与符号[循环次数]) == int(USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 1)):
                临时b = 循环次数
            循环次数 += 1
        if 临时 == "add":
            系统显示数字(临时a + 临时b, 0, 用户光标y位置User_Type_Locationy + 1)
        elif 临时 == "subtract":
            系统显示数字(临时a - 临时b, 0, 用户光标y位置User_Type_Locationy + 1)
        elif 临时 == "multiply":
            系统显示数字(临时a * 临时b, 0, 用户光标y位置User_Type_Locationy + 1)
        else:
            系统显示数字(临时a / 临时b, 0, 用户光标y位置User_Type_Locationy + 1)
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

临时b = 0
临时a = 0
循环次数 = 0
临时 = ""
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
