@echo off
echo ================================
echo SMART ANALYTICS SYSTEM STARTING
echo ================================

echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Step 1: Running ETL pipeline...
python etl\extract.py
python etl\transform.py
python etl\load.py

echo.
echo Step 2: Training ML model...
python ml\train_model.py

echo.
echo Step 3: Starting Flask API...
start cmd /k "call venv\Scripts\activate && python api\app.py"

echo Waiting for API to start...
timeout /t 5 > nul

echo.
echo Step 4: Starting Streamlit Dashboard...
start cmd /k "call venv\Scripts\activate && streamlit run dashboard\app.py"

echo.
echo ================================
echo SYSTEM IS UP
echo API  -> http://127.0.0.1:5000
echo UI   -> http://localhost:8501
echo ================================
pause
