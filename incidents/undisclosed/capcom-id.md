# Capcom (CAPCOM ID)

| | |
|---|---|
| **Date** | 2026-10-19 (detected Oct 19; disclosed Oct 22) |
| **Sector / country** | Video games · Japan / Global |
| **Attack type** | [Vector not yet disclosed (ransomware, intrusion, data theft)](../../PREVENTION-PLAYBOOK.md#undisclosed) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
A third party accessed CAPCOM ID customer data. Games were unaffected.

## Impact
11,774,247 CAPCOM ID records (emails, plus per some reports usernames, last-login time, login count and IP). Fuller data on 43 accounts. Attackers changed passwords on 196 accounts, which were then reset. No card data.

## Why it happened (root cause)
Not disclosed. The attackers were able to change account passwords, which suggests access to account-management functions, not just a read-only data copy.

## How it could have been prevented
- Notify users and require re-verification on every password or email change.
- Offer MFA and passkeys on game accounts.
- Restrict and log admin or API paths that can change credentials.
- Users: expect Capcom-themed phishing emails.

### Baseline controls for this attack type
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

## Sources
- [Capcom: Notice regarding customer information affected through unauthorized access](https://www.capcom.co.jp/ir/english/news/html/e261022.html)
- [Help Net Security: Capcom data breach exposes 11.7M account records](https://www.helpnetsecurity.com/2026/10/23/capcom-id-data-breach-11-million-records-exposed/)
- [SecurityWeek: 11 million impacted by Capcom data breach](https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
