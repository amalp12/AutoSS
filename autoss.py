import time 
import pyautogui
import sys
import os  

def get_integer_input():
  try:
    i = int(input())
    if(i>0):
        return i
    else:
        return -1
  except:
    return -1

print("This program takes screenshots of your screen every n minutes. Please enter the value for n :")
interval = get_integer_input()
if(input==-1):
    print("Invalid Input! Please restart the program and enter a valid integer input.")
    sys.exit()

    
SAVE_PATH = "screenshots"
isExist = os.path.exists(SAVE_PATH)
if(not isExist):
    os.makedirs(SAVE_PATH)



mins= interval*60
current_time = time.time()

while(True):
    new_time = time.time()
    if(int(new_time) == int(current_time+mins)):
        current_time = new_time
        print(f"Screenshot saved at {time.ctime(current_time)}")

        myScreenshot = pyautogui.screenshot()
        filename = f"{time.ctime(current_time)}.jpg".replace(":","-")
        file_path = os.path.join(SAVE_PATH,filename)
        myScreenshot.save(file_path)

