from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import requests, sys
import getLocation,getWeather

iconMap = {
    # 01 - Clear Sky
    (0, 1): "src/icons/01d.png",
    (0, 0): "src/icons/01n.png",

    # 02 - Mainly Clear / Partly Cloudy
    (1, 1): "src/icons/02d.png",
    (1, 0): "src/icons/02n.png",
    (2, 1): "src/icons/02d.png",
    (2, 0): "src/icons/02n.png",

    # 03 - Overcast
    (3, 1): "src/icons/03.png",
    (3, 0): "src/icons/03.png",

    # 09 - Drizzle
    (51, 1): "src/icons/09d.png",
    (51, 0): "src/icons/09n.png",
    (53, 1): "src/icons/09d.png",
    (53, 0): "src/icons/09n.png",
    (55, 1): "src/icons/09d.png",
    (55, 0): "src/icons/09n.png",

    # 10 - Rain & Showers
    (61, 1): "src/icons/10.png",
    (61, 0): "src/icons/10.png",
    (63, 1): "src/icons/10.png",
    (63, 0): "src/icons/10.png",
    (65, 1): "src/icons/10.png",
    (65, 0): "src/icons/10.png",
    (66, 1): "src/icons/10.png",
    (66, 0): "src/icons/10.png",
    (67, 1): "src/icons/10.png",
    (67, 0): "src/icons/10.png",
    (80, 1): "src/icons/10.png",
    (80, 0): "src/icons/10.png",
    (81, 1): "src/icons/10.png",
    (81, 0): "src/icons/10.png",
    (82, 1): "src/icons/10.png",
    (82, 0): "src/icons/10.png",

    # 13 - Snow
    (71, 1): "src/icons/13.png",
    (71, 0): "src/icons/13.png",
    (73, 1): "src/icons/13.png",
    (73, 0): "src/icons/13.png",
    (75, 1): "src/icons/13.png",
    (75, 0): "src/icons/13.png",
    (77, 1): "src/icons/13.png",
    (77, 0): "src/icons/13.png",
    (85, 1): "src/icons/13.png",
    (85, 0): "src/icons/13.png",
    (86, 1): "src/icons/13.png",
    (86, 0): "src/icons/13.png",

    # 11 - Thunderstorm
    (95, 1): "src/icons/11.png",
    (95, 0): "src/icons/11.png",
    (96, 1): "src/icons/11.png",
    (96, 0): "src/icons/11.png",
    (99, 1): "src/icons/11.png",
    (99, 0): "src/icons/11.png",
}

def updateWeather():
    try:
        city,loc=getLocation.getLocation()
        lat,long=loc.split(",",1)
        degrees,code,isDay,desc=getWeather.getWeather(lat,long)
        iconPath=getIcon(code,isDay)
        tray.setIcon(QIcon(iconPath))
        tray.setToolTip(f"{city}  {degrees}°C\nWeather: {desc}")
    except Exception as e:
        tray.setToolTip("Weather Update Failed")



app=QApplication([])
tray=QSystemTrayIcon(QIcon("src/icons/err.png"),app)
menu=QMenu()
refreshAction = menu.addAction("Refresh Now")
refreshAction.triggered.connect(updateWeather)
quitAction=menu.addAction("Quit")
quitAction.triggered.connect(app.quit)
tray.setContextMenu(menu)
tray.show()

def getIcon(code,isDay):
    return iconMap.get((code,isDay),"src/icons/err.png")


timer = QTimer()
timer.timeout.connect(updateWeather)
timer.start(30 * 60 * 1000) 

updateWeather()  
sys.exit(app.exec_())

