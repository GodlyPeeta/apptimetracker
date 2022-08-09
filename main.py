import sys
import win32gui
import json
import time

def callback(hwnd, strings):
    if win32gui.IsWindowVisible(hwnd):
        window_title = win32gui.GetWindowText(hwnd)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        if window_title and right-left and bottom-top:
            strings.append(window_title)
    return True

def searchWindow(windowName):
    winList = [] 
    win32gui.EnumWindows(callback, winList) 

    return windowName in winList

def main():
    out = json.load(open('out.json', 'r'))

    
    while True:
        if searchWindow(out['Target']):
            out['Time'] += 1/3600
            print(out);
            open('out.json', 'w').write(json.dumps(out, indent=4))
        time.sleep(5)

if __name__ == '__main__':
    main()