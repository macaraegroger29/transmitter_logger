# 🛠️ Transmitter Automation: Setup & Deployment Guide

This guide provides step-by-step instructions to set up the Transmitter Logger on any computer.

---

### 1. Prerequisites
- **Python**: Install Python 3.10+ from [python.org](https://www.python.org/).
- **Google Chrome**: Ensure you have the Chrome browser installed.
- **Chrome WebDriver**: Handled automatically by Selenium 4.6+.

---

### 2. Environment Setup (Recommended)
Using a **Virtual Environment (venv)** prevents conflicts with other Python projects.

1.  **Open terminal** in the project folder.
2.  **Create venv**: `python -m venv .venv`
3.  **Activate**:
    - **Windows**: `.venv\Scripts\activate`
    - **Mac/Linux**: `source .venv/bin/activate`

---

### 3. Install Required Libraries
```powershell
pip install selenium pandas schedule
```

---

### 4. Running the Script
```powershell
python transmitter_logger.py
```

---

### 5. Customizing the Script
You can modify these settings directly in `transmitter_logger.py`:

#### ⏱️ Changing the Timer
Find the **TIMER CONFIGURATION** section at the bottom:
```python
schedule.every(1).minutes.do(read_transmitter) # Change '1' or 'minutes' (e.g. .hours)
```

#### 👁️ Visible vs. Invisible (Headless) Mode
By default, the script runs in "Headless" (invisible) mode. To see the browser window:
- Find `options.add_argument('--headless')` and add a `#` at the start to comment it out.

---

### 6. Key Troubleshooting Tips

| Issue | Solution |
| :--- | :--- |
| **"Permission denied: transmitter_log.csv"** | **VERY COMMON:** You have the CSV open in **Excel**. Excel locks the file. **Close Excel** and the script will resume saving. |
| **"Could not find import..."** | Ensure your editor is using the correct Python interpreter (Ctrl+Shift+P > Select Interpreter). |
| **"ModuleNotFoundError"** | You haven't installed the libraries. Run `pip install...` while your environment is active. |
| **Browser doesn't start** | Ensure Google Chrome is installed on the computer. |

---

### 7. Connection details
The script is configured to connect to the transmitter at **http://192.168.1.14/index.shtml**. Ensure your computer is on the same network as the transmitter to allow data collection.
