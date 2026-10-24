# BigCommerce merchants (via Ribon apps)

| | |
|---|---|
| **Date** | 2026-09-22 (access Sep 13-17; reported Sep 22) |
| **Sector / country** | E-commerce · Global |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Attackers used compromised credentials for the third-party Ribon / Ribon 1.5 apps to read shopper data and inject scripts into merchant stores.

## Impact
Shopper names, emails, phone numbers, shipping addresses. Malicious scripts were injected into some storefronts. Passwords and payment cards were not affected.

## Why it happened (root cause)
An over-privileged third-party app was compromised, and storefronts had no protection against script injection.

## How it could have been prevented
- Review and minimise the permissions of marketplace apps, and remove unused ones.
- Use Content-Security-Policy and Subresource Integrity, and monitor payment-page scripts (PCI DSS 4.0 requirements 6.4.3 and 11.6.1).
- Platforms: rotate app credentials and alert on bulk reads by an app.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
