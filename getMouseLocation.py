import pyautogui, time

try:
    
	while True:
		x, y = pyautogui.position()
		positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		print(positionStr)
		time.sleep(0.05)

except KeyboardInterrupt:
	print('\nDone')

