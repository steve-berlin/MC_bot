import pyautogui as pt
from time import sleep

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.7)  # Increased confidence
    if position is None:
        print(f'{image} not found...')
        return False
    else:
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=clicks, interval=0.3)
        return True

def move_character(key_press, duration, action='walking'):
    if action == 'walking':
        pt.keyDown(key_press)
        sleep(duration)
        pt.keyUp(key_press)
        print('Walking...')
    elif action == 'attack':
        #1
        pt.keyDown('p')
        sleep(duration)
        pt.keyUp('p')
        #2
        pt.keyDown('p')
        sleep(duration)
        pt.keyUp('p')
        print('Planting...')
    else:
        print(f'Unknown action: {action}')


# Start game
sleep(0.5)
if not nav_to_image('start_game.png', 3):
    print("Failed to start game. Exiting...")
    exit()
duration = 8

while duration > 0:
    move_character('w', 0.15, 'walking')  # Walk forward
    move_character(None, 0.1, 'attack')  # Mine block
    duration -= 1
print('Time remaining: ', duration)