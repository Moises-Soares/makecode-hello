def on_gesture_logo_up():
    basic.show_icon(IconNames.STICK_FIGURE)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_screen_up():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_every_interval():
    basic.show_string("Viva!")
loops.every_interval(60000, on_every_interval)
