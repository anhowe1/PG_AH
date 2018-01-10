import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n', 0.25)

time.sleep (0.25)
pg.hotkey('winleft','up')
