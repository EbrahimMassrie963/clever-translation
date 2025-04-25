@echo off

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Run the FastAPI app using uvicorn
uvicorn backend.app.main:app --reload


pause
