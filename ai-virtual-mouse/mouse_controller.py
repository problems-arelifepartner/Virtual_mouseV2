import pyautogui
import config
import platform
import ctypes

class MouseController:
    def __init__(self):
        # Optimize PyAutoGUI for real-time tracking speed
        pyautogui.PAUSE = 0
        
        # WINDOWS 11 SPECIFIC OPTIMIZATION: 
        # Fixes cursor scaling issues if Windows text scaling is set to 125% or 150%
        if platform.system() == "Windows":
            try:
                # Force Windows to recognize true pixel coordinates instead of scaled ones
                ctypes.windll.shcore.SetProcessDpiAwareness(2) 
            except Exception:
                try:
                    ctypes.windll.user32.SetProcessDPIAware():
                except Exception:
                    pass # Fallback if system blocks API execution

        self.screen_w, self.screen_h = pyautogui.size()
        self.ploc_x, self.ploc_y = 0, 0
        
        # Emergency Break: Slam mouse to top-left corner (0,0) to abort script execution
        pyautogui.FAILSAFE = True 

    def move_cursor(self, raw_x, raw_y):
        # Map raw decimal coordinate ratios natively to your screen resolution monitors
        screen_x = int(raw_x * self.screen_w)
        screen_y = int(raw_y * self.screen_h)

        # Smooth out pixel micro-jitters using LERP
        cloc_x = self.ploc_x + (screen_x - self.ploc_x) / config.SMOOTHING
        cloc_y = self.ploc_y + (screen_y - self.ploc_y) / config.SMOOTHING

        # Safely execute standard coordinate translations across desktop platforms
        pyautogui.moveTo(int(cloc_x), int(cloc_y))
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
