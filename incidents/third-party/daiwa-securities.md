# Daiwa Securities Group

| | |
|---|---|
| **Date** | 2026-10-05 (reported around Oct 5) |
| **Sector / country** | Finance · Japan |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
An external vendor was breached and Daiwa client data was exposed.

## Impact
More than 110,000 clients' names and account numbers.

## Why it happened (root cause)
Third-party vendor compromise (details not disclosed).

## How it could have been prevented
- Share only the fields a vendor needs, and tokenise account numbers where possible.
- Require vendor breach notification and audit rights.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
