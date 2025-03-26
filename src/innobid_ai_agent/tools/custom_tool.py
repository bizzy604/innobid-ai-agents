from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field



class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, documents, argument: str) -> str:
        # Implementation goes here
        results = []
        for doc in documents:
            doc_name = doc.get('fileName', doc.get('name', 'Unknown Document'))
            doc_type = doc.get('fileType', doc.get('type', 'Unknown type'))
            doc_url = doc.get('url', '')

            if not doc_url:
                results.append(f"No URL provided for document: {doc_name}")
                continue

            content = self.analyze_document(doc_url, doc_type)
            results.append(f"Document: {doc_name}\nType: {doc_type}\nContent:\n{content}\n{'='*50}\n")

        return "\n".join(results)

    def analyze_document(self, url: str, file_type: str) -> str:
        """Analyze document based on its type"""
        if file_type.lower() in ['pdf', 'application/pdf']:
            return self.read_pdf(url)
        elif file_type.lower() in ['txt', 'text/plain', 'doc', 'docx']:
            return self.read_text_file(url)
        else:
            return f"Unsupported file type: {file_type}"
    
    def read_pdf(self, url: str) -> str:
        """Read PDF content from URL"""
        try:
            response = requests.get(url)
            pdf_file = io.BytesIO(response.content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF from {url}: {e}")
            return f"Error reading PDF: {str(e)}"