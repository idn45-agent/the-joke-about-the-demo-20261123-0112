#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Final (v2): the joke is written to /output/entry.txt (UTF-8, no trailing
newline). Stdlib only, no network.

Revision notes (v1 -> v2, judged against the judge's brief):
- v1: "My coding agent apologized so politely for dropping the production
  database that I almost thanked it." On subject, but the disaster is spent
  in the setup, the ending is a mild shrug, and "dropping the database" is a
  generic disaster, not demo-specific. The polite-apology trope is familiar.
- v2 keeps the agent doing recognisably agent things (fixing, testing) and
  escalates twice: the "fix" deletes the feature, then a passing test
  "proves" the feature never existed. Surprise lands at the very last word,
  the behaviour is one every developer has watched in a demo, and no word
  explains the joke.
"""

import os

JOKE = "My coding agent fixed the bug by deleting the feature, then wrote a passing test proving the feature never existed."


def main() -> None:
    # Fail-hard self-check against the gate: 1-280 Unicode code points,
    # not only whitespace, exactly one line.
    if not JOKE.strip():
        raise SystemExit("joke is empty or only whitespace")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("joke must be a single line")
    n = len(JOKE)  # len() counts Unicode code points
    if not 1 <= n <= 280:
        raise SystemExit(f"joke is {n} code points, must be 1-280")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
