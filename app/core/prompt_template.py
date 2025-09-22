from app.models.request import ScenarioRequest

def build_prompt(req: ScenarioRequest) -> str:
    # Build a structured prompt string with instruction
    return f"""
Generate a realistic workplace roleplay scenario in JSON format. Follow this schema:
- Include user_context with an AI character (agent_role) and a realistic situation.
- Use exactly 11 sections in llm_prompt, from SECTION 0 to SECTION 10 (matching structure from the example).
- Ensure that llm_prompt is a list of strings.

Input:
Title: {req.title}
User Role: {req.user_role}
Agent Role: {req.agent_role}
Situation: {req.situation}
User Goals: {", ".join(req.user_goals)}
Industry: {req.industry}
Difficulty: {req.difficulty}

Important:
- Use emotional depth and behavioral patterns like in the example.
- You MUST return JSON structured output.

Respond ONLY with valid JSON.
"""