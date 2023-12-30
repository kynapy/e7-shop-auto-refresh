import pyautogui
import time
import keyboard
import win32api, win32con

DELAY_TIME = 0.5

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def scroll():
    click(1280, 600)
    pyautogui.scroll(-5, 1280, 600)
    time.sleep(2)
    click(1280, 600)

def shopRefresh(counter):
    refreshPosition = pyautogui.center(pyautogui.locateOnScreen('./images/refreshButton.png', confidence=0.95))
    click(refreshPosition[0], refreshPosition[1])
    click(refreshPosition[0], refreshPosition[1])
    time.sleep(1)
    confirmPosition = pyautogui.center(pyautogui.locateOnScreen('./images/refreshConfirm.png', confidence=0.95))
    click(confirmPosition[0], confirmPosition[1])
    click(confirmPosition[0], confirmPosition[1])
    time.sleep(0.7)
    counter.addRefreshes()

class StatsCounter():
    def __init__(self):
        self.covenants = 0
        self.mystics = 0
        self.refreshes = 0

    def addCovenant(self):
        self.covenants += 1

    def addMystics(self):
        self.mystics += 1

    def addRefreshes(self):
        self.refreshes += 1

    def printStats(self):
        print("Refreshes: ", self.refreshes)
        print("Skystones used: ", self.refreshes * 3)
        print("Covenants bought: ", self.covenants)
        print("Mystics bought: ", self.mystics)
        print("----------------------------------------")

def findCovenant(counter):
    try:
        covenantPosition = pyautogui.locateOnScreen("./images/covenant.png", confidence=0.95)
    except Exception:
        print("No covenant bookmarks")
        return
    try:
        print("Buying covenant bookmarks")
        time.sleep(DELAY_TIME)
        covenantPoint = pyautogui.center(covenantPosition)
        click(covenantPoint[0] + 1000, covenantPoint[1] + 50)  # Hard coded displacement
        click(covenantPoint[0] + 1000, covenantPoint[1] + 50)  # Hard coded displacement
        time.sleep(DELAY_TIME)
        buyPosition = pyautogui.center(pyautogui.locateOnScreen("./images/buyCovenantButton.png", confidence=0.95))
        click(buyPosition[0], buyPosition[1])
        click(buyPosition[0], buyPosition[1])
        time.sleep(DELAY_TIME)
        counter.addCovenant()
    except Exception:
        pass

def findMystics(counter):
    try:
        mysticPosition = pyautogui.locateOnScreen("./images/mystic.png", confidence=0.95)
    except Exception:
        print("No mystic bookmarks")
        return
    try:
        print("Buying mystic bookmarks")
        time.sleep(DELAY_TIME)
        mysticPoint = pyautogui.center(mysticPosition)
        click(mysticPoint[0] + 1000, mysticPoint[1] + 50)  # Hard coded displacement
        click(mysticPoint[0] + 1000, mysticPoint[1] + 50)  # Hard coded displacement
        time.sleep(DELAY_TIME)
        buyPosition = pyautogui.center(pyautogui.locateOnScreen("./images/buyMysticButton.png", confidence=0.95))
        click(buyPosition[0], buyPosition[1])
        click(buyPosition[0], buyPosition[1])
        time.sleep(DELAY_TIME)
        counter.addMystics()
    except:
        pass

def load_file(filename):
    f = open(filename, "r+")
    refreshes = int(f.readline().split(": ")[1])
    f.readline()  # Ignore skystones used
    covenants = int(f.readline().split(": ")[1])
    mystics = int(f.readline().split(": ")[1])
    f.close()
    return refreshes, covenants, mystics

def write_file(filename, refreshes, cov, mys):
    f = open(filename, "w")
    f.write("Refreshes: " + str(refreshes) + "\n")
    f.write("Skystones used: " + str(refreshes * 3) + "\n")
    f.write("Covenants bought: " + str(cov) + "\n")
    f.write("Mystics bought: " + str(mys) + "\n")
    f.close()

def main():
    failcount = 0
    filename = "refresh_log.txt"
    # Statistics for user
    if True:
        refreshes, covenantBought, mysticsBought = load_file(filename)

    counter = StatsCounter()

    while not keyboard.is_pressed('c'):
        try:
            # Look for BM
            findCovenant(counter)
            findMystics(counter)

            scroll() # Scroll down

            # Look for BM
            findCovenant(counter)
            findMystics(counter)

            # Print statistics
            counter.printStats()

            # Refresh
            shopRefresh(counter)

        except Exception as e:
            print("Auto refreshing has faced an error, trying to restart")
            print("Error :", e)
            time.sleep(3)
            failcount += 1
            if failcount > 25:
                break

    # Termination of refreshing, saving progress of refreshingcccccccccccc
    print("Auto refreshing has been stopped")
    write_file(filename,
               refreshes + counter.refreshes,
               covenantBought + counter.covenants,
               mysticsBought + counter.mystics)


if __name__ == "__main__":
    main()