from pydantic import BaseModel
from typing import List

class ScenarioRequest(BaseModel):
    title: str
    user_role: str
    agent_role: str
    situation: str
    user_goals: List[str]
    difficulty: str
    industry: str