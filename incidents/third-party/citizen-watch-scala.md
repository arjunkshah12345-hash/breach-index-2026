# Citizen Watch (via Scala Communications)

| | |
|---|---|
| **Date** | 2026-10-05 (reported Oct 5-6) |
| **Sector / country** | Manufacturing / IT vendor · Japan |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Attackers accessed the FAQ and inquiry-management system Scala Communications runs for client companies.

## Impact
Scala: up to 713,126 customer-inquiry records across 5+ client companies. Citizen: about 100,000 customers, including names, addresses, phone numbers, emails, and bank and credit-card information.

## Why it happened (root cause)
An outsourced customer-support system held sensitive financial data and was compromised (vector not disclosed).

## How it could have been prevented
- Never let payment or bank details sit in support-ticket or FAQ systems; redact them on intake.
- Purge support-inquiry data on a retention schedule.
- Assess vendor security for any outsourced system that holds customer PII.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
