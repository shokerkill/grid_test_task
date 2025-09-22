from fastapi import APIRouter, HTTPException
from app.models.request import ScenarioRequest
from app.models.response import ScenarioResponse
from app.services.scenario_generator import generate_scenario

router = APIRouter()

@router.post("/generate", response_model=ScenarioResponse)
async def generate(req: ScenarioRequest):
    try:
        return await generate_scenario(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))