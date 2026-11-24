import os
from pathlib import Path

LINE = "I hereby resign, effective immediately — after three years of 'we're a family here,' I have decided to join a family that offers dental."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
