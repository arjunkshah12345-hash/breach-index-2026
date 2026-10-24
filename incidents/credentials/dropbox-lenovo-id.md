# Dropbox users (via Lenovo ID email-verification flaw)

| | |
|---|---|
| **Date** | 2026-09-02 (reported Sep 2) |
| **Sector / country** | Cloud storage · Global |
| **Attack type** | [Stolen or reused credentials](../../PREVENTION-PLAYBOOK.md#credentials) |
| **Status** | Reported (secondary sources) |
| **Attacker** | Unknown |

## What happened
Attackers abused a Lenovo email-verification flaw to create Lenovo IDs claiming victims' email addresses, then signed into the matching Dropbox accounts via federated login.

## Impact
About 5,000 Dropbox accounts accessed without passwords; some files viewed and downloaded.

## Why it happened (root cause)
An identity-federation logic flaw: a relying party trusted an email claim from an identity provider that had not actually verified the email.

## How it could have been prevented
- Relying parties should link federated accounts on the IdP's immutable subject ID, never on email alone, and require email_verified.
- Require step-up re-authentication before linking a new federated login to an existing account.
- IdPs must verify email ownership before asserting it.

### Baseline controls for this attack type
- Phishing-resistant MFA (FIDO2/passkeys) on every externally reachable login, including SFTP, VPN, admin panels, CI/CD and cloud consoles. No password-only exceptions for 'legacy' systems.
- Rotate every credential after any prior incident, and monitor infostealer/breach feeds for your domains and vendors.
- Replace long-lived static secrets with short-lived tokens (OIDC workload identity, SSO-issued sessions).
- Alert on impossible travel, new devices, and unusual data volume per account. Most of these intrusions ran for weeks.
- Least privilege and data minimisation: an account that can read everything turns one stolen login into a mass breach.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
