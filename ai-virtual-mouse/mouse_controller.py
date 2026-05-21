import pyautogui
import config

class MouseController:
    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()
        self.ploc_x, self.ploc_y = 0, 0
        pyautogui.FAILSAFE = True # Slap hand into upper left corner to kill script

    def move_cursor(self, raw_x, raw_y):
        # Map raw hand decimals directly to your monitor resolution scales
        screen_x = int(raw_x * self.screen_w)
        screen_y = int(raw_y * self.screen_h)

        # Smooth out pixel jitter
        cloc_x = self.ploc_x + (screen_x - self.ploc_x) / config.SMOOTHING
        cloc_y = self.ploc_y + (screen_y - self.ploc_y) / config.SMOOTHING

        pyautogui.moveTo(cloc_x, cloc_y)
        self.ploc_x, self.ploc_y = cloc_x, cloc_y

    def left_click_down(self):
        pyautogui.mouseDown()

    def left_click_up(self):
        pyautogui.mouseUp()

    def scroll_action(self, direction):
        if direction == "up":
            pyautogui.scroll(3)
        elif direction == "down":
            pyautogui.scroll(-3)
          
