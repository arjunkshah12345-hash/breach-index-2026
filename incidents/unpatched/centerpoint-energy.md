# CenterPoint Energy

| | |
|---|---|
| **Date** | 2026-09-16 (reported Sep 16) |
| **Sector / country** | Utilities · US |
| **Attack type** | [Unpatched or zero-day flaw in internet-facing software](../../PREVENTION-PLAYBOOK.md#unpatched) |
| **Status** | Partially confirmed |
| **Attacker** | Actor using a hex-encoded handle |

## What happened
The attacker claimed to have pulled data through an external-facing API.

## Impact
About 7.49M records claimed: names, SSNs, phone numbers, addresses, account and billing data for some customers. CenterPoint confirmed unauthorized access. Electricity and gas were unaffected.

## Why it happened (root cause)
An external API exposed bulk customer data, most likely through broken object-level authorization or weak API authentication (exact flaw not disclosed).

## How it could have been prevented
- Keep an inventory of every external API, and test for broken object-level authorization (OWASP API #1).
- Rate-limit and alert on bulk enumeration; 7M records should never leave through a customer API.
- Never return SSNs from customer-facing APIs; mask them server-side.

### Baseline controls for this attack type
- Keep an external attack-surface inventory and patch known-exploited bugs (CISA KEV) within days, not quarters.
- Treat vendor 'temporary mitigations' (WAF rules, config workarounds) as stopgaps. Several 2026 breaches came from bypassing them.
- Keep management interfaces of VPNs, firewalls and appliances off the internet. Put them on an isolated management network.
- Assume an edge device will be popped: segment it from crown-jewel systems and monitor it for new web shells and outbound connections.
- Sandbox risky processing (file uploads, image parsing) and run it with minimal privileges.

## Sources
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
