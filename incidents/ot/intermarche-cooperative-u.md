# Intermarché and Coopérative U (refrigeration systems)

| | |
|---|---|
| **Date** | 2026-10-12 (night of Oct 11-12) |
| **Sector / country** | Grocery retail · France |
| **Attack type** | [Operational technology and physical systems](../../PREVENTION-PLAYBOOK.md#ot) |
| **Status** | Confirmed |
| **Attacker** | Unknown (Paris prosecutor / OFAC investigating) |

## What happened
Attackers remotely forced refrigeration units into defrost across hundreds of stores overnight. One report says Danfoss refrigeration controls were targeted (unconfirmed).

## Impact
150-200 Intermarché stores and fewer than 100 Coopérative U stores had to throw away all fresh and frozen products. No data theft reported. Insurers may not cover the losses.

## Why it happened (root cause)
Refrigeration controllers or their remote-management platform were reachable and controllable from outside. Exact path not disclosed.

## How it could have been prevented
- Never expose refrigeration or building-management controllers to the internet; use a brokered, MFA-protected vendor access path.
- Change default credentials and patch controller firmware.
- Set hard local temperature limits and alarms that a remote 'defrost' command can't override for hours.
- Run overnight alerting to on-call staff for mass setpoint or mode changes.

### Baseline controls for this attack type
- Never expose OT controllers or vendor remote-management portals directly to the internet.
- Route vendor remote access through a brokered, MFA-protected, logged path that is only enabled when needed.
- Change default credentials and patch controller firmware.
- Enforce safe limits locally (hard setpoint bounds, interlocks), so a remote command can't push equipment out of a safe range.
- Alert on setpoint or mode changes outside maintenance windows, and practise manual fallback.

## Sources
- [Sud Radio (AFP): Supermarkets hit by cyberattack on refrigeration systems](https://www.sudradio.fr/societe/des-supermarches-victimes-dune-cyberattaque-visant-leurs-installations-frigorifiques-confirment-cooperative-u-et-intermarche)
- [Paris Match: Supermarkets forced to throw away fresh and frozen goods](https://www.parismatch.be/actualites/monde/2026/10/12/inedit-et-dune-extreme-gravite-de-nombreux-supermarches-contraints-de-jeter-une-grande-quantite-de-produits-frais-et-surgeles-en-france-2K5XHP7LYFB6PCUIU56YP65GQA/)
- [SharkStriker: Top data breaches of October 2026](https://sharkstriker.com/blog/october-2026-data-breaches/)

_Compiled 2026-10-24. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
