from dataclasses import dataclass

from .section_utils import get_section


class TimingPointsSection:
    def __init__(self, file_path: str) -> None:
        settings = get_section("TimingPoints", file_path)

        # Only handle bpm changes as for now.
        self.red_lines: list[TimingPoint] = []

        for setting in settings:
            (
                time,
                beat_length,
                meter,
                sample_set,
                sample_index,
                volume,
                uninherited,
                effects,
            ) = setting.split(",")

            # Skip green lines
            if uninherited == "0":
                continue

            self.red_lines.append(
                TimingPoint(
                    time,
                    beat_length,
                    meter,
                    sample_set,
                    sample_index,
                    volume,
                    uninherited,
                    effects,
                )
            )


@dataclass
class TimingPoint:
    time: str
    beat_length: str
    meter: str
    sample_set: str
    sample_index: str
    volume: str
    uninherited: str
    effects: str
