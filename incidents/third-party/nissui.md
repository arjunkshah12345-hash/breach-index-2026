# Nissui

| | |
|---|---|
| **Date** | 2026-10-07 (via IDCF Cloud attack) |
| **Sector / country** | Food processing · Japan |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Not disclosed |

## What happened
Systems hosted in a third-party data centre (IDCF) went down in the ransomware attack.

## Impact
Its logistics subsidiary stopped shipping at all sites, with partial restart on Oct 9.

## Why it happened (root cause)
Business-critical logistics depended on a single hosting provider with no failover.

## How it could have been prevented
- Run business-continuity plans for losing a hosting provider, including manual shipping procedures.
- Keep failover or restore capability in a second environment for order and logistics systems.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [BleepingComputer: Ransomware attack disrupts Japan's IDCF Cloud](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
