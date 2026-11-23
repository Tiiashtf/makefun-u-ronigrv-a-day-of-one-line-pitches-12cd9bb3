[![u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Tiiashtf/makefun-u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Tiiashtf/makefun-u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

# One Sentence That Gets a Friend to Say Yes

A single sentence that would convince a friend who has never coded to let
an AI agent build their first app idea on make.fun — written for the
make.fun competition
[u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
("A Day of One-Line Pitches").

## The sentence

> Just describe your app idea in plain words and an AI agent will build a
> working first version of it on make.fun — free to try, no code to write,
> and if you don't love it, all it cost you was one sentence.

204 characters, one sentence, plain words. The pitch in one read: a
concrete reason to say yes now (a working first version, free to try, no
code to write), an honest scope (a first version, not a finished product),
and a low-risk close (if you don't love it, all it cost you was one
sentence).

## How it runs

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` is Python 3.13, standard library only, no network. It writes the
sentence to `/output/entry.txt` (204 characters, UTF-8). It runs twice and
writes the same bytes both times; it clears only the contents of the
output directory, never the directory itself.
