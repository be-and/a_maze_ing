import subprocess
import re

MAX_SEED = 1000
failed = []

for seed in range(1, MAX_SEED + 1):

    print(f"Testing seed {seed}/{MAX_SEED}")

    # Update the seed in config.txt
    with open("config.txt", "r") as f:
        config = f.read()

    config = re.sub(r"SEED=\d+", f"SEED={seed}", config)

    with open("config.txt", "w") as f:
        f.write(config)

    # Run your program:
    # 4 = Save maze
    # 5 = Exit
    subprocess.run(
        ["python3", "a_maze_ing.py", "config.txt"],
        input="4\n5\n",
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    # Run the analyzer
    result = subprocess.run(
        ["python3", "maze_analyzer.py", "maze.txt"],
        capture_output=True,
        text=True,
        check=True,
    )

    # Check whether the maze failed
    if "Not Pac-Man-ready" in result.stdout:
        failed.append(seed)
        print(f"❌ Seed {seed} failed.")

print("\n==============================")

if failed:
    print("The following seeds failed:")
    print(failed)
else:
    print(f"✅ All {MAX_SEED} seeds passed!")
