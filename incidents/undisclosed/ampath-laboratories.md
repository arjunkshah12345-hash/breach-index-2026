# Ampath Laboratories

| | |
|---|---|
| **Date** | 2026-10-15 (October 2026) |
| **Sector / country** | Healthcare (pathology) · South Africa |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Claimed (unverified) |
| **Attacker** | BytetoBreach |

## What happened
Ransomware attack and data-theft claim.

## Impact
80M patient records claimed (names, ID numbers, DOB, sex, addresses, emails, phones). Unverified.

## Why it happened (root cause)
Not disclosed.

## How it could have been prevented
- Use the baseline controls for this category.
- Apply data retention limits to historical lab-patient records.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
