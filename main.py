def on_forever():
    while input.button_is_pressed(Button.A):
        for index in range(3):
            basic.show_arrow(ArrowNames.NORTH)
            basic.show_arrow(ArrowNames.NORTH_EAST)
            basic.show_arrow(ArrowNames.EAST)
            basic.show_arrow(ArrowNames.SOUTH)
            basic.show_arrow(ArrowNames.SOUTH_EAST)
            basic.show_arrow(ArrowNames.SOUTH_WEST)
            basic.show_arrow(ArrowNames.WEST)
            basic.show_arrow(ArrowNames.NORTH_WEST)
            basic.show_arrow(ArrowNames.NORTH)
basic.forever(on_forever)

def on_forever2():
    basic.show_number(input.temperature())
    while input.temperature() < 37:
        basic.show_number(input.temperature())
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever2)
