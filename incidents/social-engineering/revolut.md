# Revolut

| | |
|---|---|
| **Date** | 2026-09-12 (reported Sep 12) |
| **Sector / country** | Fintech · UK / EU |
| **Attack type** | [Social engineering (vishing, help-desk impersonation, fraudulent requests)](../../PREVENTION-PLAYBOOK.md#social-engineering) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Fraudulent data requests sent from a legitimate government-agency email domain led Revolut to hand over customer data.

## Impact
Customer DOBs, contact details, passport and licence copies, possible selfies, statements and transaction histories. Systems and funds unaffected.

## Why it happened (root cause)
A fake official data request (emergency or law-enforcement style) from a compromised or spoofed real government mailbox was trusted because of the sender domain.

## How it could have been prevented
- Verify every legal or law-enforcement data request out of band, by calling a known number for the agency, and use LE portals where they exist.
- Apply a two-person rule and minimum-necessary disclosure for legal requests.
- Don't treat the sender domain as proof; government mailboxes get compromised.

### Baseline controls for this attack type
- Help-desk identity verification that can't be beaten on a phone call (video and ID check, manager callback, no MFA resets on inbound calls).
- Phishing-resistant MFA, so there is no push to approve and no code to read out.
- Bind sessions to devices and alert on token reuse from new IPs.
- Verify official or legal data requests out of band, using contact details you already hold, never those in the request.
- Run regular vishing drills for executives, finance and IT support.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
