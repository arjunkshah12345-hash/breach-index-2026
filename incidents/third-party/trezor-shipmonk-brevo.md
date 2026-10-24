# Trezor (via ShipMonk and via Brevo); BitBox; CoinTracking

| | |
|---|---|
| **Date** | 2026-09-10 (ShipMonk Sep 5; Brevo Sep 10) |
| **Sector / country** | Crypto hardware / fintech · Global |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Two separate vendor compromises: a fulfilment partner (ShipMonk) still held old records that should have been deleted, and the email-marketing platform (Brevo) had customer accounts taken over and used to send phishing.

## Impact
ShipMonk exposed about 67,000 more US Trezor customers (names, emails, phones, addresses, orders). In a separate incident, 138 Brevo email-marketing accounts were breached, contacts were exported from 43, and phishing emails seeking wallet seed phrases went out through legitimate crypto mailing lists.

## Why it happened (root cause)
Vendor data retention failure (ShipMonk), and compromised marketing-platform accounts that could send as trusted brands (Brevo).

## How it could have been prevented
- Contracts should require deletion of shipping data after fulfilment, with verified deletion.
- Turn on MFA and IP-restricted API keys for email service provider accounts, and alert on contact exports.
- Tell crypto customers repeatedly that you will never ask for a seed phrase.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
