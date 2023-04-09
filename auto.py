import keyboard
import pyautogui
import random
import mouse

pyautogui.FAILSAFE = False
STATUS = 'run'
DEVICE_MODE = 'mouse'

class Mouse:
    def __init__(self):
        self.rec = None
        
 
    def random_mouse_movement(self,width,height):
        __width = random.randrange(0,width,1)
        __height = random.randrange(0,height,1)
        pyautogui.moveTo(__width,__height,0.4,pyautogui.easeInQuad)
        pyautogui.sleep(3)
        rand = random.randrange(1,50,1)
        if rand > 250:
            up_down = random.randrange(0,2,1)
            if up_down == 0:
                print('scrill up')
                self.scroll(rand)
            else:
                print('scroll down')
                self.scroll(-rand)
            pyautogui.sleep(3)
   
    def mouse_click(self,x,y,clicks=0,button="left"):
        pyautogui.click(x,y,clicks=clicks,button=button)

    def mouse_drag(self,x,y,button="left"):
        pyautogui.drag(x,y,0.4,pyautogui.easeOutQuad,button=button)
    
    def get_cur_pos(self):
        return pyautogui.position()
    
    # (+) val for scroll up , (-) for scroll down
    def scroll(self,clicks): 
        pyautogui.scroll(clicks)
    
    def record(self):
        rec=mouse.record()
        self.rec = rec
        # print(rec)
    def play(self):
        if(self.rec != None) :
            mouse.play(self.rec)


class Keyboard:
    def __init__(self):
        self.rec = None
        
    def write(self,snippet):
        pyautogui.write(snippet,0.2)

    def scroll_up(self,presses):
        pyautogui.press('up',presses=presses,interval=0.3)
    
    def scroll_down(self,presses):
        pyautogui.press('down',presses=presses,interval=0.3)
    
    def hotkeys(self,*keys):
        print(*keys)
        pyautogui.hotkey(*keys)

    def record(self):
        rec=keyboard.record(until='esc')
        self.rec =rec

    def play(self):
        if(self.rec != None):
            keyboard.play(self.rec)

    def automate_scrolling(self):
        val = random.randrange(0,100,1)
        print(val)
        if val > 50:
            self.scroll_up(random.randrange(1,50,1))
            if val > 60 and val < 80:
                self.hotkeys('alt','tab')
        else:
            self.scroll_down(random.randrange(1,50,1))



m = Mouse()
k = Keyboard()
width, height = pyautogui.size()


def close():
    global STATUS
    STATUS = 'close'


def change_mode(mode):
    global DEVICE_MODE
    DEVICE_MODE = mode


def keyboard_mode():
    change_mode('keyboard')


def mouse_mode():
    change_mode('mouse')


def idle_mode():
    change_mode('idle')


def mouse_record():
    change_mode('mouse_rec')
    # m.record()
    # change_mode('idle')
    # print('record finished')


def keyboard_record():
    change_mode('keyboard_rec')
    k.record()
    # change_mode('idle')
    print('record finished')


def play_mode():
    print('in play mode')
    global DEVICE_MODE
    if DEVICE_MODE == 'mouse_idle':
        change_mode('mouse_play')
    if DEVICE_MODE == 'keyboard_idle':
        change_mode('keyboard_play')
    # m.play()


keyboard.add_hotkey('ctrl+alt+space', close)
keyboard.add_hotkey('ctrl+alt+k', keyboard_mode)
keyboard.add_hotkey('ctrl+alt+m', mouse_mode)
keyboard.add_hotkey('ctrl+alt+i', idle_mode)
keyboard.add_hotkey('alt+m', mouse_record)
keyboard.add_hotkey('alt+k', keyboard_record)
keyboard.add_hotkey('ctrl+alt+b', play_mode)


def automate_mouse():
    m.random_mouse_movement(width, height)


def automate_keyboard():
    k.automate_scrolling()


while True:
    print('in while', DEVICE_MODE)
    if(STATUS != 'close'):
        if(DEVICE_MODE == 'mouse'):
            print('in mouse mode')
            automate_mouse()
        elif(DEVICE_MODE == 'mouse_rec'):
            m.record()
            change_mode('mouse_idle')
        elif(DEVICE_MODE == 'keyboard_rec'):
            k.record()
            change_mode('keyboard_idle')
        elif(DEVICE_MODE == 'mouse_play'):
            m.play()
        elif(DEVICE_MODE == 'keyboard_play'):
            k.play()
        elif(DEVICE_MODE == 'keyboard'):
            automate_keyboard()
        pyautogui.sleep(3)
    else:
        break
