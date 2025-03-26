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
        return "Output from the tool"