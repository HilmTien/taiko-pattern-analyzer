from .section_utils import get_section


class GeneralSection:
    def __init__(self, file_path: str) -> None:
        settings = get_section("General", file_path)

        # Type hint
        self.AudioFilename: str
        self.AudioLeadIn: str
        self.PreviewTime: str
        self.Countdown: str
        self.SampleSet: str
        self.StackLeniency: str
        self.Mode: str
        self.LetterboxInBreaks: str
        self.WidescreenStoryboard: str

        # Trust the system
        for setting in settings:
            key, val = setting.split(": ")
            setattr(self, key, val)
