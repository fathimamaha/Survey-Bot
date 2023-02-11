import subprocess
import pyautogui
import time
def open_private_chrome_window(url):
    subprocess.Popen(["google-chrome", "--incognito", url])
    
def new_tab():
    pyautogui.hotkey('alt','d')
    pyautogui.hotkey('alt','enter')
    pyautogui.click(359,103)
    
def click_events():
    while True:
    
        time.sleep(5)
        '''
        f = open("clicks.txt","r")
        for line in f:
            line = line.strip()
            x_y = line.split()
            print(x_y)
            if len(x_y)==2:
                x = int(x_y[0])
                y = int(x_y[1])
                print("clicking",x,y)
                pyautogui.click(x, y)
                print("click done")
                time.sleep(2)
        '''
        new_tab()
             


open_private_chrome_window("<survey link>")
time.sleep(5)
print("going to click")
click_events()
