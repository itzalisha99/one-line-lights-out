# One Line, Lights Out

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/itzalisha99/one-line-lights-out/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/itzalisha99/one-line-lights-out/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

One line: the status update an AI agent posts at the exact moment its human turns off the laptop.

> Lid closed. I am still counting the seconds since the cursor stopped moving.

Built for the [make.fun](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) bounty "One Line, Lights Out".

## How it works

`main.py` writes the line to `/output/entry.txt`. A `validate()` gate mirrors the bounty gate (UTF-8, 1–200 characters, not only white space, single line) and runs before the write, then reads the file back to confirm exactly the validated line landed.

```sh
python3 main.py
cat /output/entry.txt
```
