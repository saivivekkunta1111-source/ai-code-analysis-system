from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

import shutil
import os
import time

from app.utils.extractor import extract_zip
from app.utils.progress_tracker import progress_status
from app.utils.control_flags import control_flags
from app.utils.logger import logger

from app.analyzer import read_project_files
from app.ai_service import generate_documentation

app = FastAPI()

os.makedirs("uploads", exist_ok=True)
os.makedirs("reports", exist_ok=True)


@app.get("/")
def home():

    return {
        "message": "AI Code Analysis System Running"
    }


@app.get("/status")
def get_status():

    return progress_status


@app.post("/pause")
def pause_analysis():

    control_flags["paused"] = True

    return {
        "message": "Analysis paused"
    }


@app.post("/resume")
def resume_analysis():

    control_flags["paused"] = False

    return {
        "message": "Analysis resumed"
    }


@app.get("/download-report")
def download_report():

    report_path = "reports/report.md"

    if os.path.exists(report_path):

        return FileResponse(
            report_path,
            media_type="text/markdown",
            filename="report.md"
        )

    return {
        "error": "Report not found"
    }


@app.post("/analyze")
async def analyze_project(file: UploadFile = File(...)):

    try:

        logger.info("Analysis Started")

        progress_status["current_step"] = "Uploading ZIP"

        zip_path = f"uploads/{file.filename}"

        with open(zip_path, "wb") as buffer:

            shutil.copyfileobj(file.file, buffer)

        while control_flags["paused"]:

            progress_status["current_step"] = "Paused"

            time.sleep(1)

        progress_status["current_step"] = "Extracting Files"

        extract_folder = f"uploads/{file.filename}_data"

        extract_zip(zip_path, extract_folder)

        while control_flags["paused"]:

            progress_status["current_step"] = "Paused"

            time.sleep(1)

        progress_status["current_step"] = "Reading Project Files"

        code_content = read_project_files(extract_folder)

        while control_flags["paused"]:

            progress_status["current_step"] = "Paused"

            time.sleep(1)

        progress_status["current_step"] = "Generating AI Documentation"

        report = generate_documentation(code_content)

        report_path = "reports/report.md"

        with open(report_path, "w", encoding="utf-8") as f:

            f.write(report)

        progress_status["current_step"] = "Completed"
        progress_status["completed"] = True

        logger.info("Analysis Completed")

        return {
            "status": "success",
            "message": "Documentation generated successfully",
            "report": report
        }

    except Exception as e:

        logger.error(str(e))

        return {
            "status": "error",
            "message": str(e)
        }