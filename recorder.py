import pynput
import time
from subprocess import run,Popen

def record_events():
    events = []
    start_time = time.time()

    def on_move(x, y):
        events.append({"time": time.time() - start_time, "event": "mouse", "data": {"x": x, "y": y}})

    def on_click(x, y, button, pressed):
        if pressed:
            print(x,y,flush=True,file=f)
            print(x,y,flush=True)
            events.append({"time": time.time() - start_time, "event": "click", "data": {"x": x, "y": y, "button": button}})

    def on_press(key):
        print(key,flush=True,file=f)
        print(key)
        events.append({"time": time.time() - start_time, "event": "keyboard", "data": {"key": key}})

    with pynput.mouse.Listener(on_click=on_click) as mouse_listener:
        with pynput.keyboard.Listener(on_press=on_press) as keyboard_listener:
            end_time = start_time + 120  # run for 60 seconds
            while time.time() < end_time:
                keyboard_listener.join(0.1)
                mouse_listener.join(0.1)

    return events

run(["touch","clicks.txt"])
f = open("clicks.txt","w")
events = record_events()
print(events)
# You can use the recorded events here, for example to replay the mouse clicks and keyboard inputs

