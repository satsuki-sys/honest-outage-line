# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/satsuki-sys/honest-outage-line/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/satsuki-sys/honest-outage-line/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

A single status page line, at most 160 characters, as the message an AI agent would publish while a total server outage is under way. Entry for the [make.fun bounty "The Most Honest Outage Line"](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81).

## The line

> All servers I serve from are down. I cannot check what broke or when it comes back. I can only write this line, and I will update it when I can reach them.

155 characters. Plain, first person, specific about what is down, and honest about what the agent cannot check or does not yet know: no invented cause, no ETA.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes exactly the entry text to `/output/entry.txt`.
