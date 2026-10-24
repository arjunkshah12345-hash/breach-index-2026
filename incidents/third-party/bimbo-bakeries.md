# Bimbo Bakeries USA

| | |
|---|---|
| **Date** | 2026-09-06 (reported Sep 6) |
| **Sector / country** | Food manufacturing · US |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Clop |

## What happened
Clop exploited an Oracle E-Business Suite zero-day through a third-party vendor's environment.

## Impact
Employee data stolen, including names and SSNs. Total not disclosed.

## Why it happened (root cause)
A zero-day in Oracle EBS, reached through a vendor.

## How it could have been prevented
- Don't expose ERP systems (Oracle EBS, PeopleSoft) to the internet; require VPN or zero-trust access.
- Patch Oracle CPU releases promptly, and know which vendors run ERP on your behalf.
- Encrypt or tokenise SSNs at the field level in HR systems.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
