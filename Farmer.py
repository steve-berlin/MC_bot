import pyautogui as pt
from time import sleep
path='Photos/start_game.png'
rows:int=input('Rows: ')
cols:int=input('Columns: ')
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=round(0.448))  # Increased confidence
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
        pt.mouseDown()  # Start mining (left mouse button)
        sleep(duration)
        pt.mouseUp()  # Stop mining
        print('Farming...')
    elif action == 'plant':
        pt.keyDown('x')
        sleep(duration)
        pt.keyUp('x')
        print('Farming...')
    elif action == 'meal':
        pt.keyDown('x')
        sleep(duration)
        pt.keyUp('x')
        
        pt.keyDown('8')
        pt.keyUp('8')
        
        pt.keyDown('x')
        sleep(duration)
        pt.keyUp('x')
        pt.keyDown('x')
        sleep(duration)
        pt.keyUp('x')
        
        pt.keyDown('9')
        pt.keyUp('9')
        print('Mealing...')
    else:
        print(f'Unknown action: {action}')


# Start game
sleep(0.5)
if not nav_to_image(path, 3):
    print("Failed to start game. Exiting...")
    exit()
Duration=cols
subDuration = rows

while Duration!=0:
    #Plant
    while subDuration != 0:
        move_character('w', 0.15, 'walking')  # Walk forward
        move_character(None, 0.1, 'plant')  # Mine block
        # move_character(None, 0.1, 'meal') 
        subDuration -= 1
    move_character('d', 0.15, 'walking')
    subDuration = rows-1
    while subDuration != 0:
        move_character('s', 0.15, 'walking')  # Walk forward
        move_character(None, 0.1, 'plant')  # Mine block
        # move_character(None, 0.1, 'meal') 
        subDuration -= 1
    #Collect

    subDuration = rows-1
    while subDuration != 0:
        move_character('w', 0.15, 'walking')  # Walk forward
        move_character(None, 0.1, 'attack')  # Mine block
        # move_character(None, 0.1, 'meal') 
        subDuration -= 1
    move_character('d', 0.15, 'walking')
    subDuration = rows-1
    while subDuration != 0:
        move_character('s', 0.15, 'walking')  # Walk forward
        move_character(None, 0.1, 'attack')  # Mine block
        # move_character(None, 0.1, 'meal') 
        subDuration -= 1

print('Time remaining: ',Duration, subDuration)
