from app.models.request import ScenarioRequest
from app.models.response import ScenarioResponse
from app.clients.gemini import GeminiClient, OpenAIClient
from app.core.prompt_template import build_prompt
from app.utils.validators import validate_llm_sections
import json

async def generate_scenario(req: ScenarioRequest) -> ScenarioResponse:
    prompt = build_prompt(req)
    client = OpenAIClient()

    # call the OpenAI client
    response_text = await client.generate(
        messages=[
            {"role": "system", "content": "You are a scenario generator. Respond in JSON only."},
            {"role": "user", "content": prompt},
        ]
    )

    parsed = json.loads(response_text)

    if not validate_llm_sections(parsed["simulation"]["llm_prompt"]):
        raise ValueError("LLM output does not contain all required sections.")

    return ScenarioResponse(**parsed)