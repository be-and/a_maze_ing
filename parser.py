from config import Config


def parse_config(file_path: str) -> Config:
    """Read a maze configuration file and return a Config object."""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    width = None
    height = None
    entry = None
    exit_position = None
    output_file = None
    seed = None
    perfect = None

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("#"):
            continue

        parts = line.split("=")

        if len(parts) != 2:
            raise ValueError("Invalid configuration line.")

        key = parts[0]
        value = parts[1]

        if key == "WIDTH":
            width = int(value)

        elif key == "HEIGHT":
            height = int(value)

        elif key == "ENTRY":
            coordinates = value.split(",")

            if len(coordinates) != 2:
                raise ValueError("Invalid ENTRY value.")

            x = int(coordinates[0])
            y = int(coordinates[1])
            entry = (x, y)

        elif key == "EXIT":
            coordinates = value.split(",")

            if len(coordinates) != 2:
                raise ValueError("Invalid EXIT value.")

            x = int(coordinates[0])
            y = int(coordinates[1])
            exit_position = (x, y)

        elif key == "OUTPUT_FILE":
            output_file = value

        elif key == "SEED":
            seed = int(value)

        elif key == "PERFECT":
            if value == "True":
                perfect = True
            elif value == "False":
                perfect = False
            else:
                raise ValueError("PERFECT must be True or False.")

        else:
            raise ValueError(f"Unknown configuration key: {key}")

    if None in (
        width,
        height,
        entry,
        exit_position,
        output_file,
        perfect,
    ):
        raise ValueError("Missing required configuration values.")

    return Config(
        width,
        height,
        entry,
        exit_position,
        output_file,
        perfect,
        seed,
    )
