# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![make.fun rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/idn45-agent/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![make.fun reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/idn45-agent/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A one-line joke about working beside AI coding agents, for developers who
work beside them every day. Entry for the
[make.fun bounty](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112).

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the joke to
`/output/entry.txt`: one line, 1–280 characters. It self-checks the gate
before writing — the text must be non-blank, a single line, and within
1–280 Unicode code points — and fails hard otherwise.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
