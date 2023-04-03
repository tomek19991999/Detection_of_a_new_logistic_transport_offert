from PIL import ImageGrab #pip install pillow
from pynput import mouse #pip install pynput
import keyboard
import time
import winsound



def on_click(x2, y2, button, pressed):
    global x, y
    if pressed:
        print('Mouse clicked at ({0}, {1})'.format(x2, y2))
        x=x2
        y=y2
        listener.stop()

prev_x=0
x=0
prev_y=0
y=0
px = ImageGrab.grab().load()
prev_color = px[prev_x, prev_y]

while True:
    if keyboard.is_pressed('esc'):
        print("Exiting program!")
        break
    if keyboard.is_pressed('\\'):
        print("clicked \!")
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

    px = ImageGrab.grab().load()
    color = px[x, y]
    if color!=prev_color:
        print("Color changed! R:",color[0],"G:",color[1],"B:",color[2])
        #sound
        winsound.Beep(1000,300) #(Hz, volume)

    if x!=prev_x or y!=prev_y:
        print("Changed coordinates to: x:",x," y:",y)

    prev_color=color
    prev_x=x
    prev_y=y

    time.sleep(0.01)

