import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.1)
time.sleep(1)
pg.hotkey('winleft','up')
time.sleep(1)
pg.hotkey('winleft','up')
time.sleep(1)
