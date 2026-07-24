from config import Config


def parse_config(file_path: str) -> Config:
    """Parse the maze configuration file."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except OSError as e:
        raise ValueError(f"Could not open configuration file: {e}") from e

    width = None
    height = None
    entry = None
    exit_p = None
    output_file = None
    seed = None
    perfect = None

    seen_keys = set()

    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if "=" not in line:
            raise ValueError(f"Invalid configuration line: {line}")

        key, value = map(str.strip, line.split("=", 1))
        key = key.upper()

        if key in seen_keys:
            raise ValueError(f"Duplicate configuration key: {key}")

        seen_keys.add(key)

        if key == "WIDTH":
            try:
                width = int(value)
            except ValueError as e:
                raise ValueError("WIDTH must be an integer.") from e

        elif key == "HEIGHT":
            try:
                height = int(value)
            except ValueError as e:
                raise ValueError("HEIGHT must be an integer.") from e

        elif key == "ENTRY":
            coordinates = value.split(",")

            if len(coordinates) != 2:
                raise ValueError("Invalid ENTRY value.")

            try:
                x, y = map(int, map(str.strip, coordinates))
            except ValueError as e:
                raise ValueError(
                    "ENTRY coordinates must be integers."
                ) from e

            entry = (x, y)

        elif key == "EXIT":
            coordinates = value.split(",")

            if len(coordinates) != 2:
                raise ValueError("Invalid EXIT value.")

            try:
                x, y = map(int, map(str.strip, coordinates))
            except ValueError as e:
                raise ValueError(
                    "EXIT coordinates must be integers."
                ) from e

            exit_p = (x, y)

        elif key == "OUTPUT_FILE":
            output_file = value

            if output_file == "":
                raise ValueError("OUTPUT_FILE cannot be empty.")

        elif key == "SEED":
            try:
                seed = int(value)
            except ValueError as e:
                raise ValueError("SEED must be an integer.") from e

        elif key == "PERFECT":
            if value == "True":
                perfect = True
            elif value == "False":
                perfect = False
            else:
                raise ValueError("PERFECT must be True or False.")

        else:
            raise ValueError(f"Unknown configuration key: {key}")

    if width is None:
        raise ValueError("Missing WIDTH.")

    if height is None:
        raise ValueError("Missing HEIGHT.")

    if entry is None:
        raise ValueError("Missing ENTRY.")

    if exit_p is None:
        raise ValueError("Missing EXIT.")

    if output_file is None:
        raise ValueError("Missing OUTPUT_FILE.")

    if perfect is None:
        raise ValueError("Missing PERFECT.")

    if width <= 0:
        raise ValueError("WIDTH must be greater than zero.")

    if height <= 0:
        raise ValueError("HEIGHT must be greater than zero.")

    entry_x, entry_y = entry
    exit_x, exit_y = exit_p

    if not (0 <= entry_x < width and 0 <= entry_y < height):
        raise ValueError("ENTRY is outside maze bounds.")

    if not (0 <= exit_x < width and 0 <= exit_y < height):
        raise ValueError("EXIT is outside maze bounds.")

    if entry == exit_p:
        raise ValueError("ENTRY and EXIT must be different.")

    return Config(
        width=width,
        height=height,
        entry=entry,
        exit_p=exit_p,
        output_file=output_file,
        perfect=perfect,
        seed=seed,
    )
