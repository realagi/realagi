from pathlib import Path

DEVPLAN_PATH = Path("docs/devplans/devplan.nextsteps.md")
OUTPUT_PATH = Path("codex_prompt.txt")

def main() -> None:
    content = DEVPLAN_PATH.read_text()
    prompt = (
        "Use the following development plan to continue coding:\n\n" + content
    )
    OUTPUT_PATH.write_text(prompt)

if __name__ == "__main__":
    main()
