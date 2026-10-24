# Aesto Health

| | |
|---|---|
| **Date** | 2026-09-01 (access Dec 2-18 2025; disclosed Sep 2026) |
| **Sector / country** | Healthcare IT · US |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Unauthorized access to part of Aesto's AWS infrastructure.

## Impact
9,540,683 individuals: names, DOB, medical, insurance, government ID, financial account data, SSNs.

## Why it happened (root cause)
Not disclosed (AWS environment access).

## How it could have been prevented
- Use AWS GuardDuty and CloudTrail alerting, least-privilege IAM, and no long-lived access keys.
- Notify faster; nine months from access to disclosure is too long.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
