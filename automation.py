import subprocess

commands = [
    ["node", "generate-json.js"],
    ["git", "add", "."],
    ["git", "commit", "-m", "PYQ added"],
    ["git", "push", "origin", "main"]
]

for command in commands:
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"Error while running: {' '.join(command)}")
        break