import pyautogui as py
import time

time.sleep(3)
dist = 250
while dist > 0:
    py.drag(dist,0)
    dist -= 6
    py.drag(0, dist)
    py.drag(-dist, 0)
    dist -= 6
    py.drag(0, -dist)