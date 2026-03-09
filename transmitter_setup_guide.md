# 🛠️ Transmitter Automation: Setup & Deployment Guide

This guide provides step-by-step instructions to set up the Transmitter Logger on any computer.

---

### 1. Prerequisites
- **Python**: Install Python 3.10+ from [python.org](https://www.python.org/).
- **Google Chrome**: Ensure you have the Chrome browser installed.
- **Chrome WebDriver**: Modern Selenium versions (4.6+) handle this automatically, so no separate download is usually needed.

---

### 2. Environment Setup
It is best practice to use a **Virtual Environment (venv)** to keep your global Python installation clean.

1.  **Open your terminal/command prompt** in the project folder.
2.  **Create the environment**:
    ```powershell
    python -m venv .venv
    ```
3.  **Activate the environment**:
    - **Windows**: `.venv\Scripts\activate`
    - **Mac/Linux**: `source .venv/bin/activate`

---

### 3. Install Required Libraries
Once the environment is active, install the necessary Python packages:

```powershell
pip install selenium pandas schedule
```

---

### 4. Project Structure
Ensure your folder contains these two primary files:
- `transmitter_logger.py`: The Python script (renamed from `transmitter_logger` to include the `.py` extension).
- `test_transmitter.html`: The HTML status page you want to monitor.

---

### 5. Running the Script
Run the script using the Python interpreter:

```powershell
python transmitter_logger.py
```

---

### 6. Key Troubleshooting Tips
| Issue | Solution |
| :--- | :--- |
| **"Could not find import..."** | Ensure the file has a `.py` extension and you've selected the correct Python interpreter in your editor. |
| **"ModuleNotFoundError"** | You haven't installed the `pip` packages in the *current* active environment. Run the install command again. |
| **File Path Errors** | The script uses `os.path` to find the HTML file. Ensure the `.html` file is in the same folder as the `.py` script. |
| **Browser Fails to Open** | Ensure Chrome is installed. Selenium will automatically download the correct driver. |

---

### 7. File Renaming (Crucial)
If you are moving this from a system where the file was just called `transmitter_logger`, **always rename it** to `transmitter_logger.py`. Python scripts must have the `.py` extension for standard execution and IDE support.
