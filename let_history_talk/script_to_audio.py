from typing import List, TypedDict

import soundfile as sf
import torch
from kokoro import KPipeline


class DialoguePart(TypedDict):
    role: str
    message: str


class ScriptToAudio:
    "A class to convert a script to speech."


    def __init__(self, lang_code: str = "a"):
        """Init class.

        Args:
            lang_code (str, optional): See kokoro languages. Defaults to "a".
        """
        self.pipeline = KPipeline(lang_code=lang_code, repo_id="hexgrad/Kokoro-82M")

    def generate(
        self,
        script: List[DialoguePart],
        output_path: str | None = None,
        host_voice: str = "af_heart",
        guest_voice: str = "../out/am_eric.pt",
    ) -> torch.Tensor:
        """Generate audion from a podcast script.

        Args:
            script (List[DialoguePart]): The script to convert to audio.
            output_path (str | None, optional): If set the audio file is saved to this path. Defaults to None.
            host_voice (str, optional): A path to a voice.pt or the name of one of the default voices. Defaults to "af_heart".
            guest_voice (str, optional): A path to a voice.pt or the name of one of the default voices. Defaults to "../out/am_eric.pt".

        Returns:
            torch.Tensor: The final podcast audio.
        """

        output_audio_list = []

        for part in script:
            if part["role"] == "host":
                voice = host_voice
            else:
                voice = guest_voice

            generator = self.pipeline(
                part["message"],
                voice=voice,  # <= change voice here
                speed=1,
                split_pattern=None,
            )

            _, _, audio = next(generator)

            output_audio_list.append(audio)

        output_audio = torch.cat(output_audio_list, dim=0)

        if output_path:
            sf.write(output_path, output_audio, 24000)

        return output_audio