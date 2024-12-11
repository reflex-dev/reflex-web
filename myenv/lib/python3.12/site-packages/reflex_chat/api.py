"""Define common AI API functions."""

import os


async def default_process(chat):
    """Process the chat messages.

    Args:
        chat: The chat object.
    """
    chat.append_to_response(
        "Pass the `process` argument to connect the chat to a model."
    )
    yield


def openai(
    client=None,
    model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
):
    """Get the response from the API.

    Args:
        form_data: A dict with the current question.
    """
    from openai import OpenAI
    client = client or OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def process(chat):
        # Start a new session to answer the question.
        session = client.chat.completions.create(
            model=model,
            messages=chat.get_messages(),
            stream=True,
        )

        # Stream the results, yielding after every word.
        for item in session:
            delta = item.choices[0].delta.content
            chat.append_to_response(delta)
            yield

    return process
