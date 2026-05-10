import google.generativeai as genai
import os

from app.agents.architecture_agent import architecture_analysis
from app.agents.api_agent import api_analysis
from app.agents.security_agent import security_analysis
from app.agents.pm_agent import pm_documentation

from app.utils.logger import logger
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_documentation(code_content):

    try:

        logger.info("Starting Multi-Agent Analysis")

        architecture_report = architecture_analysis(
            model,
            code_content
        )

        api_report = api_analysis(
            model,
            code_content
        )

        security_report = security_analysis(
            model,
            code_content
        )

        pm_report = pm_documentation(
            model,
            code_content
        )

        technical_report = f"""

# Technical Documentation

{architecture_report}

{api_report}

{security_report}
"""

        product_report = f"""

# Product Management Documentation

{pm_report}
"""

        final_report = f"""

# Multi-Agent AI Documentation Report

{technical_report}

{product_report}
"""

        logger.info("Report Generated Successfully")

        return final_report

    except Exception as e:

        logger.error(str(e))

        return f"Error generating documentation: {str(e)}"