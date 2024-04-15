from dataclasses import dataclass

from .section_utils import get_section


class HitObjectsSection:
    def __init__(self, file_path: str) -> None:
        settings = get_section("HitObjects", file_path)

        self.hit_objects: list[HitObject] = []

        for setting in settings:
            (x, y, time, type_, hitsound, *object_params, hit_sample) = setting.split(
                ","
            )

            self.hit_objects.append(
                HitObject(x, y, time, type_, hitsound, object_params, hit_sample)
            )


@dataclass
class HitObject:
    x: str
    y: str
    time: str
    type_: str
    hitsound: str
    object_params: str
    hit_sample: str
