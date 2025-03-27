from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from crewai_tools import PDFSearchTool
import os
from dotenv import load_dotenv
from typing import Type
from crewai.tools import BaseTool
import requests
from innobid_ai_agent.tools.DocumentReader import PDFReaderTool 
load_dotenv()


ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

class Results(BaseModel):
    score: int
    report: str

class AggregateResults(BaseModel):
    document_analysis: Results
    initial_screening: Results
    compliance: Results
    risk_assessment: Results
    comparative_analysis: Results
    award_recommendation: Results
    summary: Results

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class InnobidAiAgent():
    """InnobidAiAgent crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def document_reader_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['document_reader_agent'],
            tool=PDFReaderTool(),
            verbose=True,
            
        )
    
    @agent
    def initial_screening_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['initial_screening_agent'],
            verbose=True
        )
    
    @agent
    def compliance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['compliance_agent'],
            verbose=True
        )
    
    @agent
    def risk_assessment_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['risk_assessment_agent'],
            verbose=True
        )
    
    @agent
    def comparative_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comparative_analysis_agent'],
            verbose=True
        )
    
    @agent
    def award_recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['award_recommendation_agent'],
            verbose=True
        )

    @agent
    def summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summary_agent'],
        )
    

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def document_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_analyst_task'],
        )
    
    @task
    def initial_screening_task(self) -> Task:
        return Task(
            config=self.tasks_config['initial_screening_task'],
        )

    @task
    def initial_screening_task(self) -> Task:
        return Task(
            config=self.tasks_config['initial_screening_task'],
        )
    
    @task
    def compliance_task(self) -> Task:
        return Task(
            config=self.tasks_config['compliance_task'],
        )

    @task
    def risk_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['risk_assessment_task'],
        )
    
    @task
    def comparative_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['comparative_analysis_task'],
        )
    
    @task
    def award_recommendation_taskk(self) -> Task:
        return Task(
            config=self.tasks_config['award_recommendation_task'],
        )
    
    @task
    def summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['summary_task'],
            output_pydantic = AggregateResults
        )

    @crew
    def crew(self) -> Crew:
        """Creates the InnobidAiAgent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
