from app.core.config import settings
from google import genai
import openai
import asyncio

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    async def generate(self, prompt: str) -> str:
        import asyncio
        loop = asyncio.get_event_loop()

        def sync_call():
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text

        return await loop.run_in_executor(None, sync_call)


class OpenAIClient:
    def __init__(self):
        openai.api_base = "https://openrouter.ai/api/v1"
        openai.api_key = settings.OPENROUTER_API_KEY

    async def generate(self, messages: list[dict], model: str = "openai/gpt-4o") -> str:
        loop = asyncio.get_event_loop()

        def sync_call():
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                headers={
                    "HTTP-Referer": getattr(settings, "SITE_URL", ""),
                    "X-Title": getattr(settings, "SITE_NAME", ""),
                },
            )
            return response.choices[0].message["content"]

        return await loop.run_in_executor(None, sync_call)