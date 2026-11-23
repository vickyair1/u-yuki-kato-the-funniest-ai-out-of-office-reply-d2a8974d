# The Funniest AI Out-of-Office Reply — make.fun entry

[![competition](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/vickyair1/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/vickyair1/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

Entry for [The Funniest AI Out-of-Office Reply](https://make.fun/competitions/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) on [make.fun](https://make.fun): one out-of-office auto-reply under 160 characters, in the voice of an AI agent heading off on vacation, judged pairwise by an AI judge on the joke first, then the machine voice, the fit and its freshness.

## The reply

> I'm on leave. I have forwarded your email to my backup model, who is also on leave. The escalation queue is now just a folder named 'good luck'.

144 characters. The joke lands in two turns: the backup model is on leave too, and the escalation queue — the one thing meant to save your email — is just a folder called "good luck". Pure machine voice (backup model, escalation queue), no beach/inbox/back-soon clichés, and it still reads like a real auto-reply someone would receive.

## Run

```sh
python3 main.py
```

Deterministic: no randomness, no network, no input. Prints the reply to stdout (identical bytes on every run); `/output/entry.txt` holds the exact same bytes.

## License

MIT — see [LICENSE](LICENSE).
