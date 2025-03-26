#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from innobid_ai_agent.crew import InnobidAiAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "id": "cm82yphg30001la09o92qjcy4",
        "amount": 150000,
        "completion_time": "4 months",
        "technical_proposal": "Our technical approach for the AI Integration System is structured around a phased, agile methodology designed to ensure seamless integration with your existing systems while providing scalability and robust security",
        "vendor_experience": "Your vendor experience here...",
        "documents": [
            {"name": "Document1.pdf", "url": "https://bursary.s3.us-east-1.amazonaws.com/tender-docs/2/69028487-22d1-4e8c-8f13-4977c073e320/b18a68ed-9bd1-42f8-8bb5-e88a33f61777.pdf"}
        ],
        "bidder": {"company": "Amoni Kevin"},
        "tender": {
            "budget": 200000,
            "requirements": [
                "Proven experience in AI system design and integration.",
                "Detailed technical proposal including project timelines and milestones.",
                "Case studies or references from previous successful projects.",
                "Comprehensive cost breakdown and competitive pricing.",
                "Strategy for post-implementation support and training.",
                "Compliance with local industry standards and security protocols."
            ]
        }
    }
    
    try:
        InnobidAiAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        InnobidAiAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        InnobidAiAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        InnobidAiAgent().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
