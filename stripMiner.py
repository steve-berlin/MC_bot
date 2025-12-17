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
        pt.mouseDown()  # Start mining (left mouse button)
        sleep(duration)
        pt.mouseUp()  # Stop mining
        print('Mining...')
    else:
        print(f'Unknown action: {action}')

def locate_lava():
    screenshot = pt.screenshot()
    screenshot.save('/media/vas/VAS/MC bot v1.0/Photos/debug_screenshot.png')
    print("/media/vas/VAS/MC bot v1.0/Photos/debug_screenshot.png'")

    try:
        position = pt.locateCenterOnScreen('/media/vas/VAS/MC bot v1.0/Photos/lava.png', confidence=0.6)
        if position:
            print(f"Lava found at {position}")
    except pt.ImageNotFoundException:
        print("Lava image not found on screen. Check visibility and matching.")
        # Optionally add fallback logic here

        position = pt.locateCenterOnScreen('/media/vas/VAS/MC bot v1.0/Photos/lava.png', confidence=round(0.168))
        if position is None:
            return False
    else:
        move_character('s', 2)  # Back up from lava
        print('Found lava!!')
        return True

# Start game
sleep(1)
if not nav_to_image('/media/vas/VAS/MC bot v1.0/Photos/start_game.png', 3):
    print("Failed to start game. Exiting...")
    exit()

duration = 10
while duration > 0:
    if not locate_lava():
        move_character('w', 2, 'walking')  # Walk forward
        move_character(None, 2, 'attack')  # Mine block
        duration -= 1
    else:
        break

print('Time remaining: ', duration)