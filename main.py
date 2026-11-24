"""The Funniest Toaster Error Message — make.fun entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), with no trailing newline.

End-to-end check: to be verified by running.
"""

import os

LINE = "ERROR 04: Lever stuck. The bread refuses to come up. Negotiations have failed."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
