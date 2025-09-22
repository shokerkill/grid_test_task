from pydantic import BaseModel
from typing import List, Dict, Union

class AvatarSpeakingTo(BaseModel):
    short_name: str
    full_name: str
    role: str
    summary: str

class ScenarioDetails(BaseModel):
    user_role: str
    what_happened_context: List[str]
    user_goals: List[str]
    user_talking_points: List[str]

class UserContext(BaseModel):
    avatar_speaking_to: AvatarSpeakingTo
    scenario_details: ScenarioDetails

class Simulation(BaseModel):
    llm_prompt: List[str]

class ScenarioResponse(BaseModel):
    user_context: UserContext
    simulation: Simulation