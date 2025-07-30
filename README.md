# WeatherPeek ☁️🌤️

WeatherPeek is a minimalist weather monitor that runs in your system tray. Built with **Python** and **PyQt5**, it fetches your current location and displays the live weather using icon-based indicators in the tray — no popups, no windows, just clean, quiet updates.

---

## Features

- 🌍 Auto-detects your location (based on IP)
- ⛅ Displays weather via dynamic tray icons (day/night aware)
- 🔁 Updates automatically at regular intervals
- 🖥️ Lightweight and non-intrusive
- 📡 Uses free weather APIs

---

## Preview

![Tray Example](demo.gif)  

---

## Requirements

- Python 3.x
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Requests](https://pypi.org/project/requests/)
- [Open-Meteo API](https://open-meteo.com/)
- [IPInfo.io (or fallback IP Geolocation API)](https://ipinfo.io/)
- [PyInstaller](https://www.pyinstaller.org/) for packaging

---


## Download

👉 [Download the latest release](https://github.com/mwahaj36/Weather-Peek/releases) from the **Releases** section.

- ✅ Pre-built `.exe` for Windows available
- 🧪 Python source version for Linux/macOS

> No installation needed — just run it!

---

# Optional Setup for WeatherPeek (Windows)

Enhance your experience by making the WeatherPeek tray icon always visible and setting it to auto-run at system startup.

---

## Make Tray Icon Always Visible

1. **Right-click** on the taskbar and choose **Taskbar settings**
2. Scroll to **Notification area** and click **"Select which icons appear on the taskbar"**
3. Find **WeatherPeek** 
4. Toggle it **ON** to always show the icon in the system tray

---

## Run WeatherPeek on Startup Automatically

1. Press `Win + R` to open the Run dialog
2. Type: `shell:startup`
3. Press **Enter** — this opens the Startup folder
4. Copy the WeatherPeek `.exe` file (or a shortcut to it) into this folder

> WeatherPeek will now launch automatically every time you log in

---


## Installation

```bash
git clone https://github.com/yourusername/weatherpeek.git
cd weatherpeek
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


