# Educational Testing Service (ETS) / California Dept. of Education

| | |
|---|---|
| **Date** | 2026-10-19 (access May 22 to Sep 18; reported Oct 19) |
| **Sector / country** | Education · US |
| **Attack type** | [Stolen or reused credentials](../../PREVENTION-PLAYBOOK.md#credentials) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
An unauthorized party used compromised login credentials to access an SFTP file-transfer site run by ETS, the state's testing contractor, and copied files repeatedly over about four months.

## Impact
Data on millions of current and former California public-school students (anyone enrolled in the last three school years at least; 5.7M+ enrolled in 2025-26 alone): names, Statewide Student IDs, DOB, home address, demographics, disability and program data, test scores. No SSNs or financial data.

## Why it happened (root cause)
Valid credentials on an internet-facing SFTP server, apparently with no second factor. The long dwell time points to no alerting on bulk downloads.

## How it could have been prevented
- Put SFTP behind SSO with phishing-resistant MFA, or use key-based auth with IP allow-listing for named partner systems only.
- Don't leave years of student records sitting on a transfer site. Files should be picked up and then auto-deleted.
- Alert on download volume per account; four months of repeated copying should have tripped something.
- Contracts with state testing vendors should require MFA, logging and retention limits, with audits.

### Baseline controls for this attack type
- Phishing-resistant MFA (FIDO2/passkeys) on every externally reachable login, including SFTP, VPN, admin panels, CI/CD and cloud consoles. No password-only exceptions for 'legacy' systems.
- Rotate every credential after any prior incident, and monitor infostealer/breach feeds for your domains and vendors.
- Replace long-lived static secrets with short-lived tokens (OIDC workload identity, SSO-issued sessions).
- Alert on impossible travel, new devices, and unusual data volume per account. Most of these intrusions ran for weeks.
- Least privilege and data minimisation: an account that can read everything turns one stolen login into a mass breach.

## Sources
- [Malwarebytes: Millions of California students' data stolen](https://www.malwarebytes.com/blog/data-breaches/2026/10/millions-of-california-students-sensitive-data-stolen-in-breach)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
