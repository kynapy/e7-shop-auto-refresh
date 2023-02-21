import pyautogui
import time
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def findCovenant(covenant):
    covenantPosition = pyautogui.locateOnScreen("./images/covenant.png", confidence=0.95)
    if (covenantPosition != None) :
        print("Buying covenant bookmarks")
        time.sleep(0.5)
        covenantPoint = pyautogui.center(covenantPosition)
        click(covenantPoint[0] + 800, covenantPoint[1] + 50)  # Hard coded displacement
        click(covenantPoint[0] + 800, covenantPoint[1] + 50)  # Hard coded displacement
        time.sleep(0.5)
        buyPosition = pyautogui.center(pyautogui.locateOnScreen("./images/buyCovenantButton.png"))
        click(buyPosition[0], buyPosition[1])
        click(buyPosition[0], buyPosition[1])
        time.sleep(0.5)
        covenant += 1
    else:
        print("No covenant bookmarks")
    return covenant

def findMystics(mystic):
    mysticPosition = pyautogui.locateOnScreen("./images/mystic.png", confidence=0.95)
    if (mysticPosition != None) :
        print("Buying mystic bookmarks")
        time.sleep(0.5)
        mysticPoint = pyautogui.center(mysticPosition)
        click(mysticPoint[0] + 800, mysticPoint[1] + 50)  # Hard coded displacement
        click(mysticPoint[0] + 800, mysticPoint[1] + 50)  # Hard coded displacement
        time.sleep(0.5)
        buyPosition = pyautogui.center(pyautogui.locateOnScreen("./images/buyMysticButton.png"))
        click(buyPosition[0], buyPosition[1])
        click(buyPosition[0], buyPosition[1])
        time.sleep(0.5)
        mystic += 1
    else:
        print("No mystic bookmarks")
    return mystic

def main():
    # Statistics for user
    covenantBought = 0
    mysticsBought = 0
    refreshes = 0

    while not keyboard.is_pressed('c'):
        # Find for BM
        covenantBought = findCovenant(covenantBought)
        mysticsBought = findMystics(mysticsBought)

        # Scroll down
        click(1280, 600)
        pyautogui.scroll(-5, 1280, 600)
        time.sleep(2)
        click(1280, 600)

        # Find for BM
        covenantBought = findCovenant(covenantBought)
        mysticsBought = findMystics(mysticsBought)

        # Print statistics
        refreshes += 1
        print("Refreshes: " + str(refreshes))
        print("Skystones used: " + str(refreshes*3))
        print("Covenants bought: " + str(covenantBought))
        print("Mystics bought: " + str(mysticsBought))
        print("----------------------------------------")

        # Refresh
        refreshPosition = pyautogui.center(pyautogui.locateOnScreen('./images/refreshButton.png', confidence=0.5))
        click(refreshPosition[0], refreshPosition[1])
        click(refreshPosition[0], refreshPosition[1])
        time.sleep(0.4)
        confirmPosition = pyautogui.center(pyautogui.locateOnScreen('./images/refreshConfirm.png'))
        click(confirmPosition[0], confirmPosition[1])
        click(confirmPosition[0], confirmPosition[1])
        time.sleep(0.7)


if __name__ == "__main__":
    main()