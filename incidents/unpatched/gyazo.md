# Gyazo

| | |
|---|---|
| **Date** | 2026-09-18 (reported Sep 18) |
| **Sector / country** | Consumer software · Japan / Global |
| **Attack type** | [Unpatched or zero-day flaw in internet-facing software](../../PREVENTION-PLAYBOOK.md#unpatched) |
| **Status** | Confirmed |
| **Attacker** | Unknown |

## What happened
Attackers exploited a flaw in the image-upload server to execute commands.

## Impact
About 23.62M user records plus metadata from about 490M images: password hashes, session IDs, IPs, and EXIF location data.

## Why it happened (root cause)
Command execution in the upload-processing path, with access to the user database from that server.

## How it could have been prevented
- Process uploads in a sandboxed, unprivileged worker with no database credentials.
- Strip EXIF and location data at upload time and don't keep it.
- Hash passwords with a modern KDF (Argon2id or bcrypt), and invalidate sessions after a breach.

### Baseline controls for this attack type
- Keep an external attack-surface inventory and patch known-exploited bugs (CISA KEV) within days, not quarters.
- Treat vendor 'temporary mitigations' (WAF rules, config workarounds) as stopgaps. Several 2026 breaches came from bypassing them.
- Keep management interfaces of VPNs, firewalls and appliances off the internet. Put them on an isolated management network.
- Assume an edge device will be popped: segment it from crown-jewel systems and monitor it for new web shells and outbound connections.
- Sandbox risky processing (file uploads, image parsing) and run it with minimal privileges.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
