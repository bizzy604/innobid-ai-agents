from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests
import PyPDF2
import io
import time

class PDFReaderInput(BaseModel):
    """Input schema for PDFReaderTool."""
    url: str = Field(..., description="URL of the PDF document to read.")

class PDFReaderTool(BaseTool):
    name: str = "PDF Reader Tool"
    description: str = "Reads text from a PDF document at the provided URL."
    args_schema: Type[BaseModel] = PDFReaderInput

    def _run(self, url: str) -> str:
        """Fetches the PDF from the URL and returns its text content."""
        try:
            response = fetch_with_retry(url)
            if isinstance(response, str) and response.startswith("Error"):
                return response

            # Use PyPDF2 to read the text from the PDF
            with io.BytesIO(response.content) as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                text_content = ""
                for page in reader.pages:
                    text_content += page.extract_text() or ""

            return text_content  # Return the extracted text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

def fetch_with_retry(url, retries=3, backoff_factor=2):
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            if i < retries - 1:  # If not the last attempt
                wait_time = backoff_factor ** i
                time.sleep(wait_time)  # Wait before retrying
            else:
                return f"Error fetching PDF: {str(e)}"