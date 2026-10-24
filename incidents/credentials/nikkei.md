# Nikkei

| | |
|---|---|
| **Date** | 2026-10-07 (unauthorized access Oct 7) |
| **Sector / country** | Media · Japan |
| **Attack type** | [Stolen or reused credentials](../../PREVENTION-PLAYBOOK.md#credentials) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Attackers got into a cloud service Nikkei used for system development.

## Impact
About 1.83M records accessed: about 150,000 with personal information, about 120,000 with email addresses. No card data. No misuse found as of Oct 16.

## Why it happened (root cause)
Previously compromised credentials were still valid, and the development environment held real personal data.

## How it could have been prevented
- Rotate all credentials after any prior compromise, including those for dev and test tooling.
- Use masked or synthetic data in development environments, not production personal data.
- Require SSO and MFA on developer SaaS, and watch infostealer feeds for employee credentials.

### Baseline controls for this attack type
- Phishing-resistant MFA (FIDO2/passkeys) on every externally reachable login, including SFTP, VPN, admin panels, CI/CD and cloud consoles. No password-only exceptions for 'legacy' systems.
- Rotate every credential after any prior incident, and monitor infostealer/breach feeds for your domains and vendors.
- Replace long-lived static secrets with short-lived tokens (OIDC workload identity, SSO-issued sessions).
- Alert on impossible travel, new devices, and unusual data volume per account. Most of these intrusions ran for weeks.
- Least privilege and data minimisation: an account that can read everything turns one stolen login into a mass breach.

## Sources
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
