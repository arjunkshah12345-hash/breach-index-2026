# Bee Cheng Hiang

| | |
|---|---|
| **Date** | 2026-09-30 (reported Sep 30) |
| **Sector / country** | Retail (food) · Singapore |
| **Attack type** | [Exposed services, misconfiguration and internal error](../../PREVENTION-PLAYBOOK.md#exposure) |
| **Status** | Confirmed |
| **Attacker** | None (internal error) |

## What happened
A bug in AI-assisted code caused bulk marketing emails to reveal recipient addresses.

## Impact
95,364 customer email addresses exposed to other recipients. No misuse found.

## Why it happened (root cause)
AI-generated code shipped without adequate review or testing of a privacy-sensitive path.

## How it could have been prevented
- Review and test AI-written code like any other, especially anything that touches customer data.
- Send bulk email through an ESP that sends one message per recipient, never multi-recipient To or CC.
- Do a canary send to an internal list before any bulk send.

### Baseline controls for this attack type
- Default-deny network exposure. Scan your own IP space and cloud accounts continuously for open databases, storage buckets and admin and AI-agent panels.
- Require authentication on every internal tool, including self-hosted AI agent platforms, even if it is 'just a test'.
- Run cloud posture management (CSPM) with alerts on public resources.
- Code-review and test any automated customer messaging. AI-generated code needs the same review as human-written code.
- Log and rate-limit, so sustained automated probing is visible.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
