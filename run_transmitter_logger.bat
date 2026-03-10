@echo off
cd /d "c:\Users\jao\projects\automation"
:: Activate the virtual environment if it exists
if exist ".venv\Scripts\activate" (
    call .venv\Scripts\activate
)
:: Run the script
python transmitter_logger.py
pause
