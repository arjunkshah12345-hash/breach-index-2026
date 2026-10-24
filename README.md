# Company Hacks: September to October 2026

A directory of organisations hacked or breached between **1 Sep and 2026-10-24**. Each entry says why it happened and how it could have been prevented.

- **65 incident files** in [`incidents/`](incidents/), grouped by how attackers got in
- **7 multi-victim campaigns** in [CAMPAIGNS.md](CAMPAIGNS.md)
- **32 unverified ransomware leak-site claims** in [LEAK-SITE-CLAIMS.md](LEAK-SITE-CLAIMS.md)
- **Cross-cutting fixes** in [PREVENTION-PLAYBOOK.md](PREVENTION-PLAYBOOK.md)
- **Website:** https://breach-index-2026.vercel.app (source: [`site/index.html`](site/index.html), a single self-contained file with no dependencies)
- Machine-readable data in [`data/incidents.json`](data/incidents.json) and [`data/incidents.csv`](data/incidents.csv). Run `python3 build.py` to regenerate everything.

> This isn't literally every company. Ransomware trackers log roughly 700-800 victims a month (BlackFog counted 789 in September 2026 across 79 groups). This directory covers the notable, publicly reported cases, plus a list of leak-site claims.

## The short version: why companies are getting hacked right now

1. **Logins, not exploits.** Stolen, reused or never-rotated credentials (ETS, Nikkei, Florida DAVID, Veradigm), plus vishing of help desks (ShinyHunters, PREY-0058). Fix: phishing-resistant MFA everywhere, with no exceptions.
2. **Through someone else.** Cloud hosts (IDCF took down 495 organisations at once), support vendors (Scala to Citizen), fulfilment and email providers (ShipMonk, Brevo), plugins and CLIs (UpdraftPlus, OVHcloud), and PaaS secret stores (Railway). Fix: least data shared, scoped and revocable integration keys, and your own backups.
3. **Edge boxes and enterprise apps.** Zero-days in VPNs, security appliances, PeopleSoft, EBS and TeamCity (Bitget lost $387.5M after two security appliances were popped). Fix: patch known-exploited bugs in days, keep management interfaces off the internet, and segment.
4. **AI is speeding up attackers.** One operator with AI agents breached 100+ companies for about $5k. Storm-0940 used an agentic pentest tool against 2,250+ M365 tenants. Fix: assume constant, cheap probing, and shrink your attack surface.
5. **Physical consequences.** Refrigeration controllers at hundreds of French supermarkets were forced into defrost overnight. Fix: OT never on the open internet, with local safety limits.

Of the 65 incidents, 28 have a publicly known entry vector; the other 37 haven't been disclosed yet.

## By attack type
| Attack type | Incidents |
|---|---|
| [Stolen or reused credentials](PREVENTION-PLAYBOOK.md#credentials) | 5 |
| [Third-party vendor and supply-chain compromise](PREVENTION-PLAYBOOK.md#third-party) | 12 |
| [Unpatched or zero-day flaw in internet-facing software](PREVENTION-PLAYBOOK.md#unpatched) | 7 |
| [Social engineering (vishing, help-desk impersonation, fraudulent requests)](PREVENTION-PLAYBOOK.md#social-engineering) | 1 |
| [Exposed services, misconfiguration and internal error](PREVENTION-PLAYBOOK.md#exposure) | 2 |
| [Operational technology and physical systems](PREVENTION-PLAYBOOK.md#ot) | 1 |
| [Vector not yet disclosed (ransomware, intrusion, data theft)](PREVENTION-PLAYBOOK.md#undisclosed) | 37 |

## All incidents (newest first)
| Date | Organisation | Sector | Attack type | Status |
|---|---|---|---|---|
| 2026-10-23 | [Aryza](incidents/undisclosed/aryza.md) | Fintech software | Vector not yet disclosed (ransomware, intrusion, data theft) | Claimed (unverified) |
| 2026-10-21 | [Railway](incidents/third-party/railway.md) | Developer platform (PaaS) | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-21 | [Quest Diagnostics (Quanum Lab Services Manager)](incidents/undisclosed/quest-diagnostics.md) | Healthcare | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-19 | [Educational Testing Service (ETS) / California Dept. of Education](incidents/credentials/ets-california-students.md) | Education | Stolen or reused credentials | Confirmed |
| 2026-10-19 | [OVHcloud CLI](incidents/third-party/ovhcloud-cli.md) | Cloud / developer tooling | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-19 | [Capcom (CAPCOM ID)](incidents/undisclosed/capcom-id.md) | Video games | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-18 | [UpdraftPlus / TeamUpdraft (WordPress)](incidents/third-party/updraftplus.md) | Software (WordPress plugins) | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-16 | [State Bank of India (SBI)](incidents/undisclosed/sbi.md) | Banking | Vector not yet disclosed (ransomware, intrusion, data theft) | Partially confirmed |
| 2026-10-15 | [Ampath Laboratories](incidents/undisclosed/ampath-laboratories.md) | Healthcare (pathology) | Vector not yet disclosed (ransomware, intrusion, data theft) | Claimed (unverified) |
| 2026-10-14 | [Zeabur](incidents/undisclosed/zeabur.md) | Cloud deployment platform | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-12 | [Intermarché and Coopérative U (refrigeration systems)](incidents/ot/intermarche-cooperative-u.md) | Grocery retail | Operational technology and physical systems | Confirmed |
| 2026-10-12 | [Ahold Delhaize (Food Lion, Giant Food, The GIANT Company, Stop & Shop, Hannaford, and others)](incidents/undisclosed/ahold-delhaize.md) | Grocery retail | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-10 | [GMO Internet (Onamae.com Desktop Cloud)](incidents/undisclosed/gmo-onamae-desktop-cloud.md) | Hosting | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-10 | [Denmark Central Population Registry (CPR) and Technical University of Denmark (DTU)](incidents/undisclosed/denmark-cpr-dtu.md) | Government / Education | Vector not yet disclosed (ransomware, intrusion, data theft) | Reported (secondary sources) |
| 2026-10-10 | [US municipalities: Heber City UT, Vicksburg MS, Radford VA, Everett MA; Springfield (MA) Public Schools](incidents/undisclosed/us-municipalities.md) | Local government / Education | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-08 | [University of Illinois Chicago (College of Medicine)](incidents/undisclosed/uic-college-of-medicine.md) | Education / Healthcare | Vector not yet disclosed (ransomware, intrusion, data theft) | Partially confirmed |
| 2026-10-08 | [ASOS](incidents/undisclosed/asos.md) | Retail (fashion) | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-08 | [Georgia Power](incidents/undisclosed/georgia-power.md) | Utilities | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-08 | [UK fashion retail: The Foschini Group (Hobbs, Whistles) and Phase Eight](incidents/undisclosed/uk-fashion-retail.md) | Retail (fashion) | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-08 | [Senture (US Department of Transportation contractor)](incidents/undisclosed/senture-dot.md) | BPO / Government contractor | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-08 | [Icon Oncology](incidents/undisclosed/icon-oncology.md) | Healthcare | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-07 | [Nikkei](incidents/credentials/nikkei.md) | Media | Stolen or reused credentials | Confirmed |
| 2026-10-07 | [IDC Frontier (IDCF Cloud, SoftBank)](incidents/third-party/idc-frontier-idcf-cloud.md) | Cloud / data centre | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-07 | [East Japan Railway (JR East) / View Card](incidents/third-party/jr-east-view-card.md) | Transport | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-07 | [Nissui](incidents/third-party/nissui.md) | Food processing | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-06 | [Mr.Max Holdings](incidents/undisclosed/mr-max.md) | Retail | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-05 | [Citizen Watch (via Scala Communications)](incidents/third-party/citizen-watch-scala.md) | Manufacturing / IT vendor | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-05 | [Daiwa Securities Group](incidents/third-party/daiwa-securities.md) | Finance | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-05 | [Yakiniku King (Monogatari Corp.)](incidents/undisclosed/yakiniku-king-monogatari.md) | Restaurants | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-04 | [Nueva EPS](incidents/undisclosed/nueva-eps.md) | Health insurance | Vector not yet disclosed (ransomware, intrusion, data theft) | Claimed (unverified) |
| 2026-10-01 | [Daiichi Kosho (via Nippon Columbia)](incidents/third-party/daiichi-kosho.md) | Entertainment | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-10-01 | [Frontline Education](incidents/unpatched/frontline-education.md) | EdTech | Unpatched or zero-day flaw in internet-facing software | Confirmed |
| 2026-10-01 | [Skyticket (Adventure Inc.)](incidents/undisclosed/skyticket-adventure.md) | Travel | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-01 | [GMO Research & AI](incidents/undisclosed/gmo-research.md) | Market research | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-10-01 | [MetaMask (Consensys)](incidents/undisclosed/metamask.md) | Crypto wallet | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-30 | [Bee Cheng Hiang](incidents/exposure/bee-cheng-hiang.md) | Retail (food) | Exposed services, misconfiguration and internal error | Confirmed |
| 2026-09-30 | [US Department of Defense (Defense Manpower Data Center)](incidents/undisclosed/dod-dmdc.md) | Government | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-30 | [Times Car Rental](incidents/undisclosed/times-car-rental.md) | Car rental | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-26 | [Keio Corporation](incidents/undisclosed/keio.md) | Transport / hospitality | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-25 | [Dyfed-Powys Police](incidents/undisclosed/dyfed-powys-police.md) | Law enforcement | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-24 | [Bitget](incidents/unpatched/bitget.md) | Crypto exchange | Unpatched or zero-day flaw in internet-facing software | Confirmed |
| 2026-09-24 | [Astrana Health](incidents/undisclosed/astrana.md) | Healthcare | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-22 | [BigCommerce merchants (via Ribon apps)](incidents/third-party/bigcommerce-ribon.md) | E-commerce | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-09-22 | [FBI (FBIJobs.gov / applicant portal)](incidents/unpatched/fbi-peoplesoft.md) | Government | Unpatched or zero-day flaw in internet-facing software | Claimed (unverified) |
| 2026-09-21 | [Ludwig Maximilian University of Munich (LMU)](incidents/undisclosed/lmu-munich.md) | Education | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-18 | [Gyazo](incidents/unpatched/gyazo.md) | Consumer software | Unpatched or zero-day flaw in internet-facing software | Confirmed |
| 2026-09-16 | [CenterPoint Energy](incidents/unpatched/centerpoint-energy.md) | Utilities | Unpatched or zero-day flaw in internet-facing software | Partially confirmed |
| 2026-09-14 | [Japan Digital Agency (Government Solution Service)](incidents/unpatched/japan-digital-agency.md) | Government | Unpatched or zero-day flaw in internet-facing software | Confirmed |
| 2026-09-12 | [Florida Highway Safety & Motor Vehicles (DAVID database)](incidents/credentials/florida-flhsmv-david.md) | Government | Stolen or reused credentials | Confirmed |
| 2026-09-12 | [Revolut](incidents/social-engineering/revolut.md) | Fintech | Social engineering (vishing, help-desk impersonation, fraudulent requests) | Confirmed |
| 2026-09-10 | [Trezor (via ShipMonk and via Brevo); BitBox; CoinTracking](incidents/third-party/trezor-shipmonk-brevo.md) | Crypto hardware / fintech | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-09-10 | [AdaptHealth](incidents/undisclosed/adapthealth.md) | Healthcare | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-10 | [IDScan](incidents/undisclosed/idscan.md) | Identity verification | Vector not yet disclosed (ransomware, intrusion, data theft) | Reported (secondary sources) |
| 2026-09-10 | [Weverse (HYBE)](incidents/undisclosed/weverse.md) | Entertainment | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-09 | [Veradigm](incidents/credentials/veradigm.md) | Healthcare IT | Stolen or reused credentials | Confirmed |
| 2026-09-08 | [Vietnam APIS airline passenger database](incidents/exposure/vietnam-apis-database.md) | Aviation / Government | Exposed services, misconfiguration and internal error | Reported (secondary sources) |
| 2026-09-08 | [Stadtwerke Landsberg](incidents/undisclosed/stadtwerke-landsberg.md) | Utilities | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-07 | [Condé Nast](incidents/undisclosed/conde-nast.md) | Media | Vector not yet disclosed (ransomware, intrusion, data theft) | Claimed (unverified) |
| 2026-09-07 | [Mathspace](incidents/undisclosed/mathspace.md) | EdTech | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-06 | [Bimbo Bakeries USA](incidents/third-party/bimbo-bakeries.md) | Food manufacturing | Third-party vendor and supply-chain compromise | Confirmed |
| 2026-09-05 | [JetBrains (Cadence environment)](incidents/unpatched/jetbrains-cadence.md) | Software | Unpatched or zero-day flaw in internet-facing software | Confirmed |
| 2026-09-05 | [Berlin state government (two departments)](incidents/undisclosed/berlin-state-government.md) | Government | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-02 | [Dropbox users (via Lenovo ID email-verification flaw)](incidents/credentials/dropbox-lenovo-id.md) | Cloud storage | Stolen or reused credentials | Reported (secondary sources) |
| 2026-09-01 | [Aesto Health](incidents/undisclosed/aesto-health.md) | Healthcare IT | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |
| 2026-09-01 | [Novocure](incidents/undisclosed/novocure.md) | Medical devices | Vector not yet disclosed (ransomware, intrusion, data theft) | Confirmed |

## Status key
- **Confirmed**: the organisation or an authority acknowledged the incident.
- **Partially confirmed**: the incident was acknowledged, but the scope claimed by attackers is not verified.
- **Claimed (unverified)**: a threat-actor or forum claim only.
- **Reported (secondary sources)**: covered by trackers or press, without a primary statement found.

## Contributing
Found a breach we missed, or a detail that's out of date?

1. Edit the `INCIDENTS` list in [`build.py`](build.py). Every entry needs at least one public source in `SRC`.
2. Run `python3 build.py`. This regenerates the markdown files, the JSON and CSV data, and the website. It uses only the standard library.
3. Open a pull request.

Keep claims honest: use `Claimed (unverified)` for threat-actor posts, and don't guess at root causes the victim hasn't disclosed.

## License
Code is [MIT](LICENSE). Incident write-ups summarise public reporting; follow the linked sources for the originals.

_Compiled 2026-10-24 from public reporting. Sources are listed in every file._
