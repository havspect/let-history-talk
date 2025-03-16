from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class PodcastScript(BaseModel):
    """A generated podcast script with dialogue between a host and a guest speaker."""

    title: str = Field(
        description="The title of the podcast episode",
        examples=["The Future of AI in Healthcare"],
    )
    host: str = Field(description="The name of the podcast host", examples=["Alicia"])
    guest: str = Field(
        description="The name of the guest speaker", examples=["Dr. Smith"]
    )
    dialogue: List[Dict[str, str]] = Field(
        description="The dialogue between the host and the guest",
        examples=[
            {
                "role": "host",
                "message": "Hello, Dr. Smith. It's great to have you on the show.",
            },
            {
                "role": "guest",
                "message": "Thank you, Alicia. I'm excited to discuss the latest advancements in AI.",
            },
        ],
    )


class PodcastResponse(BaseModel):
    """The response containing the podcast script and brainstorming ideas."""

    scratchpad: Optional[str | None] = Field(
        default=None, description="Your brainstorming ideas for the podcast script"
    )
    podcast_script: PodcastScript = Field(description="The generated podcast script")
