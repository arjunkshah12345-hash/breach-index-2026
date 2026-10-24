# FBI (FBIJobs.gov / applicant portal)

| | |
|---|---|
| **Date** | 2026-09-22 (claimed Sep 22) |
| **Sector / country** | Government · US |
| **Attack type** | [Unpatched or zero-day flaw in internet-facing software](../../PREVENTION-PLAYBOOK.md#unpatched) |
| **Status** | Claimed (unverified) |
| **Attacker** | ShinyHunters |

## What happened
ShinyHunters says it exploited Oracle PeopleSoft and then pivoted into FBI-managed AWS GovCloud.

## Impact
ShinyHunters claims 2-3 TB on current and former employees and applicants. A 5,000-record sample was partly matched by Reuters. The FBI confirmed only that it is investigating activity affecting FBIJobs.gov; the job portals were taken offline.

## Why it happened (root cause)
Linked to CVE-2026-35273 (unauthenticated RCE in PeopleSoft PeopleTools, patched by Oracle in June). Mandiant and Vectra describe a one-character substitution that slipped past the recommended WAF workaround.

## How it could have been prevented
- Apply the vendor patch; don't rely on WAF rules as the long-term fix.
- Keep HR and applicant systems off the open internet where possible, and segment them from cloud admin roles.
- Use least-privilege cloud roles, so a compromised app server can't pivot across the cloud account.

### Baseline controls for this attack type
- Keep an external attack-surface inventory and patch known-exploited bugs (CISA KEV) within days, not quarters.
- Treat vendor 'temporary mitigations' (WAF rules, config workarounds) as stopgaps. Several 2026 breaches came from bypassing them.
- Keep management interfaces of VPNs, firewalls and appliances off the internet. Put them on an isolated management network.
- Assume an edge device will be popped: segment it from crown-jewel systems and monitor it for new web shells and outbound connections.
- Sandbox risky processing (file uploads, image parsing) and run it with minimal privileges.

## Sources
- [BleepingComputer: ShinyHunters claims FBI hack via PeopleSoft](https://bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach)
- [Help Net Security: FBI job portals remain offline](https://www.helpnetsecurity.com/2026/09/28/fbi-job-portals-offline-shinyhunters-breach/)
- [Vectra: ShinyHunters breached the FBI by bypassing the fix](https://www.vectra.ai/blog/shinyhunters-breached-the-fbi-by-bypassing-the-fix)
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
