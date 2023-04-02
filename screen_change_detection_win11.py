from pynput import keyboard
from pynput import mouse #pip install pynput
from PIL import ImageGrab #pip install pillow
from pygame import mixer
import time
import screeninfo #pip install screeninfo
import winsound

def getHex(rgb):
    return '%02X%02X%02X' % rgb

def checkColor():
    global prev_color, coords
    # take info about monitor
    monitors = screeninfo.get_monitors()
    # select monitor
    monitor = monitors[0]
    # take coordinates of pixels
    bbox = (monitor.x + coords[0], monitor.y + coords[1], monitor.x + coords[0] + 1, monitor.y + coords[1] + 1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r, g, b = rgbim.getpixel((0, 0))
    color = (r, g, b)
    print(f'COLOR: rgb{(r,g,b)} | HEX #{getHex((r,g,b))}')
    print(f'Coords: {coords}')
    if prev_color is not None and color != prev_color:
        #dzwiek
        winsound.Beep(1000,300) #(Hz, glosnosc)

    prev_color = color
    time.sleep(1)


def on_press(key):
    global capturing, coords, stop
    if key == keyboard.KeyCode(char='\\'):
        capturing = True
        print("Click on a pixel to capture its color")
    elif key == keyboard.Key.esc:
        capturing = False
        stop = True
        print("Exiting program")
        return False
    return True

def on_click(x, y, button, pressed):
    global capturing, coords, last_capture_time
    if capturing and pressed and button == mouse.Button.left:
        capturing = False
        coords = (x, y)
        last_capture_time = time.monotonic()
        print(f"Captured color at {coords}")

capturing = False
coords = None
last_capture_time = 0
prev_color = None
count = 0
stop = False

if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press) as klstnr:
        with mouse.Listener(on_click=on_click) as mlstnr:
            while not stop:
                if coords and time.monotonic() - last_capture_time > 1:
                    checkColor()
                    last_capture_time = time.monotonic()
            klstnr.join()
            mlstnr.join()
