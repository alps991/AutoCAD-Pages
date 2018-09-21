import pyautogui, time
from setup import *

pyautogui.FAILSAFE = True

def slowDoubleClick(x, y):
	pyautogui.click(x,y)
	time.sleep(0.1)
	pyautogui.click(x,y)
	
def createPage():
	pyautogui.mouseDown(pageListX,pageListY)
	pyautogui.keyDown('ctrl')
	pyautogui.moveTo(pageListX + 8, pageListY, duration=0.1)
	time.sleep(0.1)
	pyautogui.mouseUp()
	time.sleep(0.1)
	pyautogui.keyUp('ctrl')
	time.sleep(0.1)
	if i < 24:
		pyautogui.doubleClick(pageListX + 35, pageListY)
		time.sleep(0.1)
		if i < 10:
			pyautogui.press('0')
			time.sleep(0.1)			
	else:
		pyautogui.keyDown('ctrl')
		pyautogui.press('pagedown')
		pyautogui.keyUp('ctrl')
		time.sleep(0.1)
		pyautogui.doubleClick(furthestPageListX, pageListY)
		time.sleep(0.1)
	pyautogui.typewrite(str(i), interval=0.1)
	pyautogui.press('enter')
	
def enterViewPort():
	slowDoubleClick(viewPortTitleX, viewPortTitleY)
	time.sleep(0.1)

def moveViewPort():
    if i % 10 == 1:
        pyautogui.click(downHandX, downHandY)
        time.sleep(.75)
        for j in range(9):
            pyautogui.click(leftHandX, leftHandY)
            time.sleep(.75)
    else:
        pyautogui.click(rightHandX, rightHandY)
        time.sleep(.75)

def copyTitle():
	slowDoubleClick(viewPortTitleX, viewPortTitleY)
	time.sleep(.1)
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.press('esc')
	pyautogui.press('esc')
	time.sleep(.1)
	
	slowDoubleClick(emptySpaceX, emptySpaceY)
	time.sleep(.1)
	slowDoubleClick(titleBlockTitleX, titleBlockTitleY)
	slowDoubleClick(titleBlockTitleX, titleBlockTitleY)
	time.sleep(.25)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.click(emptySpaceX, emptySpaceY)
    

start = int(input('Enter number of first page to be made: '))
end = int(input('Enter number of final page to be made: '))

startTime = time.time()

if start < 24:
	pageListX = (start - 1) * pageListItemWidth + firstPageListX
else:
	pageListX = furthestPageListX

time.sleep(1)

pyautogui.click(800,10)

for i in range(start, end + 1):
	createPage()
	if i < 24:
		pageListX += pageListItemWidth
	enterViewPort()
	moveViewPort()
	copyTitle()
	
endTime = time.time()

elapsedTime = str(round(endTime - startTime))

print('This process took ' + elapsedTime + ' seconds')
    
input('Press enter to finish')

