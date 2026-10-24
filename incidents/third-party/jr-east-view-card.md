# East Japan Railway (JR East) / View Card

| | |
|---|---|
| **Date** | 2026-10-07 (via IDCF Cloud attack) |
| **Sector / country** | Transport · Japan |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Not disclosed |

## What happened
JR East and its card subsidiary were hit through the ransomware attack on their cloud host, IDC Frontier.

## Impact
Email-delivery data covering about 6.09M accounts may have been compromised.

## Why it happened (root cause)
Concentration risk: customer email-delivery data was hosted with a single cloud provider that was then compromised.

## How it could have been prevented
- Keep only the data a vendor needs for the task (for example, hashed or tokenised identifiers instead of full contact lists where possible).
- Map and tier cloud-provider dependencies, and require isolation and backup guarantees.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [BleepingComputer: Ransomware attack disrupts Japan's IDCF Cloud](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)
- [Cybernews: Cyberattack on Japanese cloud firm hits railways, police, food suppliers](https://cybernews.com/security/japanese-cloud-cyberattack-railways-police-495-organizations-idcf/)
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
