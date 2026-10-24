# Denmark Central Population Registry (CPR) and Technical University of Denmark (DTU)

| | |
|---|---|
| **Date** | 2026-10-10 (October 2026) |
| **Sector / country** | Government / Education · Denmark |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Reported (secondary sources) |
| **Attacker** | Unknown |

## What happened
Reported breaches of the national civil registry and of DTU's identity and access management systems, with large-scale exfiltration at DTU.

## Impact
CPR: 8.8M people (names, addresses, CPR numbers). DTU: about 200,000 people from identity and access management systems.

## Why it happened (root cause)
Not disclosed.

## How it could have been prevented
- Treat the IAM system itself as tier 0, with privileged-access workstations and MFA for admins.
- Monitor bulk directory exports.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)
- [Tech.co: Data breaches that have happened this year (2026)](https://tech.co/news/data-breaches-updated-list)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
