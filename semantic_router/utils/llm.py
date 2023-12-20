import os

import openai

from semantic_router.utils.logger import logger


async def llm(prompt: str) -> str | None:
    try:
        client = openai.AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

        completion = await client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.01,
            max_tokens=200,
        )

        output = completion.choices[0].message.content

        if not output:
            raise Exception("No output generated")
        return output
    except Exception as e:
        logger.error(f"LLM error: {e}")
        raise Exception(f"LLM error: {e}")