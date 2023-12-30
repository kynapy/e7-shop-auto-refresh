# Epic Seven Shop Auto Refresher

This is a Python programme used to auto refresh for Covenant and Mystic bookmarks in Epic Seven.

## Disclaimer

This program was written and used with Epic Seven running full screen on BlueStacks emulator, and on a Windows machine with a screen resolution of 1920 x 1080p. I have yet to test it on other emulators or on devices with other screen resolutions, but this should work on any Windows machine with 1920 x 1080p display setting.

## Guide for players (some Python proficiency)

1. Install required libraries with `pip install pyautogui keyboard pywin32 opencv-python`
2. Replace the images with snips of your own. I used the built-in snipping tool for windows.

    > Note: You would need to do some refreshing yourself to find Mystics and Covenants bookmarks to take screenshots of, but you only have to do it once on the device you are using. The `buyCovenantButton.png` and `buyMysticButton.png` are the ones from the second confirmation, not the ones at the right side of the shop, so click on buy first, then take a snip of the buy button when the confirmation pops up.

3. Run the program.

## Basic Guide (no programming background)

1. Download this folder from GitHub by clicking the `Code` button and then `Download ZIP` or using [this](https://github.com/kynapy/e7-shop-auto-refresh/archive/refs/heads/main.zip). Unzip the file with an unzipping software of your choice.
2. Install Python! Simply download the latest version of Python3 at [their website](https://www.python.org/downloads/).
3. Open up the Command Prompt after installing Python. If Python3 is successfully installed, typing in `python --version` should tell you your currently installed Python version.
4. Install the required Python libraries by typing in `pip install pyautogui keyboard pywin32 opencv-python` in the Command Prompt. Let it run for a bit, and afterwards, you can close your Command Prompt. :)
5. Open up Epic Seven in full screen on BlueStacks and take snips (I used the built-in Snipping Tool in Windows) to replace the images in the `/images` folder.

    > Note: You would need to do some refreshing yourself to find Mystics and Covenants bookmarks to take screenshots of, but you only have to do it once on the device you are using. The `buyCovenantButton.png` and `buyMysticButton.png` are the ones from the second confirmation, not the ones at the right side of the shop, so click on buy first, then take a snip of the buy button when the confirmation pops up.

6. With the installation of Python3 comes along a built-in Integrated Development Environment (IDE) called IDLE, which is sufficient for our use case. Simply use the Windows search to look for IDLE and open it up.
7. On the top left, click on File -> Open, and open where you downloaded the folder, and open the `autoRefresh.py` file. This should open up the code.
8. Run the program by pressing `F5` or by clicking Run -> Run Module. Doing so will run the program. You can now watch the shop refresh itself. Cheers!

Do let me know if further clarifications/explanations are needed! Have fun summoning!
