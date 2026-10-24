# Prevention Playbook

These fixes are grouped by how attackers got in during Sep to Oct 2026. If you only do ten things, do these, in roughly this order of payoff:

1. **Phishing-resistant MFA (passkeys / FIDO2) on everything reachable from the internet.** This includes SFTP, VPN, CI/CD, admin panels, SaaS and vendor portals. It defeats stolen passwords, MFA-fatigue and help-desk vishing, and would have stopped or blunted ETS, Nikkei, Florida DAVID, PREY-0058 and much of ShinyHunters.
2. **Patch known-exploited vulnerabilities in days.** Start with edge devices (VPNs, firewalls, security appliances) and enterprise apps (PeopleSoft, EBS, TeamCity, Windchill). Don't rely on WAF workarounds.
3. **Keep management interfaces and OT off the internet.** This covers appliance admin UIs, refrigeration and building controllers, databases, and self-hosted AI agent platforms.
4. **Segment.** A compromised appliance or web server must not be able to reach wallets, HR data, or the hypervisor (Bitget, IDCF).
5. **Replace static secrets with short-lived ones.** Use OIDC workload identity and scoped, IP-restricted vendor keys, and rotate everything after any incident (Railway, Veradigm, Nikkei, Zeabur).
6. **Inventory third parties and minimise what they hold.** Contracts should require MFA, logs, fast notification and deletion (Scala, ShipMonk, Daiwa, IDCF).
7. **Immutable backups outside your primary provider, with tested restores.** The goal is to survive both ransomware and losing your cloud host.
8. **Exfiltration detection.** Alert on bulk downloads, API enumeration and unusual outbound transfers; several of these breaches ran for months.
9. **Help-desk and legal-request verification.** These processes must not be beatable by a convincing phone call or a real-looking government email (Revolut).
10. **Software supply-chain integrity.** Use immutable, signed releases, verify what you install, and require hardware-key MFA for maintainers (OVHcloud CLI, UpdraftPlus).

<a id="credentials"></a>
## Stolen or reused credentials
**Why it works:** Attackers log in with a valid username/password or key (phished, bought from infostealer logs, reused from an older breach, or never rotated). No exploit needed, so it looks like normal use.

**Prevent it:**
- Phishing-resistant MFA (FIDO2/passkeys) on every externally reachable login, including SFTP, VPN, admin panels, CI/CD and cloud consoles. No password-only exceptions for 'legacy' systems.
- Rotate every credential after any prior incident, and monitor infostealer/breach feeds for your domains and vendors.
- Replace long-lived static secrets with short-lived tokens (OIDC workload identity, SSO-issued sessions).
- Alert on impossible travel, new devices, and unusual data volume per account. Most of these intrusions ran for weeks.
- Least privilege and data minimisation: an account that can read everything turns one stolen login into a mass breach.

**Seen in:** [Educational Testing Service](incidents/credentials/ets-california-students.md), [Nikkei](incidents/credentials/nikkei.md), [Florida Highway Safety & Motor Vehicles](incidents/credentials/florida-flhsmv-david.md), [Veradigm](incidents/credentials/veradigm.md), [Dropbox users](incidents/credentials/dropbox-lenovo-id.md)

<a id="third-party"></a>
## Third-party vendor and supply-chain compromise
**Why it works:** The victim was never breached directly. A vendor, SaaS provider, cloud host, plugin, or software release they trusted was compromised and used as the way in.

**Prevent it:**
- Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.
- Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.
- Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).
- Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.
- Plan for a provider outage: keep independent backups and a tested restore path outside the provider.

**Seen in:** [IDC Frontier](incidents/third-party/idc-frontier-idcf-cloud.md), [East Japan Railway](incidents/third-party/jr-east-view-card.md), [Nissui](incidents/third-party/nissui.md), [Citizen Watch](incidents/third-party/citizen-watch-scala.md), [Daiwa Securities Group](incidents/third-party/daiwa-securities.md), [Daiichi Kosho](incidents/third-party/daiichi-kosho.md), [Trezor](incidents/third-party/trezor-shipmonk-brevo.md), [Bimbo Bakeries USA](incidents/third-party/bimbo-bakeries.md), [BigCommerce merchants](incidents/third-party/bigcommerce-ribon.md), [UpdraftPlus / TeamUpdraft](incidents/third-party/updraftplus.md), [OVHcloud CLI](incidents/third-party/ovhcloud-cli.md), [Railway](incidents/third-party/railway.md)

<a id="unpatched"></a>
## Unpatched or zero-day flaw in internet-facing software
**Why it works:** A vulnerability in an edge device or public app (VPN, firewall, security appliance, ERP, CI server, upload handler, API) gave attackers code execution or data access.

**Prevent it:**
- Keep an external attack-surface inventory and patch known-exploited bugs (CISA KEV) within days, not quarters.
- Treat vendor 'temporary mitigations' (WAF rules, config workarounds) as stopgaps. Several 2026 breaches came from bypassing them.
- Keep management interfaces of VPNs, firewalls and appliances off the internet. Put them on an isolated management network.
- Assume an edge device will be popped: segment it from crown-jewel systems and monitor it for new web shells and outbound connections.
- Sandbox risky processing (file uploads, image parsing) and run it with minimal privileges.

**Seen in:** [Bitget](incidents/unpatched/bitget.md), [FBI](incidents/unpatched/fbi-peoplesoft.md), [Japan Digital Agency](incidents/unpatched/japan-digital-agency.md), [Gyazo](incidents/unpatched/gyazo.md), [CenterPoint Energy](incidents/unpatched/centerpoint-energy.md), [JetBrains](incidents/unpatched/jetbrains-cadence.md), [Frontline Education](incidents/unpatched/frontline-education.md)

<a id="social-engineering"></a>
## Social engineering (vishing, help-desk impersonation, fraudulent requests)
**Why it works:** Attackers talk a human into handing over access: calling the help desk, posing as IT to get an MFA approval, or sending a fake official data request.

**Prevent it:**
- Help-desk identity verification that can't be beaten on a phone call (video and ID check, manager callback, no MFA resets on inbound calls).
- Phishing-resistant MFA, so there is no push to approve and no code to read out.
- Bind sessions to devices and alert on token reuse from new IPs.
- Verify official or legal data requests out of band, using contact details you already hold, never those in the request.
- Run regular vishing drills for executives, finance and IT support.

**Seen in:** [Revolut](incidents/social-engineering/revolut.md)

<a id="exposure"></a>
## Exposed services, misconfiguration and internal error
**Why it works:** Nobody had to break in. A database, AI agent platform, or service was reachable without authentication, or an internal mistake published data.

**Prevent it:**
- Default-deny network exposure. Scan your own IP space and cloud accounts continuously for open databases, storage buckets and admin and AI-agent panels.
- Require authentication on every internal tool, including self-hosted AI agent platforms, even if it is 'just a test'.
- Run cloud posture management (CSPM) with alerts on public resources.
- Code-review and test any automated customer messaging. AI-generated code needs the same review as human-written code.
- Log and rate-limit, so sustained automated probing is visible.

**Seen in:** [Vietnam APIS airline passenger database](incidents/exposure/vietnam-apis-database.md), [Bee Cheng Hiang](incidents/exposure/bee-cheng-hiang.md)

<a id="ot"></a>
## Operational technology and physical systems
**Why it works:** Attackers reached controllers that run physical equipment (refrigeration, building management, industrial systems) and changed how it behaved.

**Prevent it:**
- Never expose OT controllers or vendor remote-management portals directly to the internet.
- Route vendor remote access through a brokered, MFA-protected, logged path that is only enabled when needed.
- Change default credentials and patch controller firmware.
- Enforce safe limits locally (hard setpoint bounds, interlocks), so a remote command can't push equipment out of a safe range.
- Alert on setpoint or mode changes outside maintenance windows, and practise manual fallback.

**Seen in:** [Intermarché and Coopérative U](incidents/ot/intermarche-cooperative-u.md)

<a id="undisclosed"></a>
## Vector not yet disclosed (ransomware, intrusion, data theft)
**Why it works:** The organisation has confirmed or been accused of a breach, but has not said how attackers got in. Across 2026 incidents where the vector did come out, the usual causes were stolen credentials, unpatched edge devices, and third parties.

**Prevent it:**
- The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.
- Immutable, offline or logically separated backups, with restores tested against a realistic scenario.
- Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.
- Data minimisation and retention limits, because data you deleted can't be stolen.
- Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.

**Seen in:** [Quest Diagnostics](incidents/undisclosed/quest-diagnostics.md), [Capcom](incidents/undisclosed/capcom-id.md), [Ahold Delhaize](incidents/undisclosed/ahold-delhaize.md), [Keio Corporation](incidents/undisclosed/keio.md), [State Bank of India](incidents/undisclosed/sbi.md), [Ampath Laboratories](incidents/undisclosed/ampath-laboratories.md), [Skyticket](incidents/undisclosed/skyticket-adventure.md), [Yakiniku King](incidents/undisclosed/yakiniku-king-monogatari.md), [Mr.Max Holdings](incidents/undisclosed/mr-max.md), [GMO Research & AI](incidents/undisclosed/gmo-research.md), [GMO Internet](incidents/undisclosed/gmo-onamae-desktop-cloud.md), [Zeabur](incidents/undisclosed/zeabur.md), [Aesto Health](incidents/undisclosed/aesto-health.md), [AdaptHealth](incidents/undisclosed/adapthealth.md), [US Department of Defense](incidents/undisclosed/dod-dmdc.md), [Times Car Rental](incidents/undisclosed/times-car-rental.md), [Denmark Central Population Registry](incidents/undisclosed/denmark-cpr-dtu.md), [Nueva EPS](incidents/undisclosed/nueva-eps.md), [Condé Nast](incidents/undisclosed/conde-nast.md), [IDScan](incidents/undisclosed/idscan.md), [Weverse](incidents/undisclosed/weverse.md), [Novocure](incidents/undisclosed/novocure.md), [Astrana Health](incidents/undisclosed/astrana.md), [Ludwig Maximilian University of Munich](incidents/undisclosed/lmu-munich.md), [Mathspace](incidents/undisclosed/mathspace.md), [University of Illinois Chicago](incidents/undisclosed/uic-college-of-medicine.md), [ASOS](incidents/undisclosed/asos.md), [Georgia Power](incidents/undisclosed/georgia-power.md), [MetaMask](incidents/undisclosed/metamask.md), [UK fashion retail: The Foschini Group](incidents/undisclosed/uk-fashion-retail.md), [Senture](incidents/undisclosed/senture-dot.md), [Aryza](incidents/undisclosed/aryza.md), [Icon Oncology](incidents/undisclosed/icon-oncology.md), [Stadtwerke Landsberg](incidents/undisclosed/stadtwerke-landsberg.md), [Berlin state government](incidents/undisclosed/berlin-state-government.md), [US municipalities: Heber City UT, Vicksburg MS, Radford VA, Everett MA; Springfield](incidents/undisclosed/us-municipalities.md), [Dyfed-Powys Police](incidents/undisclosed/dyfed-powys-police.md)

