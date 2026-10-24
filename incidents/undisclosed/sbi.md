# State Bank of India (SBI)

| | |
|---|---|
| **Date** | 2026-10-16 (alerts Oct 16; reported Oct 21) |
| **Sector / country** | Banking · India |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Partially confirmed |
| **Attacker** | 'Siriusim' (claimed) |

## What happened
SBI investigated suspected customer-data exposure after alerts from threat intelligence, the Defence Cyber Agency and CERT-In.

## Impact
A 375,000-record dark-web dataset was reviewed; SBI identified 3,897 customer records with PII (name, mobile, DOB, email, address, customer ID, loan details). Core operations unaffected.

## Why it happened (root cause)
Not disclosed; may involve a subsidiary or vendor.

## How it could have been prevented
- Monitor the dark web for your own data, which is how this was caught.
- Apply data-loss prevention to loan-processing and partner channels.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
