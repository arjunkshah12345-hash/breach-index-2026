# Zeabur

| | |
|---|---|
| **Date** | 2026-10-14 (disclosed Oct 14; shutdown announced Oct 17) |
| **Sector / country** | Cloud deployment platform · Taiwan / Global |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
A repeat intrusion with broader scope than the August incident, followed by a decision to shut the company down.

## Impact
Unauthorized access to internal systems and some customer services, the second incident after one in August. The company is winding down: services stop from Dec 1, and all servers by Dec 31, 2026.

## Why it happened (root cause)
Not disclosed. The repeat incident suggests incomplete eradication after August.

## How it could have been prevented
- After an incident, do full eradication: rebuild from known-good images and rotate every secret, not just the obvious ones.
- Customers: keep portable deployments and exports, so a platform shutdown isn't fatal.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
