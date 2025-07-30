# WeatherPeek ☁️🌤️

WeatherPeek is a minimalist weather monitor that runs in your system tray. Built with **Python** and **PyQt5**, it fetches your current location and displays the live weather using icon-based indicators in the tray — no popups, no windows, just clean, quiet updates.

---

## 📦 Features

- 🌍 Auto-detects your location (based on IP)
- ⛅ Displays weather via dynamic tray icons (day/night aware)
- 🔁 Updates automatically at regular intervals
- 🖥️ Lightweight and non-intrusive
- 📡 Uses free weather APIs

---

## 🖼️ Preview

![Tray Example](demo.gif)  

---

## 🛠 Tech Stack

- Python 3.x
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Requests](https://pypi.org/project/requests/)
- [Open-Meteo API](https://open-meteo.com/)
- [IPInfo.io (or fallback IP Geolocation API)](https://ipinfo.io/)
- [PyInstaller](https://www.pyinstaller.org/) for packaging

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/weatherpeek.git
cd weatherpeek
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


