# OVHcloud CLI

| | |
|---|---|
| **Date** | 2026-10-19 (94-minute window, 14:47-16:21 UTC+2) |
| **Sector / country** | Cloud / developer tooling · France / Global |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
A compromised developer account was used to swap legitimate release files for malicious ones. Source code and the build chain were not affected.

## Impact
Release binaries for v0.11.0 to v0.15.0 were replaced with malicious files. Anyone who downloaded and ran them during the window should rotate exposed secrets.

## Why it happened (root cause)
A single developer account could overwrite published release artifacts.

## How it could have been prevented
- Make releases immutable once published; nobody should be able to replace a binary after release.
- Sign artifacts and publish provenance (Sigstore / SLSA). Users should verify signatures or pinned checksums.
- Require hardware-key MFA for maintainers, and two-person approval for release changes.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
