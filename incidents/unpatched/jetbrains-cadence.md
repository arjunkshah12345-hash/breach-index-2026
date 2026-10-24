# JetBrains (Cadence environment)

| | |
|---|---|
| **Date** | 2026-09-05 (reported Sep 5) |
| **Sector / country** | Software · Global |
| **Attack type** | [Unpatched or zero-day flaw in internet-facing software](../../PREVENTION-PLAYBOOK.md#unpatched) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Attackers exploited an unpatched critical TeamCity vulnerability to reach the Cadence environment.

## Impact
Possible exposure of AWS credentials, secrets and backups. Users were told to rotate credentials.

## Why it happened (root cause)
An unpatched CI/CD server. TeamCity auth-bypass bugs (for example CVE-2026-63077) are also being used by ransomware gangs.

## How it could have been prevented
- Treat CI/CD as crown jewels: patch fast, never expose it publicly, and require SSO and MFA.
- Keep cloud credentials out of CI; use OIDC federation for short-lived tokens.

### Baseline controls for this attack type
- Keep an external attack-surface inventory and patch known-exploited bugs (CISA KEV) within days, not quarters.
- Treat vendor 'temporary mitigations' (WAF rules, config workarounds) as stopgaps. Several 2026 breaches came from bypassing them.
- Keep management interfaces of VPNs, firewalls and appliances off the internet. Put them on an isolated management network.
- Assume an edge device will be popped: segment it from crown-jewel systems and monitor it for new web shells and outbound connections.
- Sandbox risky processing (file uploads, image parsing) and run it with minimal privileges.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
