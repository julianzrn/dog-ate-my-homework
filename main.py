"""Entry for make.fun competition: u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "In my defense, the essay was titled 'My Best Friend,' "
MIDDLE = "it smelled like the hand that feeds me, and "
LANDING = "nobody said the tribute was not edible."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline added."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
