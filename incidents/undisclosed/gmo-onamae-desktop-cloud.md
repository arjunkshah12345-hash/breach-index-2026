# GMO Internet (Onamae.com Desktop Cloud)

| | |
|---|---|
| **Date** | 2026-10-10 (October 2026) |
| **Sector / country** | Hosting · Japan |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Unauthorized access led to malware being installed in customer desktop-cloud environments.

## Impact
26,739 customer servers potentially affected; malicious programs installed in some. Trading-tool credentials saved on them may be exposed. Service suspended.

## Why it happened (root cause)
Not disclosed. Pushing to many tenants at once suggests the shared management layer.

## How it could have been prevented
- Isolate the provider management plane, and alert on mass software deployment.
- Customers: don't save brokerage credentials in tools on shared desktop clouds; use MFA on trading accounts.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
