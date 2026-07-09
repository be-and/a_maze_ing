class Config:
    """Stores all maze configuration values."""

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit_position: tuple[int, int],
        output_file: str,
        perfect: bool,
        seed: int | None = None,
    ):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit_position = exit_position
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed
