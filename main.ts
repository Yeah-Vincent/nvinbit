input.onPinPressed(TouchPin.P0, function () {
    if (用户光标x位置User_Type_Locationx == 12) {
        if (用户光标y位置User_Type_Locationy == 3) {
            OLED12864_I2C.clear()
            OLED12864_I2C.showString(
            0,
            0,
            "vin:bit 0.0.1",
            270
            )
            OLED12864_I2C.showString(
            0,
            1,
            当前选择字,
            1
            )
            用户光标y位置User_Type_Locationy = 1
            用户光标x位置User_Type_Locationx += 1
        } else {
            用户光标y位置User_Type_Locationy += 1
            用户光标x位置User_Type_Locationx = 0
            USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + 当前选择字]
            USERS_WORDS_ON_SCREEN = [当前选择字]
        }
    } else {
        用户光标x位置User_Type_Locationx += 1
        USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + 当前选择字]
    }
})
function 系统显示字符 (要显示的字符: string, 显示的位置x: number, 显示的位置y: number) {
    OLED12864_I2C.showString(
    显示的位置x,
    显示的位置y,
    要显示的字符,
    1
    )
    USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + 要显示的字符]
}
input.onButtonPressed(Button.A, function () {
    if (USERS_WORDS_ON_SCREEN[0] == "") {
        OLED12864_I2C.showString(
        用户光标x位置User_Type_Locationx,
        用户光标y位置User_Type_Locationy,
        " ",
        1
        )
        当前选择字 = " "
    } else {
        OLED12864_I2C.showString(
        0,
        1,
        USERS_WORDS_ON_SCREEN[0],
        1
        )
        OLED12864_I2C.showString(
        用户光标x位置User_Type_Locationx,
        用户光标y位置User_Type_Locationy,
        " ",
        1
        )
        当前选择字 = " "
    }
})
function 系统显示数字 (显示的数字: number, 位置x: number, 位置y: number) {
    OLED12864_I2C.showNumber(
    位置x,
    位置y,
    显示的数字,
    1
    )
    USERS_WORDS_ON_SCREEN = ["" + USERS_WORDS_ON_SCREEN[0] + 显示的数字]
}
input.onPinPressed(TouchPin.P2, function () {
    if (次数 == 29) {
    	
    } else {
        OLED12864_I2C.clear()
        OLED12864_I2C.showString(
        0,
        0,
        "vin:bit 0.0.1",
        270
        )
        if (USERS_WORDS_ON_SCREEN[0] == "") {
            次数 = 次数 + 1
            OLED12864_I2C.showString(
            用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            _26个字母与符号[次数],
            1
            )
            当前选择字 = _26个字母与符号[次数]
        } else {
            OLED12864_I2C.showString(
            0,
            1,
            USERS_WORDS_ON_SCREEN[0],
            1
            )
            次数 = 次数 + 1
            OLED12864_I2C.showString(
            用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            _26个字母与符号[次数],
            1
            )
            当前选择字 = _26个字母与符号[次数]
        }
    }
})
function 显示字符 (x: number, y: number, 字符: string, 是加是减: boolean) {
	
}
input.onButtonPressed(Button.B, function () {
    if (USERS_WORDS_ON_SCREEN[0].charAt(USERS_WORDS_ON_SCREEN[0].length - 1) == "/") {
        OLED12864_I2C.clear()
        OLED12864_I2C.showString(
        0,
        0,
        "vin:bit 0.0.1",
        270
        )
        临时 = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].length - 2, USERS_WORDS_ON_SCREEN[0].length)
        if (临时 == "add" || (临时 == "subtract" || (临时 == "multiply" || 临时 == "divide"))) {
            系统显示字符("/", 用户光标x位置User_Type_Locationx + 1, 用户光标y位置User_Type_Locationy)
            用户光标y位置User_Type_Locationy += 1
            判断按钮第几遍 = 1
        } else {
        	
        }
    } else {
        images.createImage(`
            # # . # #
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            `).scrollImage(0, 500)
    }
})
input.onPinPressed(TouchPin.P1, function () {
    if (次数 <= 0) {
    	
    } else {
        OLED12864_I2C.clear()
        OLED12864_I2C.showString(
        0,
        0,
        "vin:bit 0.0.1",
        270
        )
        if (USERS_WORDS_ON_SCREEN[0] == "") {
            次数 = 次数 - 1
            OLED12864_I2C.showString(
            用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            _26个字母与符号[次数],
            1
            )
            当前选择字 = _26个字母与符号[次数]
        } else {
            OLED12864_I2C.showString(
            0,
            1,
            USERS_WORDS_ON_SCREEN[0],
            1
            )
            次数 = 次数 - 1
            OLED12864_I2C.showString(
            用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            _26个字母与符号[次数],
            1
            )
            当前选择字 = _26个字母与符号[次数]
        }
    }
})
let 临时 = ""
let 当前选择字 = ""
let 用户光标x位置User_Type_Locationx = 0
let 用户光标y位置User_Type_Locationy = 0
let USERS_WORDS_ON_SCREEN: string[] = []
let 次数 = 0
let _26个字母与符号: string[] = []
let 判断按钮第几遍 = 0
判断按钮第几遍 = 0
_26个字母与符号 = [
"a",
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
"/"
]
次数 = 0
USERS_WORDS_ON_SCREEN = [""]
datalogger.mirrorToSerial(true)
OLED12864_I2C.init(60)
OLED12864_I2C.showString(
0,
0,
"vin:bit 0.0.1",
270
)
OLED12864_I2C.showString(
0,
1,
"a",
1
)
let OLEDs_word_now = "vin:bit 0.0.1"
用户光标y位置User_Type_Locationy = 1
