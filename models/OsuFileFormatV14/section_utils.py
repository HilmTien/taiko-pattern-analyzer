from typing import Literal


Section = Literal[
    "General",
    "Editor",
    "Metadata",
    "Difficulty",
    "Events",
    "TimingPoints",
    "Colours",
    "HitObjects",
]


def get_section(section_name: Section, file_path: str) -> list[str]:
    settings = []

    with open(file_path, encoding="utf-8") as osu_file:
        for line in osu_file:
            # Find the section in the .osu
            if f"[{section_name}]" not in line:
                continue

            lines = map(lambda line: line.strip(), osu_file.readlines())

            for setting_line in lines:
                # Exit flag for current section
                if not setting_line:
                    break

                settings.append(setting_line)

    return settings
