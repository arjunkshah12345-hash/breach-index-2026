# Quest Diagnostics (Quanum Lab Services Manager)

| | |
|---|---|
| **Date** | 2026-10-21 (discovered Oct 21; 8-K filed Oct 22) |
| **Sector / country** | Healthcare · US |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Unauthorized access to Quanum, Quest's lab ordering and billing system, which involved 'certain patient records'.

## Impact
Patient personal information and records (PHI) taken. Count not disclosed. Quanum is used by about 500,000 clinicians across North America.

## Why it happened (root cause)
Not disclosed.

## How it could have been prevented
- Phishing-resistant MFA for every clinician and admin login to Quanum-type portals.
- Bulk-export detection on PHI systems.
- Quest's 2019 breach (11.9M records) came through a billing vendor; review third-party access to Quanum too.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [TechCrunch: Quest Diagnostics confirms patient data compromised (2026-10-23)](https://techcrunch.com/2026/10/23/lab-testing-giant-quest-diagnostics-confirms-patients-personal-and-health-data-was-compromised-during-breach/)
- [Tech Insider: Quest Diagnostics Quanum LSM breach](https://tech-insider.org/quest-diagnostics-quanum-lsm-breach-2026/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
