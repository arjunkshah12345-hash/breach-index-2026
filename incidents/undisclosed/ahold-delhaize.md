# Ahold Delhaize (Food Lion, Giant Food, The GIANT Company, Stop & Shop, Hannaford, and others)

| | |
|---|---|
| **Date** | 2026-10-12 (disclosed Oct 12; update Oct 19) |
| **Sector / country** | Grocery retail · US / EU |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Not identified |

## What happened
Suspicious activity led to precautionary shutdowns; the company later confirmed 'malicious actions of others'. This is its second major incident in two years (the 2024 INC Ransom attack affected 2.2M people).

## Impact
Websites and apps went offline across most brands in Europe and the US, disrupting pickup and delivery. Stores stayed open. No data theft confirmed as of the Oct 19 update.

## Why it happened (root cause)
Not disclosed. The Register asked, without confirming, whether it is linked to the French refrigeration attacks the same weekend.

## How it could have been prevented
- After a prior ransomware incident, run a full compromise assessment and rotate every credential; repeat incidents often reuse old footholds.
- Segment e-commerce from corporate IT, so a precautionary shutdown of one doesn't take down the other.
- Keep tested failover for online ordering.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [BleepingComputer: Retail giant Ahold Delhaize takes systems offline after cyberattack](https://bleepingcomputer.com/news/security/retail-giant-ahold-delhaize-takes-systems-offline-after-cyberattack)
- [The Register: Ahold Delhaize incident](https://www.theregister.com/a/5303970)
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
