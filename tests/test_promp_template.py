from app.core.prompt_template import build_prompt
from app.models.request import ScenarioRequest

def test_prompt_structure():
    req = ScenarioRequest(
        title="Tough feedback",
        user_role="Manager",
        agent_role="Engineer",
        situation="Underperformance",
        user_goals=["Give feedback", "Maintain trust"],
        difficulty="high",
        industry="Tech"
    )
    prompt = build_prompt(req)
    assert "Generate a realistic workplace roleplay scenario" in prompt