
from urllib import response
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responces import responces

mouse=Controller()

class whatsapp:
    def __init__(self,speed=.5,click_speed=.3) -> None:
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
        pass 

    def nav_green_dot(self):
        try:
            position=pt.locateOnScreen('D:\comp\python\whatsapp_bot\greendot.png', confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception(nav_greengot0):',e)
        
    def nav_inpputbox(self):
        try:
            position=pt.locateOnScreen('D:\comp\python\whatsapp_bot\paperclip.png', confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(100,10,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception(nav_inputbox):',e)
        
    def nav_messsage(self):
        try:
            position=pt.locateOnScreen('D:\comp\python\whatsapp_bot\paperclip.png', confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(90,-70,duration=self.speed)
        except Exception as e:
            print('Exception(nav_message):',e)
            
    def get_message(self):
        pt.tripleClick()
        sleep(self.speed)
        pt.rightClick()
        sleep(self.speed)
        pt.moveRel(10,10, duration=self.speed)
        pt.click()
        sleep(1)
        self.message=pc.paste()
        print('user says: ', self.message)

    def send_message(self):
        try:
            if self.message!=self.last_message:
                bot_reponse=responces(self.message)
                print('you say: ', bot_reponse)
                pt.typewrite(bot_reponse, interval=.1)
                pt.press('enter')

                self.last_message=self.message
            else:
                print('no new messages...')
        except Exception as e:
         print('Exception(send_message):',e)

    def nav_x(self):
        try:
            position=pt.locateOnScreen('x.png',confidence=.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(10,10,duration=self.speed)
            pt.click()
        except Exception as e:
            print('Exception(nav_x):',e)

wa_bot=whatsapp(speed=.5,click_speed=.4)
sleep(2) 
wa_bot.nav_green_dot()
wa_bot.nav_x()
wa_bot.nav_messsage()
wa_bot.get_message()
wa_bot.nav_inpputbox()
wa_bot.send_message()

