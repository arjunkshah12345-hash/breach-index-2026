# Veradigm

| | |
|---|---|
| **Date** | 2026-09-09 (reported Sep 9) |
| **Sector / country** | Healthcare IT · US |
| **Attack type** | [Stolen or reused credentials](../../PREVENTION-PLAYBOOK.md#credentials) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
An unauthorized party used stolen credentials belonging to a third-party vendor to call a Veradigm API and download patient data.

## Impact
Patient information downloaded from some healthcare customers, including SSNs in some cases. Clinical data not compromised.

## Why it happened (root cause)
A vendor API credential that was long-lived and broadly scoped, with no anomaly detection on bulk pulls.

## How it could have been prevented
- Issue vendor API credentials scoped to the minimum data, IP-restricted, short-lived, and bound with mTLS where possible.
- Rate-limit and alert on bulk record retrieval per client.
- Require vendors to protect the credentials you issue them (secret managers, MFA on their side).

### Baseline controls for this attack type
- Phishing-resistant MFA (FIDO2/passkeys) on every externally reachable login, including SFTP, VPN, admin panels, CI/CD and cloud consoles. No password-only exceptions for 'legacy' systems.
- Rotate every credential after any prior incident, and monitor infostealer/breach feeds for your domains and vendors.
- Replace long-lived static secrets with short-lived tokens (OIDC workload identity, SSO-issued sessions).
- Alert on impossible travel, new devices, and unusual data volume per account. Most of these intrusions ran for weeks.
- Least privilege and data minimisation: an account that can read everything turns one stolen login into a mass breach.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
