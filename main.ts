basic.forever(function () {
    while (input.buttonIsPressed(Button.A)) {
        for (let index = 0; index < 3; index++) {
            basic.showArrow(ArrowNames.North)
            basic.showArrow(ArrowNames.NorthEast)
            basic.showArrow(ArrowNames.East)
            basic.showArrow(ArrowNames.South)
            basic.showArrow(ArrowNames.SouthEast)
            basic.showArrow(ArrowNames.SouthWest)
            basic.showArrow(ArrowNames.West)
            basic.showArrow(ArrowNames.NorthWest)
            basic.showArrow(ArrowNames.North)
        }
    }
})
basic.forever(function () {
    basic.showNumber(input.temperature())
    while (input.temperature() < 36) {
        basic.showNumber(input.temperature())
        basic.showIcon(IconNames.Sad)
    }
})
