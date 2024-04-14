from models.OsuFileFormatV14 import OsuFileFormatV14


def main():
    osu_file = OsuFileFormatV14(
        r"C:\Users\tien-\AppData\Local\osu!\Songs\-45 - System Sun\-45 - System Sun (Defectum) [as].osu"
    )
    assert osu_file.general.Mode == "1", "The gamemode for the .osu must be osu! taiko."

    print(osu_file.timing_points.red_lines)


if __name__ == "__main__":
    main()
