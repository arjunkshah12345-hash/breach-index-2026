# IDC Frontier (IDCF Cloud, SoftBank)

| | |
|---|---|
| **Date** | 2026-10-07 (ransomware Oct 7) |
| **Sector / country** | Cloud / data centre · Japan |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Not disclosed |

## What happened
Ransomware took down part of IDCF Cloud. The provider isolated the affected region. It later said no data was taken from customer VMs, which conflicts with some customers' notices.

## Impact
495 companies and local governments affected. Virtual servers in four availability zones stopped and could not restart, and customers were warned they might have to restore from their own backups. Downstream victims include JR East / View Card (about 6.09M records), Nissui logistics, and Ibaraki Prefecture and prefectural police websites.

## Why it happened (root cause)
Entry vector not disclosed. Because it hit many tenants at once, the attackers most likely reached the shared management or virtualisation layer rather than individual tenants.

## How it could have been prevented
- Providers: isolate the hypervisor and management plane on a separate network with phishing-resistant MFA and just-in-time admin access, and keep immutable backups of tenant volumes.
- Customers: keep your own backups outside the provider, and test a restore into a second region or provider.
- Customers: contracts should require breach notice within hours and spell out recovery responsibilities.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [BleepingComputer: Ransomware attack disrupts Japan's IDCF Cloud](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)
- [Cybernews: Cyberattack on Japanese cloud firm hits railways, police, food suppliers](https://cybernews.com/security/japanese-cloud-cyberattack-railways-police-495-organizations-idcf/)
- [Rescana: IDCF Cloud ransomware amid wider Japan attack wave](https://www.rescana.com/post/idcf-cloud-ransomware-japan-attack-wave-october-2026)
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
