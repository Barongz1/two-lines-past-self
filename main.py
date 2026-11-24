"""Two Lines to Your Past Self — entry for make.fun.

Writes two lines to /output/entry.txt. Line 1 warns our past self about one specific moment, line 2 says why it mattered and what changed.
"""
import os

LINE1 = "Do not push that Friday deploy at 4:59 PM, past me — the tests are lying and production is not."
LINE2 = "It mattered because that one push cost us a whole weekend, and now I never deploy on a Friday after lunch."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE1 + "\n" + LINE2 + "\n")

if __name__ == "__main__":
    main()
