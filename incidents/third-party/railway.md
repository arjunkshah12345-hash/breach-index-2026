# Railway

| | |
|---|---|
| **Date** | 2026-10-21 (disclosed Oct 21) |
| **Sector / country** | Developer platform (PaaS) · US |
| **Attack type** | [Third-party vendor and supply-chain compromise](../../PREVENTION-PLAYBOOK.md#third-party) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Railway detected anomalous activity in the systems that store customer environment variables. It suggested this may be one of a series of attacks on platform companies and AI inference providers (unconfirmed).

## Impact
An unauthorized party may have accessed encrypted customer environment variables and decrypted some of them (API keys, database credentials, registry credentials). Railway told all users to rotate secrets and paused deployments.

## Why it happened (root cause)
Full root cause not yet published. The attacker reached both the stored secrets and the means to decrypt them.

## How it could have been prevented
- Platforms: use envelope encryption with KMS or HSM keys that only the running workload's identity can use to decrypt, so stored secrets plus database access is not enough.
- Customers: prefer short-lived credentials (OIDC federation to AWS/GCP, scoped database users) over static keys in environment variables.
- Customers: set spend limits and alerts on LLM and API keys (OpenAI, Anthropic, OpenRouter, Stripe) to catch abuse fast.

### Baseline controls for this attack type
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

## Sources
- [Railway blog: Security disclosure / preliminary report, Oct 21 incident](https://blog.railway.com/)
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
