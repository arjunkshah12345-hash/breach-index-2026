# Daiichi Kosho (via Nippon Columbia)

| | |
|---|---|
| **Date** | 2026-10-01 (October 2026) |
| **Sector / country** | Entertainment · Japan |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Daiichi Kosho's supplier, Nippon Columbia Group, was hit by a cyberattack that exposed Daiichi Kosho customer data.

## Impact
About 8.72M customers: names, gender, DOB, emails, phone numbers.

## Why it happened (root cause)
Supplier compromise (vector not disclosed).

## How it could have been prevented
- Limit and expire the customer data shared with group companies and suppliers.
- Include suppliers in your security monitoring and incident-response plans.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
