# Bitget

| | |
|---|---|
| **Date** | 2026-09-24 (first access Aug 31; theft Sep 24) |
| **Sector / country** | Crypto exchange · Global |
| **Attack type** | [Unpatched or zero-day flaw in internet-facing software](../../PREVENTION-PLAYBOOK.md#unpatched) |
| **Status** | Confirmed |
| **Attacker** | Not confirmed (one outlet says North Korea) |

## What happened
Attackers used zero-days in two third-party security appliances, planted a web shell, moved laterally to the production wallet job server, obtained high-privilege internal credentials, and issued fraudulent withdrawals. First they sent small test transfers that stayed under the risk-control threshold.

## Impact
About $387.5M drained from hot and warm wallets. Cold wallets and user balances were covered by the protection fund.

## Why it happened (root cause)
Security appliances had network reach into the wallet infrastructure. Withdrawal authority sat on a server that could be commanded once compromised, and risk checks only looked at single transactions.

## How it could have been prevented
- Isolate security appliances; they should have no route to production wallet systems.
- Require multi-party HSM or MPC signing with policy enforced outside the hot server (velocity limits, allow-lists, human approval above thresholds).
- Risk controls should flag patterns (new destinations, cumulative volume, test-then-drain), not only single transfers.
- Watch appliances for web shells and unexpected outbound C2 traffic.

### Baseline controls for this attack type
- Keep an external attack-surface inventory and patch known-exploited bugs (CISA KEV) within days, not quarters.
- Treat vendor 'temporary mitigations' (WAF rules, config workarounds) as stopgaps. Several 2026 breaches came from bypassing them.
- Keep management interfaces of VPNs, firewalls and appliances off the internet. Put them on an isolated management network.
- Assume an edge device will be popped: segment it from crown-jewel systems and monitor it for new web shells and outbound connections.
- Sandbox risky processing (file uploads, image parsing) and run it with minimal privileges.

## Sources
- [The Hacker News: Bitget confirms third-party zero-day](https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html)
- [BleepingComputer: Bitget hacked via zero-day in third-party security products](https://bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products)
- [The Block: Bitget attacker tested risk controls with small transfers](https://www.theblock.co/news/regulation/2026-09-28-bitget-attacker-tested-risk-controls-small-transfers-388-million-theft-ceo-says-417045)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
