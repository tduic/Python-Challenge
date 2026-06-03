# Python-Challenge

My solutions to [The Python Challenge](http://www.pythonchallenge.com/), a series of riddle-style programming puzzles where each level is solved by writing a small Python script, and the answer reveals the URL of the next level.

This repo covers levels 0 through 17. Each level lives in its own script under `env/`, and the puzzle assets (images, text, pickled data) it operates on are kept in `env/txt/`.

## What's inside

Each `env/challengeNN.py` file defines a `challengeN(...)` function and a small `__main__` block that runs it. The puzzles exercise a broad range of standard-library and third-party techniques, for example:

- **challenge0** - arithmetic (`2**38`).
- **challenge01** - Caesar/ROT cipher decoding with `str.maketrans` / `str.translate`.
- **challenge02 / challenge03** - text filtering and regex extraction (`re`, `string`).
- **challenge04** - following a chain of HTTP redirects via `requests` and regex.
- **challenge05** - loading a remote pickled "banner" with `pickle` + `urllib` and rendering it.
- **challenge08** - extracting and `bz2`-decompressing credentials hidden in an HTML comment.
- **challenge11 / challenge14 / challenge16 / challenge17** - pixel-level image processing with **Pillow (PIL)** (deinterlacing, unrolling a spiral, GIF/image manipulation).

Helper file `env/utils.py` provides small `readFile` / `writeFile` wrappers used by several challenges.

## Layout

\`\`\`
env/
  challenge0.py ... challenge17.py   # one script per puzzle level
  utils.py                           # file read/write helpers
  txt/                               # puzzle inputs/assets (jpg, png, gif, txt, pickled data)
\`\`\`

## Requirements

- Python 3.7+
- [\`requests\`](https://pypi.org/project/requests/) (network challenges)
- [\`Pillow\`](https://pypi.org/project/Pillow/) (image challenges)

\`\`\`bash
pip install requests Pillow
\`\`\`

## Running

Run an individual challenge from inside the \`env\` directory (the scripts use paths relative to \`env/\`, e.g. \`txt/...\`):

\`\`\`bash
cd env
python challenge02.py
\`\`\`

Network-based challenges (4, 5, 8, ...) fetch data live from \`pythonchallenge.com\`, so they require an internet connection.

## Notes

These are personal solutions / learning exercises. Some later levels are partial or stubbed.
