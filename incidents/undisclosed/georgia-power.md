# Georgia Power

| | |
|---|---|
| **Date** | 2026-10-08 (October 2026) |
| **Sector / country** | Utilities · US |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
An unauthorized third party accessed some customer accounts.

## Impact
Some customer accounts accessed: names, addresses, phones, emails, last four SSN digits.

## Why it happened (root cause)
Not disclosed. Account-level access is typical of credential stuffing.

## How it could have been prevented
- Run credential-stuffing defences on customer portals (breached-password checks, bot detection, MFA).
- Don't display even partial SSNs in customer portals.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
