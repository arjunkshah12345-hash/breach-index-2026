# Vietnam APIS airline passenger database

| | |
|---|---|
| **Date** | 2026-09-08 (reported Sep 8) |
| **Sector / country** | Aviation / Government · Vietnam |
| **Attack type** | [Exposed services, misconfiguration and internal error](../../PREVENTION-PLAYBOOK.md#exposure) |
| **Status** | Reported (secondary sources) |
| **Attacker** | None identified (exposure) |

## What happened
A misconfigured cloud database holding advance passenger information was publicly reachable until researchers alerted authorities.

## Impact
About 220M records: names, passport numbers, nationality, DOB, flight and seat details.

## Why it happened (root cause)
Cloud database exposed to the internet without authentication.

## How it could have been prevented
- Default-deny network rules on databases, with continuous public-exposure scanning (CSPM).
- Encrypt passport fields, and keep an access log so exposure can be scoped.

### Baseline controls for this attack type
- Default-deny network exposure. Scan your own IP space and cloud accounts continuously for open databases, storage buckets and admin and AI-agent panels.
- Require authentication on every internal tool, including self-hosted AI agent platforms, even if it is 'just a test'.
- Run cloud posture management (CSPM) with alerts on public resources.
- Code-review and test any automated customer messaging. AI-generated code needs the same review as human-written code.
- Log and rate-limit, so sustained automated probing is visible.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
