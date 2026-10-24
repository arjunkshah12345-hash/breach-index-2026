# Keio Corporation

| | |
|---|---|
| **Date** | 2026-09-26 (attack Sep 26; confirmed Sep 28) |
| **Sector / country** | Transport / hospitality · Japan |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Ransomware hit Keio's business systems.

## Impact
Hospitality and payment business systems disrupted; network shut down for containment. Railway operations unaffected. About 59,000 email addresses reportedly exposed.

## Why it happened (root cause)
Not disclosed.

## How it could have been prevented
- Keep OT (rail) and IT segmented, which appears to have worked here.
- Use immutable backups for payment and hospitality systems.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)
- [Tech.co: Data breaches that have happened this year (2026)](https://tech.co/news/data-breaches-updated-list)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
