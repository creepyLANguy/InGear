import sys
import ac
import acsys

def acMain(ac_version):
        global shadow, label, appWindow
        appWindow = ac.newApp("InGear")
        ac.setSize(appWindow, 40, 60)
        ac.setBackgroundOpacity(appWindow,0)
        ac.drawBorder(appWindow,0)
        ac.setIconPosition(appWindow, 0, -9000)
        -ac.setTitlePosition(appWindow,0, -9000)

        shadow = ac.addLabel(appWindow, "?")
        ac.setFontSize(shadow, 44)
        ac.setPosition(shadow, 21, 1)
        ac.setFontColor(shadow, 0.2, 0.2, 0.2, 0.2)
        ac.setFontAlignment(shadow, "center")

        label = ac.addLabel(appWindow, "?")
        ac.setFontSize(label, 44)
        ac.setPosition(label, 20, 0)
        ac.setFontColor(label, 1, 1, 1, 0.4)
        ac.setFontAlignment(label, "center")

        return "InGear"

def acUpdate(deltaT):
        global gear, appWindow
        ac.setBackgroundOpacity(appWindow,0)
        gear = ac.getCarState(0, acsys.CS.Gear)
        if(gear == 0):
            ac.setText(label, "R")
            ac.setText(shadow, "R")
        elif(gear == 1):
            ac.setText(label, "N")
            ac.setText(shadow, "N")
        else:
            ac.setText(label, "{}".format(gear-1))
            ac.setText(shadow, "{}".format(gear-1))
