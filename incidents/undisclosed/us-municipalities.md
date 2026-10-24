# US municipalities: Heber City UT, Vicksburg MS, Radford VA, Everett MA; Springfield (MA) Public Schools

| | |
|---|---|
| **Date** | 2026-10-10 (Sep 8 to Oct 10) |
| **Sector / country** | Local government / Education · US |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Separate cyber incidents disrupting local services.

## Impact
Systems offline, including utility payments, email and phones; Springfield schools temporarily closed.

## Why it happened (root cause)
Not disclosed.

## How it could have been prevented
- Use the free CISA and MS-ISAC services for local governments (vulnerability scanning, MDBR, incident response).
- Phishing-resistant MFA on email, plus offline backups.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
