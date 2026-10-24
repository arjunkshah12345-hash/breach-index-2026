# Novocure

| | |
|---|---|
| **Date** | 2026-09-01 (access mid-Aug; reported Sep 1) |
| **Sector / country** | Medical devices · US |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | ShinyHunters |

## What happened
Unauthorized access to some information systems.

## Impact
Internal patient IDs from 1,400+ US records; identifying data for under 50 others; provider and employee contacts.

## Why it happened (root cause)
Not disclosed. ShinyHunters' 2026 playbook is mostly vishing for SSO or SaaS credentials and exploiting PeopleSoft.

## How it could have been prevented
- Use the controls listed under the social-engineering category (help-desk verification, phishing-resistant MFA).
- Review OAuth app grants in SaaS tenants.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)
- [State of Surveillance: ShinyHunters 2026 breach tracker](https://stateofsurveillance.org/news/shinyhunters-2026-breach-tracker-salesforce-carnival-canvas-campaign/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
