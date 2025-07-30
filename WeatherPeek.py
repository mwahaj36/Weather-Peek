from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
import requests, sys, os
import getLocation, getWeather

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

iconMap = {
    (0, 1): resource_path("src/icons/01d.png"),
    (0, 0): resource_path("src/icons/01n.png"),
    (1, 1): resource_path("src/icons/02d.png"),
    (1, 0): resource_path("src/icons/02n.png"),
    (2, 1): resource_path("src/icons/02d.png"),
    (2, 0): resource_path("src/icons/02n.png"),
    (3, 1): resource_path("src/icons/03.png"),
    (3, 0): resource_path("src/icons/03.png"),

    (51, 1): resource_path("src/icons/09d.png"),
    (51, 0): resource_path("src/icons/09n.png"),
    (53, 1): resource_path("src/icons/09d.png"),
    (53, 0): resource_path("src/icons/09n.png"),
    (55, 1): resource_path("src/icons/09d.png"),
    (55, 0): resource_path("src/icons/09n.png"),

    (61, 1): resource_path("src/icons/10.png"),
    (61, 0): resource_path("src/icons/10.png"),
    (63, 1): resource_path("src/icons/10.png"),
    (63, 0): resource_path("src/icons/10.png"),
    (65, 1): resource_path("src/icons/10.png"),
    (65, 0): resource_path("src/icons/10.png"),
    (66, 1): resource_path("src/icons/10.png"),
    (66, 0): resource_path("src/icons/10.png"),
    (67, 1): resource_path("src/icons/10.png"),
    (67, 0): resource_path("src/icons/10.png"),
    (80, 1): resource_path("src/icons/10.png"),
    (80, 0): resource_path("src/icons/10.png"),
    (81, 1): resource_path("src/icons/10.png"),
    (81, 0): resource_path("src/icons/10.png"),
    (82, 1): resource_path("src/icons/10.png"),
    (82, 0): resource_path("src/icons/10.png"),

    (71, 1): resource_path("src/icons/13.png"),
    (71, 0): resource_path("src/icons/13.png"),
    (73, 1): resource_path("src/icons/13.png"),
    (73, 0): resource_path("src/icons/13.png"),
    (75, 1): resource_path("src/icons/13.png"),
    (75, 0): resource_path("src/icons/13.png"),
    (77, 1): resource_path("src/icons/13.png"),
    (77, 0): resource_path("src/icons/13.png"),
    (85, 1): resource_path("src/icons/13.png"),
    (85, 0): resource_path("src/icons/13.png"),
    (86, 1): resource_path("src/icons/13.png"),
    (86, 0): resource_path("src/icons/13.png"),

    (95, 1): resource_path("src/icons/11.png"),
    (95, 0): resource_path("src/icons/11.png"),
    (96, 1): resource_path("src/icons/11.png"),
    (96, 0): resource_path("src/icons/11.png"),
    (99, 1): resource_path("src/icons/11.png"),
    (99, 0): resource_path("src/icons/11.png"),
}

def getIcon(code, isDay):
    return iconMap.get((code, isDay), resource_path("src/icons/err.png"))

def updateWeather():
    try:
        city, loc = getLocation.getLocation()
        lat, long = loc.split(",", 1)
        degrees, code, isDay, desc = getWeather.getWeather(lat, long)
        iconPath = getIcon(code, isDay)
        tray.setIcon(QIcon(iconPath))
        tray.setToolTip(f"{city}  {degrees}°C\nWeather: {desc}")
    except Exception as e:
        tray.setIcon(QIcon(resource_path("src/icons/err.png")))
        tray.setToolTip("Weather Update Failed")

app = QApplication([])
tray = QSystemTrayIcon(QIcon(resource_path("src/icons/err.png")), app)

menu = QMenu()
refreshAction = menu.addAction("Refresh Now")
refreshAction.triggered.connect(updateWeather)

quitAction = menu.addAction("Quit")
quitAction.triggered.connect(app.quit)

tray.setContextMenu(menu)
tray.show()

timer = QTimer()
timer.timeout.connect(updateWeather)
timer.start(30 * 60 * 1000)  

updateWeather()
sys.exit(app.exec_())
