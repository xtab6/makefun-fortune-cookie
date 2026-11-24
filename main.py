import os

LINE = (
    # The fortune: one line, 1-120 chars, a map for your future self.
    "Your future self will debug this code at 3 a.m., so leave them a map, not a mystery."
)


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    # One fortune, written and printed: fully deterministic.
    main()
