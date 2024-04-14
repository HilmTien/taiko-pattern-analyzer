from .timing_points_section import TimingPointsSection
from .general_section import GeneralSection


class OsuFileFormatV14:
    def __init__(self, file_path: str) -> None:
        with open(file_path, encoding="utf-8") as osu_file:
            assert osu_file.readline() == "osu file format v14\n"

        self.general = GeneralSection(file_path)
        self.timing_points = TimingPointsSection(file_path)
