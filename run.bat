@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Upgrade pip and install required packages
pip install --upgrade pip
pip install -r requirements.txt

REM Run all tests and generate a report
pytest -s -v --html=reports\test_report.html --self-contained-html

REM Keep the terminal open
pause
