import pyautogui, time

pyautogui.FAILSAFE = True

def slowDoubleClick(x, y):
	pyautogui.click(x,y)
	time.sleep(0.1)
	pyautogui.click(x,y)
	
def createPage():
    pyautogui.mouseDown(xi,yi)
    pyautogui.keyDown('ctrlleft')
    pyautogui.moveTo(xi + 8, yi, duration=0.1)
    pyautogui.mouseUp()
    pyautogui.keyUp('ctrlleft')
    pyautogui.doubleClick(xi + 35, yi)
    if i < 10:
        pyautogui.typewrite('0' + str(i), interval=0.1)
    else:
        pyautogui.typewrite(str(i), interval=0.1)
    pyautogui.press('enter')

def enterViewPort():
	slowDoubleClick(777, 190)
	time.sleep(0.1)

def moveViewPort():
    if i % 10 == 1:
        pyautogui.click(1445, 110)
        time.sleep(.75)
        for j in range(9):
            pyautogui.click(1435, 85)
            time.sleep(.75)
    else:
        pyautogui.click(1460, 85)
        time.sleep(.75)

def copyTitle():
	slowDoubleClick(777, 190)
	time.sleep(.1)
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.press('esc')
	pyautogui.press('esc')
	time.sleep(.1)
	
	slowDoubleClick(1600, 500)
	time.sleep(.1)
	slowDoubleClick(1400, 544)
	slowDoubleClick(1400, 544)
	time.sleep(.25)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.click(1600, 500)
    

start = int(input('Enter number of first page to be made: '))
end = int(input('Enter number of final page to be made: '))

startTime = time.time()

xi = start * 35 + 52
yi = 990

time.sleep(1)

pyautogui.click(800,10)

for i in range(start, end + 1):
    createPage()    
    xi += 35
    enterViewPort()
    moveViewPort()
    copyTitle()
	
endTime = time.time()

elapsedTime = str(round(endTime - startTime))

print('This process took ' + elapsedTime + ' seconds')
    
input('Press enter to finish')

