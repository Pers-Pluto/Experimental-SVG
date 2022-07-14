from matrix_svg import * 

import json

settings = json.load(open("settings.json"))

source_dir = settings["directories"]["svg_file_component_dir"]

nn = SVGFileComponent("none.svg", source_dir)
dr = SVGFileComponent("downRight.svg", source_dir)
ld = SVGFileComponent("leftDown.svg", source_dir)
lr = SVGFileComponent("leftRight.svg", source_dir)
lrc = SVGFileComponent("leftRightCrossingOver.svg", source_dir)
ud = SVGFileComponent("upDown.svg", source_dir)
udc = SVGFileComponent("upDownCrossingOver.svg", source_dir)
ul = SVGFileComponent("upLeft.svg", source_dir)
ur = SVGFileComponent("upRight.svg", source_dir)

letterA = [
    [dr, ld],
    [ur, udc]
    ]

# b

letterC = [
    [nn, nn, dr, lr, ld],
    [nn, dr, udc, ld, ud],
    [dr, udc, lrc, udc, lrc],
    [ud, ur, ud, ul, ud],
    [ur, lr, lrc, lr, ul]
]

# d

letterE = [
    [nn, dr, ld],
    [dr, lrc, udc],
    [ur, udc, ul]
]

# f

# g



letterKH = [
    [dr, ld, dr, ld, dr, ld],
    [ur, lrc, udc, lrc, udc, ul],
    [dr, udc, lrc, udc, lrc, ld],
    [ur, lrc, udc, lrc, udc, ul],
    [dr, udc, lrc, udc, lrc, nn],
    [ ur, ul, ur, ul, nn, nn]
]



