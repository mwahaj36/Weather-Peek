# WeatherPeek ☁️🌤️

**WeatherPeek** is a minimalist weather monitor that lives in your system tray.  
Built with **Python** and **PyQt5**, it fetches your current location using your IP address and shows real-time weather using icon-based tray indicators — no popups, no windows, just clean, quiet updates.

When you hover over the tray icon, it also shows a **short weather description** and the **current temperature (°C)**.

inspired by the simplicity and charm of [RunCat](https://github.com/Kyome22/RunCat_for_windows).

---

## Features

- 🌍 Auto-detects your location (via IP)
- ⛅ Displays current weather using tray icons (with day/night awareness)
- ℹ️ Hover to see weather description + temperature (°C)
- 🔁 Automatically refreshes at regular intervals
- 🖥️ Lightweight and non-intrusive
- 📡 Uses free weather APIs (Open‑Meteo + IPInfo)
- 🎨 Icons from [IconMonster](https://iconmonstr.com/)

---

## Preview

![Tray Example](demo.gif)

---

## Weather Support

Currently, WeatherPeek supports a simplified range of common weather conditions — enough to cover most typical use cases (e.g. clear sky, rain, snow, clouds, etc.), both in day and night variations.

🔧 **Planned improvements:**
- Expand icon support for more nuanced conditions
- Add optional features

---

## Tech Stack 

- Python 3.x  
- [PyQt5](https://pypi.org/project/PyQt5/)  
- [Requests](https://pypi.org/project/requests/)  
- [Open-Meteo API](https://open-meteo.com/)  
- [IPInfo.io](https://ipinfo.io/)  
- [PyInstaller](https://www.pyinstaller.org/) for packaging

---

## Download

👉 [Grab the latest release](https://github.com/mwahaj36/Weather-Peek/releases)

- ✅ Pre-built `.exe` for Windows  
- 🧪 Python source version for Linux/macOS  

> No installation needed — just run the `.exe`!

---

## Optional Setup for WeatherPeek (Windows)

### ✅ Make Tray Icon Always Visible

1. **Right-click** on the taskbar → choose **Taskbar settings**  
2. Scroll to **Notification area** → click **"Select which icons appear on the taskbar"**  
3. Find **WeatherPeek** in the list  
4. Toggle it **ON**  

---

### 🚀 Run WeatherPeek on Startup Automatically

1. Press `Win + R` to open the **Run** dialog  
2. Type: `shell:startup` and press **Enter**  
3. Copy the `WeatherPeek.exe` file (or a shortcut to it) into the folder that opens

> Now it will launch automatically each time you log in.

---

## Installation (From Source)

```bash
git clone https://github.com/mwahaj36/Weather-Peek.git
cd Weather-Peek
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python main.py
