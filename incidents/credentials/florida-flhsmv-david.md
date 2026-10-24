# Florida Highway Safety & Motor Vehicles (DAVID database)

| | |
|---|---|
| **Date** | 2026-09-12 (claimed Sep 8, confirmed Sep 12) |
| **Sector / country** | Government · US |
| **Attack type** | [Stolen or reused credentials](../../PREVENTION-PLAYBOOK.md#credentials) |
| **Status** | Confirmed |
| **Attacker** | ShinyHunters |

## What happened
Attackers logged into the DAVID driver and motor-vehicle database with a Plant City police officer's credentials.

## Impact
ShinyHunters claimed 200,000+ driver records. FLHSMV confirmed the breach but did not state its scope.

## Why it happened (root cause)
Law-enforcement credentials were stored improperly on a personal device, and the database accepted them without device or MFA checks strong enough to stop reuse.

## How it could have been prevented
- Phishing-resistant MFA and managed-device (conditional access) checks on any law-enforcement data system.
- Per-user query-volume limits and alerts; a single officer pulling bulk records is anomalous.
- Ban credential storage on personal devices, and enforce it with technical controls, not only policy.

### Baseline controls for this attack type
- Phishing-resistant MFA (FIDO2/passkeys) on every externally reachable login, including SFTP, VPN, admin panels, CI/CD and cloud consoles. No password-only exceptions for 'legacy' systems.
- Rotate every credential after any prior incident, and monitor infostealer/breach feeds for your domains and vendors.
- Replace long-lived static secrets with short-lived tokens (OIDC workload identity, SSO-issued sessions).
- Alert on impossible travel, new devices, and unusual data volume per account. Most of these intrusions ran for weeks.
- Least privilege and data minimisation: an account that can read everything turns one stolen login into a mass breach.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
