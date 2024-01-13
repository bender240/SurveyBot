from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.right:
        print(f"Right click at ({x}, {y})")

# Create a mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

    #firefox input 1 = click at (85, 745)
    #search input 2 = click at Right click at (454, 65)
    #keyboard input 1 = https://www.surveyjunkie.com/?member
    #fullscreenclick 3 = (Right click at (853, 268)
    #fullscreenclick2 4 = (1312, 15)
    #startsurveyclick 5 = (619, 393)
    #SURvEY CLICKS
    #Right click at (310, 479)
# click at (259, 257)
# click at (269, 428)
# click at (263, 398)
# click at (283, 560)
#Right click at (1124, 116)
#Right click at (728, 118)
#Right click at (163, 111)

    