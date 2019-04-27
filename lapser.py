# import libraries
import pyautogui
import PySimpleGUI as sg
import time

# layout of GUI
layout = [
    [sg.Text("Take screenshot every"), sg.InputText("3", size=(2, 1), key="time"), sg.Text("seconds")],
    [sg.Text("Save to"), sg.InputText("", key="folder"), sg.FolderBrowse()],
    [sg.Text("Amount"), sg.InputText("", key="amount")],
    [sg.Button("Start"), sg.Quit()]
]

# create window
window = sg.Window("Timelapser").Layout(layout)

# for naming the images
count = 0

# with a name and a destination folder, screenshot the screen and save it to the folder named with the given name and print it to the console
def screenshot(name, folder):
    im = pyautogui.screenshot()
    print("Saved" + name + ".png to " + folder)
    im.save(folder + "/" + name + ".png")

# warning for freezing
print("WARNING: The program (GUI) will freeze while it is taking screenshots, but the console prints each screenshot (meaning that it is working)")

# infinite loop
while True:
    # any button clicks or values of inputs
    event, values = window.Read()

    # if the quit button is pressed
    if event == "Quit":
        # close the window
        window.Close()
        # end the infinite loop
        break

    # if the start button is pressed
    if event == "Start":
        # for i < amount (of screenshots)
        for i in range(int(values["amount"])):
            # add 1 to count (for naming)
            count += 1
            # screenshot with the name of count and the destination folder
            screenshot(str(count), values["folder"])
            # wait the inputed amount of time to repeat
            time.sleep(int(values["time"]))
