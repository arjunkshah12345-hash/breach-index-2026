#!/usr/bin/env python3
"""Generate the breach directory from the incident data below.

Run:  python3 build.py
Writes README.md, incidents/<category>/<slug>.md, data/incidents.json, data/incidents.csv.
Edit the INCIDENTS list (or CATEGORIES) and re-run to update everything.
"""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AS_OF = "2026-10-24"
REPO_URL = "https://github.com/arjunkshah12345-hash/breach-index-2026"
SITE_URL = "https://breach-index-2026.vercel.app"

# --------------------------------------------------------------------------
# Sources (short key -> (title, url))
# --------------------------------------------------------------------------
SRC = {
    "shark": ("SharkStriker: Top data breaches of October 2026", "https://sharkstriker.com/blog/october-2026-data-breaches/"),
    "nexora": ("CyberNexora: Black October 2026, 14 cyber incidents", "https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/"),
    "cma": ("Cyber Management Alliance: Major cyber attacks, September 2026", "https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026"),
    "breachsense": ("Breachsense: Data breaches in October 2026", "https://www.breachsense.com/breaches/2026/october/"),
    "techco": ("Tech.co: Data breaches that have happened this year (2026)", "https://tech.co/news/data-breaches-updated-list"),
    "quest_tc": ("TechCrunch: Quest Diagnostics confirms patient data compromised (2026-10-23)", "https://techcrunch.com/2026/10/23/lab-testing-giant-quest-diagnostics-confirms-patients-personal-and-health-data-was-compromised-during-breach/"),
    "quest_ti": ("Tech Insider: Quest Diagnostics Quanum LSM breach", "https://tech-insider.org/quest-diagnostics-quanum-lsm-breach-2026/"),
    "ets_mb": ("Malwarebytes: Millions of California students' data stolen", "https://www.malwarebytes.com/blog/data-breaches/2026/10/millions-of-california-students-sensitive-data-stolen-in-breach"),
    "capcom_ir": ("Capcom: Notice regarding customer information affected through unauthorized access", "https://www.capcom.co.jp/ir/english/news/html/e261022.html"),
    "capcom_hns": ("Help Net Security: Capcom data breach exposes 11.7M account records", "https://www.helpnetsecurity.com/2026/10/23/capcom-id-data-breach-11-million-records-exposed/"),
    "capcom_sw": ("SecurityWeek: 11 million impacted by Capcom data breach", "https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/"),
    "railway": ("Railway blog: Security disclosure / preliminary report, Oct 21 incident", "https://blog.railway.com/"),
    "idcf_bc": ("BleepingComputer: Ransomware attack disrupts Japan's IDCF Cloud", "https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/"),
    "idcf_cn": ("Cybernews: Cyberattack on Japanese cloud firm hits railways, police, food suppliers", "https://cybernews.com/security/japanese-cloud-cyberattack-railways-police-495-organizations-idcf/"),
    "idcf_rescana": ("Rescana: IDCF Cloud ransomware amid wider Japan attack wave", "https://www.rescana.com/post/idcf-cloud-ransomware-japan-attack-wave-october-2026"),
    "fr_sudradio": ("Sud Radio (AFP): Supermarkets hit by cyberattack on refrigeration systems", "https://www.sudradio.fr/societe/des-supermarches-victimes-dune-cyberattaque-visant-leurs-installations-frigorifiques-confirment-cooperative-u-et-intermarche"),
    "fr_parismatch": ("Paris Match: Supermarkets forced to throw away fresh and frozen goods", "https://www.parismatch.be/actualites/monde/2026/10/12/inedit-et-dune-extreme-gravite-de-nombreux-supermarches-contraints-de-jeter-une-grande-quantite-de-produits-frais-et-surgeles-en-france-2K5XHP7LYFB6PCUIU56YP65GQA/"),
    "ahold_bc": ("BleepingComputer: Retail giant Ahold Delhaize takes systems offline after cyberattack", "https://bleepingcomputer.com/news/security/retail-giant-ahold-delhaize-takes-systems-offline-after-cyberattack"),
    "ahold_reg": ("The Register: Ahold Delhaize incident", "https://www.theregister.com/a/5303970"),
    "bitget_thn": ("The Hacker News: Bitget confirms third-party zero-day", "https://thehackernews.com/2026/10/bitget-confirms-third-party-zero-day.html"),
    "bitget_bc": ("BleepingComputer: Bitget hacked via zero-day in third-party security products", "https://bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products"),
    "bitget_block": ("The Block: Bitget attacker tested risk controls with small transfers", "https://www.theblock.co/news/regulation/2026-09-28-bitget-attacker-tested-risk-controls-small-transfers-388-million-theft-ceo-says-417045"),
    "fbi_bc": ("BleepingComputer: ShinyHunters claims FBI hack via PeopleSoft", "https://bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach"),
    "fbi_hns": ("Help Net Security: FBI job portals remain offline", "https://www.helpnetsecurity.com/2026/09/28/fbi-job-portals-offline-shinyhunters-breach/"),
    "fbi_vectra": ("Vectra: ShinyHunters breached the FBI by bypassing the fix", "https://www.vectra.ai/blog/shinyhunters-breached-the-fbi-by-bypassing-the-fix"),
    "ai_ti": ("Tech Insider: AI agent hacker breaches 100+ firms (citing Reuters)", "https://tech-insider.org/ai-agent-hacker-breach-100-companies-2026/"),
    "fw_thn": ("The Hacker News: Hackers breach enterprise firewalls and VPNs, 70,000+ credentials", "https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html"),
    "japan_wave": ("Malware News: Japan data breaches 2026, inside the October surge", "https://malware.news/t/japan-data-breaches-2026-inside-the-october-surge/126558"),
    "shiny_tracker": ("State of Surveillance: ShinyHunters 2026 breach tracker", "https://stateofsurveillance.org/news/shinyhunters-2026-breach-tracker-salesforce-carnival-canvas-campaign/"),
    "csis": ("CSIS: Significant cyber incidents", "https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents"),
    "blackfog": ("BlackFog: The state of ransomware, September 2026", "https://www.blackfog.com/the-state-of-ransomware-september-2026/"),
    "aryza": ("HookPhish: Aryza data breach, Qilin ransomware claim", "https://www.hookphish.com/blog/ransomware-group-qilin-hits-aryza/"),
}

# --------------------------------------------------------------------------
# Categories: how the attackers got in, and the baseline controls that stop it
# --------------------------------------------------------------------------
CATEGORIES = {
    "credentials": {
        "title": "Stolen or reused credentials",
        "why": "Attackers log in with a valid username/password or key (phished, bought from infostealer logs, reused from an older breach, or never rotated). No exploit needed, so it looks like normal use.",
        "prevent": [
            "Phishing-resistant MFA (FIDO2/passkeys) on every externally reachable login, including SFTP, VPN, admin panels, CI/CD and cloud consoles. No password-only exceptions for 'legacy' systems.",
            "Rotate every credential after any prior incident, and monitor infostealer/breach feeds for your domains and vendors.",
            "Replace long-lived static secrets with short-lived tokens (OIDC workload identity, SSO-issued sessions).",
            "Alert on impossible travel, new devices, and unusual data volume per account. Most of these intrusions ran for weeks.",
            "Least privilege and data minimisation: an account that can read everything turns one stolen login into a mass breach.",
        ],
    },
    "third-party": {
        "title": "Third-party vendor and supply-chain compromise",
        "why": "The victim was never breached directly. A vendor, SaaS provider, cloud host, plugin, or software release they trusted was compromised and used as the way in.",
        "prevent": [
            "Inventory which vendors hold your data and what they can reach. Tier them, and require MFA, logging, breach-notification SLAs and deletion on contract end.",
            "Give integrations scoped, revocable, IP-restricted credentials, never shared admin keys. Rotate them on any vendor incident.",
            "Minimise and expire the data you send to vendors (inquiry systems, mailing lists, fulfilment partners).",
            "Verify software you install: signed releases, provenance attestations (Sigstore/SLSA), pinned hashes, and staged rollout of updates.",
            "Plan for a provider outage: keep independent backups and a tested restore path outside the provider.",
        ],
    },
    "unpatched": {
        "title": "Unpatched or zero-day flaw in internet-facing software",
        "why": "A vulnerability in an edge device or public app (VPN, firewall, security appliance, ERP, CI server, upload handler, API) gave attackers code execution or data access.",
        "prevent": [
            "Keep an external attack-surface inventory and patch known-exploited bugs (CISA KEV) within days, not quarters.",
            "Treat vendor 'temporary mitigations' (WAF rules, config workarounds) as stopgaps. Several 2026 breaches came from bypassing them.",
            "Keep management interfaces of VPNs, firewalls and appliances off the internet. Put them on an isolated management network.",
            "Assume an edge device will be popped: segment it from crown-jewel systems and monitor it for new web shells and outbound connections.",
            "Sandbox risky processing (file uploads, image parsing) and run it with minimal privileges.",
        ],
    },
    "social-engineering": {
        "title": "Social engineering (vishing, help-desk impersonation, fraudulent requests)",
        "why": "Attackers talk a human into handing over access: calling the help desk, posing as IT to get an MFA approval, or sending a fake official data request.",
        "prevent": [
            "Help-desk identity verification that can't be beaten on a phone call (video and ID check, manager callback, no MFA resets on inbound calls).",
            "Phishing-resistant MFA, so there is no push to approve and no code to read out.",
            "Bind sessions to devices and alert on token reuse from new IPs.",
            "Verify official or legal data requests out of band, using contact details you already hold, never those in the request.",
            "Run regular vishing drills for executives, finance and IT support.",
        ],
    },
    "exposure": {
        "title": "Exposed services, misconfiguration and internal error",
        "why": "Nobody had to break in. A database, AI agent platform, or service was reachable without authentication, or an internal mistake published data.",
        "prevent": [
            "Default-deny network exposure. Scan your own IP space and cloud accounts continuously for open databases, storage buckets and admin and AI-agent panels.",
            "Require authentication on every internal tool, including self-hosted AI agent platforms, even if it is 'just a test'.",
            "Run cloud posture management (CSPM) with alerts on public resources.",
            "Code-review and test any automated customer messaging. AI-generated code needs the same review as human-written code.",
            "Log and rate-limit, so sustained automated probing is visible.",
        ],
    },
    "ot": {
        "title": "Operational technology and physical systems",
        "why": "Attackers reached controllers that run physical equipment (refrigeration, building management, industrial systems) and changed how it behaved.",
        "prevent": [
            "Never expose OT controllers or vendor remote-management portals directly to the internet.",
            "Route vendor remote access through a brokered, MFA-protected, logged path that is only enabled when needed.",
            "Change default credentials and patch controller firmware.",
            "Enforce safe limits locally (hard setpoint bounds, interlocks), so a remote command can't push equipment out of a safe range.",
            "Alert on setpoint or mode changes outside maintenance windows, and practise manual fallback.",
        ],
    },
    "undisclosed": {
        "title": "Vector not yet disclosed (ransomware, intrusion, data theft)",
        "why": "The organisation has confirmed or been accused of a breach, but has not said how attackers got in. Across 2026 incidents where the vector did come out, the usual causes were stolen credentials, unpatched edge devices, and third parties.",
        "prevent": [
            "The basics that break most ransomware chains: phishing-resistant MFA everywhere, patching edge devices fast, EDR on every endpoint and server, and no flat networks.",
            "Immutable, offline or logically separated backups, with restores tested against a realistic scenario.",
            "Data-exfiltration detection: alert on large outbound transfers and unusual cloud-storage uploads.",
            "Data minimisation and retention limits, because data you deleted can't be stolen.",
            "Keep an incident-response plan and retainer on hand, and practise the 'take the website and apps offline' decision before you need it.",
        ],
    },
}

# --------------------------------------------------------------------------
# Incidents.  status: Confirmed | Partially confirmed | Claimed (unverified) | Reported (secondary sources)
# --------------------------------------------------------------------------
INCIDENTS = [
    # ---------------- stolen / reused credentials ----------------
    dict(
        name="Educational Testing Service (ETS) / California Dept. of Education", slug="ets-california-students",
        sector="Education", country="US", date="2026-10-19", date_note="access May 22 to Sep 18; reported Oct 19",
        category="credentials", status="Confirmed", attacker="Unknown",
        impact="Data on millions of current and former California public-school students (anyone enrolled in the last three school years at least; 5.7M+ enrolled in 2025-26 alone): names, Statewide Student IDs, DOB, home address, demographics, disability and program data, test scores. No SSNs or financial data.",
        what="An unauthorized party used compromised login credentials to access an SFTP file-transfer site run by ETS, the state's testing contractor, and copied files repeatedly over about four months.",
        root_cause="Valid credentials on an internet-facing SFTP server, apparently with no second factor. The long dwell time points to no alerting on bulk downloads.",
        prevention=[
            "Put SFTP behind SSO with phishing-resistant MFA, or use key-based auth with IP allow-listing for named partner systems only.",
            "Don't leave years of student records sitting on a transfer site. Files should be picked up and then auto-deleted.",
            "Alert on download volume per account; four months of repeated copying should have tripped something.",
            "Contracts with state testing vendors should require MFA, logging and retention limits, with audits.",
        ],
        sources=["ets_mb"],
    ),
    dict(
        name="Nikkei", slug="nikkei",
        sector="Media", country="Japan", date="2026-10-07", date_note="unauthorized access Oct 7",
        category="credentials", status="Confirmed", attacker="Unknown",
        impact="About 1.83M records accessed: about 150,000 with personal information, about 120,000 with email addresses. No card data. No misuse found as of Oct 16.",
        what="Attackers got into a cloud service Nikkei used for system development.",
        root_cause="Previously compromised credentials were still valid, and the development environment held real personal data.",
        prevention=[
            "Rotate all credentials after any prior compromise, including those for dev and test tooling.",
            "Use masked or synthetic data in development environments, not production personal data.",
            "Require SSO and MFA on developer SaaS, and watch infostealer feeds for employee credentials.",
        ],
        sources=["nexora"],
    ),
    dict(
        name="Florida Highway Safety & Motor Vehicles (DAVID database)", slug="florida-flhsmv-david",
        sector="Government", country="US", date="2026-09-12", date_note="claimed Sep 8, confirmed Sep 12",
        category="credentials", status="Confirmed", attacker="ShinyHunters",
        impact="ShinyHunters claimed 200,000+ driver records. FLHSMV confirmed the breach but did not state its scope.",
        what="Attackers logged into the DAVID driver and motor-vehicle database with a Plant City police officer's credentials.",
        root_cause="Law-enforcement credentials were stored improperly on a personal device, and the database accepted them without device or MFA checks strong enough to stop reuse.",
        prevention=[
            "Phishing-resistant MFA and managed-device (conditional access) checks on any law-enforcement data system.",
            "Per-user query-volume limits and alerts; a single officer pulling bulk records is anomalous.",
            "Ban credential storage on personal devices, and enforce it with technical controls, not only policy.",
        ],
        sources=["cma", "shark"],
    ),
    dict(
        name="Veradigm", slug="veradigm",
        sector="Healthcare IT", country="US", date="2026-09-09", date_note="reported Sep 9",
        category="credentials", status="Confirmed", attacker="Unknown",
        impact="Patient information downloaded from some healthcare customers, including SSNs in some cases. Clinical data not compromised.",
        what="An unauthorized party used stolen credentials belonging to a third-party vendor to call a Veradigm API and download patient data.",
        root_cause="A vendor API credential that was long-lived and broadly scoped, with no anomaly detection on bulk pulls.",
        prevention=[
            "Issue vendor API credentials scoped to the minimum data, IP-restricted, short-lived, and bound with mTLS where possible.",
            "Rate-limit and alert on bulk record retrieval per client.",
            "Require vendors to protect the credentials you issue them (secret managers, MFA on their side).",
        ],
        sources=["cma"],
    ),
    dict(
        name="Dropbox users (via Lenovo ID email-verification flaw)", slug="dropbox-lenovo-id",
        sector="Cloud storage", country="Global", date="2026-09-02", date_note="reported Sep 2",
        category="credentials", status="Reported (secondary sources)", attacker="Unknown",
        impact="About 5,000 Dropbox accounts accessed without passwords; some files viewed and downloaded.",
        what="Attackers abused a Lenovo email-verification flaw to create Lenovo IDs claiming victims' email addresses, then signed into the matching Dropbox accounts via federated login.",
        root_cause="An identity-federation logic flaw: a relying party trusted an email claim from an identity provider that had not actually verified the email.",
        prevention=[
            "Relying parties should link federated accounts on the IdP's immutable subject ID, never on email alone, and require email_verified.",
            "Require step-up re-authentication before linking a new federated login to an existing account.",
            "IdPs must verify email ownership before asserting it.",
        ],
        sources=["cma"],
    ),

    # ---------------- third-party / supply chain ----------------
    dict(
        name="IDC Frontier (IDCF Cloud, SoftBank)", slug="idc-frontier-idcf-cloud",
        sector="Cloud / data centre", country="Japan", date="2026-10-07", date_note="ransomware Oct 7",
        category="third-party", status="Confirmed", attacker="Not disclosed",
        impact="495 companies and local governments affected. Virtual servers in four availability zones stopped and could not restart, and customers were warned they might have to restore from their own backups. Downstream victims include JR East / View Card (about 6.09M records), Nissui logistics, and Ibaraki Prefecture and prefectural police websites.",
        what="Ransomware took down part of IDCF Cloud. The provider isolated the affected region. It later said no data was taken from customer VMs, which conflicts with some customers' notices.",
        root_cause="Entry vector not disclosed. Because it hit many tenants at once, the attackers most likely reached the shared management or virtualisation layer rather than individual tenants.",
        prevention=[
            "Providers: isolate the hypervisor and management plane on a separate network with phishing-resistant MFA and just-in-time admin access, and keep immutable backups of tenant volumes.",
            "Customers: keep your own backups outside the provider, and test a restore into a second region or provider.",
            "Customers: contracts should require breach notice within hours and spell out recovery responsibilities.",
        ],
        sources=["idcf_bc", "idcf_cn", "idcf_rescana", "shark"],
    ),
    dict(
        name="East Japan Railway (JR East) / View Card", slug="jr-east-view-card",
        sector="Transport", country="Japan", date="2026-10-07", date_note="via IDCF Cloud attack",
        category="third-party", status="Confirmed", attacker="Not disclosed",
        impact="Email-delivery data covering about 6.09M accounts may have been compromised.",
        what="JR East and its card subsidiary were hit through the ransomware attack on their cloud host, IDC Frontier.",
        root_cause="Concentration risk: customer email-delivery data was hosted with a single cloud provider that was then compromised.",
        prevention=[
            "Keep only the data a vendor needs for the task (for example, hashed or tokenised identifiers instead of full contact lists where possible).",
            "Map and tier cloud-provider dependencies, and require isolation and backup guarantees.",
        ],
        sources=["idcf_bc", "idcf_cn", "shark"],
    ),
    dict(
        name="Nissui", slug="nissui",
        sector="Food processing", country="Japan", date="2026-10-07", date_note="via IDCF Cloud attack",
        category="third-party", status="Confirmed", attacker="Not disclosed",
        impact="Its logistics subsidiary stopped shipping at all sites, with partial restart on Oct 9.",
        what="Systems hosted in a third-party data centre (IDCF) went down in the ransomware attack.",
        root_cause="Business-critical logistics depended on a single hosting provider with no failover.",
        prevention=[
            "Run business-continuity plans for losing a hosting provider, including manual shipping procedures.",
            "Keep failover or restore capability in a second environment for order and logistics systems.",
        ],
        sources=["idcf_bc", "shark"],
    ),
    dict(
        name="Citizen Watch (via Scala Communications)", slug="citizen-watch-scala",
        sector="Manufacturing / IT vendor", country="Japan", date="2026-10-05", date_note="reported Oct 5-6",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="Scala: up to 713,126 customer-inquiry records across 5+ client companies. Citizen: about 100,000 customers, including names, addresses, phone numbers, emails, and bank and credit-card information.",
        what="Attackers accessed the FAQ and inquiry-management system Scala Communications runs for client companies.",
        root_cause="An outsourced customer-support system held sensitive financial data and was compromised (vector not disclosed).",
        prevention=[
            "Never let payment or bank details sit in support-ticket or FAQ systems; redact them on intake.",
            "Purge support-inquiry data on a retention schedule.",
            "Assess vendor security for any outsourced system that holds customer PII.",
        ],
        sources=["shark"],
    ),
    dict(
        name="Daiwa Securities Group", slug="daiwa-securities",
        sector="Finance", country="Japan", date="2026-10-05", date_note="reported around Oct 5",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="More than 110,000 clients' names and account numbers.",
        what="An external vendor was breached and Daiwa client data was exposed.",
        root_cause="Third-party vendor compromise (details not disclosed).",
        prevention=[
            "Share only the fields a vendor needs, and tokenise account numbers where possible.",
            "Require vendor breach notification and audit rights.",
        ],
        sources=["shark"],
    ),
    dict(
        name="Daiichi Kosho (via Nippon Columbia)", slug="daiichi-kosho",
        sector="Entertainment", country="Japan", date="2026-10-01", date_note="October 2026",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="About 8.72M customers: names, gender, DOB, emails, phone numbers.",
        what="Daiichi Kosho's supplier, Nippon Columbia Group, was hit by a cyberattack that exposed Daiichi Kosho customer data.",
        root_cause="Supplier compromise (vector not disclosed).",
        prevention=[
            "Limit and expire the customer data shared with group companies and suppliers.",
            "Include suppliers in your security monitoring and incident-response plans.",
        ],
        sources=["shark"],
    ),
    dict(
        name="Trezor (via ShipMonk and via Brevo); BitBox; CoinTracking", slug="trezor-shipmonk-brevo",
        sector="Crypto hardware / fintech", country="Global", date="2026-09-10", date_note="ShipMonk Sep 5; Brevo Sep 10",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="ShipMonk exposed about 67,000 more US Trezor customers (names, emails, phones, addresses, orders). In a separate incident, 138 Brevo email-marketing accounts were breached, contacts were exported from 43, and phishing emails seeking wallet seed phrases went out through legitimate crypto mailing lists.",
        what="Two separate vendor compromises: a fulfilment partner (ShipMonk) still held old records that should have been deleted, and the email-marketing platform (Brevo) had customer accounts taken over and used to send phishing.",
        root_cause="Vendor data retention failure (ShipMonk), and compromised marketing-platform accounts that could send as trusted brands (Brevo).",
        prevention=[
            "Contracts should require deletion of shipping data after fulfilment, with verified deletion.",
            "Turn on MFA and IP-restricted API keys for email service provider accounts, and alert on contact exports.",
            "Tell crypto customers repeatedly that you will never ask for a seed phrase.",
        ],
        sources=["cma"],
    ),
    dict(
        name="Bimbo Bakeries USA", slug="bimbo-bakeries",
        sector="Food manufacturing", country="US", date="2026-09-06", date_note="reported Sep 6",
        category="third-party", status="Confirmed", attacker="Clop",
        impact="Employee data stolen, including names and SSNs. Total not disclosed.",
        what="Clop exploited an Oracle E-Business Suite zero-day through a third-party vendor's environment.",
        root_cause="A zero-day in Oracle EBS, reached through a vendor.",
        prevention=[
            "Don't expose ERP systems (Oracle EBS, PeopleSoft) to the internet; require VPN or zero-trust access.",
            "Patch Oracle CPU releases promptly, and know which vendors run ERP on your behalf.",
            "Encrypt or tokenise SSNs at the field level in HR systems.",
        ],
        sources=["cma"],
    ),
    dict(
        name="BigCommerce merchants (via Ribon apps)", slug="bigcommerce-ribon",
        sector="E-commerce", country="Global", date="2026-09-22", date_note="access Sep 13-17; reported Sep 22",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="Shopper names, emails, phone numbers, shipping addresses. Malicious scripts were injected into some storefronts. Passwords and payment cards were not affected.",
        what="Attackers used compromised credentials for the third-party Ribon / Ribon 1.5 apps to read shopper data and inject scripts into merchant stores.",
        root_cause="An over-privileged third-party app was compromised, and storefronts had no protection against script injection.",
        prevention=[
            "Review and minimise the permissions of marketplace apps, and remove unused ones.",
            "Use Content-Security-Policy and Subresource Integrity, and monitor payment-page scripts (PCI DSS 4.0 requirements 6.4.3 and 11.6.1).",
            "Platforms: rotate app credentials and alert on bulk reads by an app.",
        ],
        sources=["cma"],
    ),
    dict(
        name="UpdraftPlus / TeamUpdraft (WordPress)", slug="updraftplus",
        sector="Software (WordPress plugins)", country="Global", date="2026-10-18", date_note="Oct 17-18 weekend",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="Commands sent to connected WordPress sites created unexpected admin users and installed malicious plugins. The risk is mainly to sites connected through UpdraftCentral remote management.",
        what="The attacker got into TeamUpdraft's website with a compromised key, stole UpdraftCentral connection keys, and used them to command customer sites.",
        root_cause="One vendor-side key compromise gave remote control of many customer sites, because the remote-management keys were stored centrally.",
        prevention=[
            "Vendors: store remote-management keys encrypted in an HSM or KMS, separate from the web tier, and require customer-side approval for high-risk commands.",
            "Site owners: disconnect remote-management services you don't use, and audit admin users and plugins.",
            "Alert on new admin-user creation in WordPress.",
        ],
        sources=["nexora"],
    ),
    dict(
        name="OVHcloud CLI", slug="ovhcloud-cli",
        sector="Cloud / developer tooling", country="France / Global", date="2026-10-19", date_note="94-minute window, 14:47-16:21 UTC+2",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="Release binaries for v0.11.0 to v0.15.0 were replaced with malicious files. Anyone who downloaded and ran them during the window should rotate exposed secrets.",
        what="A compromised developer account was used to swap legitimate release files for malicious ones. Source code and the build chain were not affected.",
        root_cause="A single developer account could overwrite published release artifacts.",
        prevention=[
            "Make releases immutable once published; nobody should be able to replace a binary after release.",
            "Sign artifacts and publish provenance (Sigstore / SLSA). Users should verify signatures or pinned checksums.",
            "Require hardware-key MFA for maintainers, and two-person approval for release changes.",
        ],
        sources=["nexora"],
    ),
    dict(
        name="Railway", slug="railway",
        sector="Developer platform (PaaS)", country="US", date="2026-10-21", date_note="disclosed Oct 21",
        category="third-party", status="Confirmed", attacker="Unknown",
        impact="An unauthorized party may have accessed encrypted customer environment variables and decrypted some of them (API keys, database credentials, registry credentials). Railway told all users to rotate secrets and paused deployments.",
        what="Railway detected anomalous activity in the systems that store customer environment variables. It suggested this may be one of a series of attacks on platform companies and AI inference providers (unconfirmed).",
        root_cause="Full root cause not yet published. The attacker reached both the stored secrets and the means to decrypt them.",
        prevention=[
            "Platforms: use envelope encryption with KMS or HSM keys that only the running workload's identity can use to decrypt, so stored secrets plus database access is not enough.",
            "Customers: prefer short-lived credentials (OIDC federation to AWS/GCP, scoped database users) over static keys in environment variables.",
            "Customers: set spend limits and alerts on LLM and API keys (OpenAI, Anthropic, OpenRouter, Stripe) to catch abuse fast.",
        ],
        sources=["railway", "nexora"],
    ),

    # ---------------- unpatched / zero-day edge ----------------
    dict(
        name="Bitget", slug="bitget",
        sector="Crypto exchange", country="Global", date="2026-09-24", date_note="first access Aug 31; theft Sep 24",
        category="unpatched", status="Confirmed", attacker="Not confirmed (one outlet says North Korea)",
        impact="About $387.5M drained from hot and warm wallets. Cold wallets and user balances were covered by the protection fund.",
        what="Attackers used zero-days in two third-party security appliances, planted a web shell, moved laterally to the production wallet job server, obtained high-privilege internal credentials, and issued fraudulent withdrawals. First they sent small test transfers that stayed under the risk-control threshold.",
        root_cause="Security appliances had network reach into the wallet infrastructure. Withdrawal authority sat on a server that could be commanded once compromised, and risk checks only looked at single transactions.",
        prevention=[
            "Isolate security appliances; they should have no route to production wallet systems.",
            "Require multi-party HSM or MPC signing with policy enforced outside the hot server (velocity limits, allow-lists, human approval above thresholds).",
            "Risk controls should flag patterns (new destinations, cumulative volume, test-then-drain), not only single transfers.",
            "Watch appliances for web shells and unexpected outbound C2 traffic.",
        ],
        sources=["bitget_thn", "bitget_bc", "bitget_block"],
    ),
    dict(
        name="FBI (FBIJobs.gov / applicant portal)", slug="fbi-peoplesoft",
        sector="Government", country="US", date="2026-09-22", date_note="claimed Sep 22",
        category="unpatched", status="Claimed (unverified)", attacker="ShinyHunters",
        impact="ShinyHunters claims 2-3 TB on current and former employees and applicants. A 5,000-record sample was partly matched by Reuters. The FBI confirmed only that it is investigating activity affecting FBIJobs.gov; the job portals were taken offline.",
        what="ShinyHunters says it exploited Oracle PeopleSoft and then pivoted into FBI-managed AWS GovCloud.",
        root_cause="Linked to CVE-2026-35273 (unauthenticated RCE in PeopleSoft PeopleTools, patched by Oracle in June). Mandiant and Vectra describe a one-character substitution that slipped past the recommended WAF workaround.",
        prevention=[
            "Apply the vendor patch; don't rely on WAF rules as the long-term fix.",
            "Keep HR and applicant systems off the open internet where possible, and segment them from cloud admin roles.",
            "Use least-privilege cloud roles, so a compromised app server can't pivot across the cloud account.",
        ],
        sources=["fbi_bc", "fbi_hns", "fbi_vectra", "cma"],
    ),
    dict(
        name="Japan Digital Agency (Government Solution Service)", slug="japan-digital-agency",
        sector="Government", country="Japan", date="2026-09-14", date_note="reported Sep 14",
        category="unpatched", status="Confirmed", attacker="Unknown",
        impact="About 246,000 personnel records potentially exposed: names, emails, phone numbers, addresses.",
        what="An attacker exploited a vulnerability in a VPN device to reach an internal system.",
        root_cause="An unpatched (or zero-day) VPN appliance.",
        prevention=[
            "Patch VPN appliances within days of a fix, or replace VPN with identity-aware zero-trust access.",
            "Monitor VPN appliances for compromise indicators, and segment what VPN users can reach.",
        ],
        sources=["cma"],
    ),
    dict(
        name="Gyazo", slug="gyazo",
        sector="Consumer software", country="Japan / Global", date="2026-09-18", date_note="reported Sep 18",
        category="unpatched", status="Confirmed", attacker="Unknown",
        impact="About 23.62M user records plus metadata from about 490M images: password hashes, session IDs, IPs, and EXIF location data.",
        what="Attackers exploited a flaw in the image-upload server to execute commands.",
        root_cause="Command execution in the upload-processing path, with access to the user database from that server.",
        prevention=[
            "Process uploads in a sandboxed, unprivileged worker with no database credentials.",
            "Strip EXIF and location data at upload time and don't keep it.",
            "Hash passwords with a modern KDF (Argon2id or bcrypt), and invalidate sessions after a breach.",
        ],
        sources=["cma"],
    ),
    dict(
        name="CenterPoint Energy", slug="centerpoint-energy",
        sector="Utilities", country="US", date="2026-09-16", date_note="reported Sep 16",
        category="unpatched", status="Partially confirmed", attacker="Actor using a hex-encoded handle",
        impact="About 7.49M records claimed: names, SSNs, phone numbers, addresses, account and billing data for some customers. CenterPoint confirmed unauthorized access. Electricity and gas were unaffected.",
        what="The attacker claimed to have pulled data through an external-facing API.",
        root_cause="An external API exposed bulk customer data, most likely through broken object-level authorization or weak API authentication (exact flaw not disclosed).",
        prevention=[
            "Keep an inventory of every external API, and test for broken object-level authorization (OWASP API #1).",
            "Rate-limit and alert on bulk enumeration; 7M records should never leave through a customer API.",
            "Never return SSNs from customer-facing APIs; mask them server-side.",
        ],
        sources=["cma"],
    ),
    dict(
        name="JetBrains (Cadence environment)", slug="jetbrains-cadence",
        sector="Software", country="Global", date="2026-09-05", date_note="reported Sep 5",
        category="unpatched", status="Confirmed", attacker="Unknown",
        impact="Possible exposure of AWS credentials, secrets and backups. Users were told to rotate credentials.",
        what="Attackers exploited an unpatched critical TeamCity vulnerability to reach the Cadence environment.",
        root_cause="An unpatched CI/CD server. TeamCity auth-bypass bugs (for example CVE-2026-63077) are also being used by ransomware gangs.",
        prevention=[
            "Treat CI/CD as crown jewels: patch fast, never expose it publicly, and require SSO and MFA.",
            "Keep cloud credentials out of CI; use OIDC federation for short-lived tokens.",
        ],
        sources=["cma"],
    ),
    dict(
        name="Frontline Education", slug="frontline-education",
        sector="EdTech", country="US", date="2026-10-01", date_note="October 2026",
        category="unpatched", status="Confirmed", attacker="Unknown",
        impact="SSNs, emails and addresses of employees at affected school districts. Scope under investigation.",
        what="Hackers exploited a vulnerability in third-party software used by Frontline.",
        root_cause="An unpatched third-party component.",
        prevention=[
            "Keep a software bill of materials, and track vulnerabilities in third-party components.",
            "Encrypt SSNs at the field level and restrict who can read them.",
        ],
        sources=["shark"],
    ),

    # ---------------- social engineering ----------------
    dict(
        name="Revolut", slug="revolut",
        sector="Fintech", country="UK / EU", date="2026-09-12", date_note="reported Sep 12",
        category="social-engineering", status="Confirmed", attacker="Unknown",
        impact="Customer DOBs, contact details, passport and licence copies, possible selfies, statements and transaction histories. Systems and funds unaffected.",
        what="Fraudulent data requests sent from a legitimate government-agency email domain led Revolut to hand over customer data.",
        root_cause="A fake official data request (emergency or law-enforcement style) from a compromised or spoofed real government mailbox was trusted because of the sender domain.",
        prevention=[
            "Verify every legal or law-enforcement data request out of band, by calling a known number for the agency, and use LE portals where they exist.",
            "Apply a two-person rule and minimum-necessary disclosure for legal requests.",
            "Don't treat the sender domain as proof; government mailboxes get compromised.",
        ],
        sources=["cma"],
    ),

    # ---------------- exposure / misconfig / AI ----------------
    dict(
        name="Vietnam APIS airline passenger database", slug="vietnam-apis-database",
        sector="Aviation / Government", country="Vietnam", date="2026-09-08", date_note="reported Sep 8",
        category="exposure", status="Reported (secondary sources)", attacker="None identified (exposure)",
        impact="About 220M records: names, passport numbers, nationality, DOB, flight and seat details.",
        what="A misconfigured cloud database holding advance passenger information was publicly reachable until researchers alerted authorities.",
        root_cause="Cloud database exposed to the internet without authentication.",
        prevention=[
            "Default-deny network rules on databases, with continuous public-exposure scanning (CSPM).",
            "Encrypt passport fields, and keep an access log so exposure can be scoped.",
        ],
        sources=["cma"],
    ),
    dict(
        name="Bee Cheng Hiang", slug="bee-cheng-hiang",
        sector="Retail (food)", country="Singapore", date="2026-09-30", date_note="reported Sep 30",
        category="exposure", status="Confirmed", attacker="None (internal error)",
        impact="95,364 customer email addresses exposed to other recipients. No misuse found.",
        what="A bug in AI-assisted code caused bulk marketing emails to reveal recipient addresses.",
        root_cause="AI-generated code shipped without adequate review or testing of a privacy-sensitive path.",
        prevention=[
            "Review and test AI-written code like any other, especially anything that touches customer data.",
            "Send bulk email through an ESP that sends one message per recipient, never multi-recipient To or CC.",
            "Do a canary send to an internal list before any bulk send.",
        ],
        sources=["cma"],
    ),

    # ---------------- OT / physical ----------------
    dict(
        name="Intermarché and Coopérative U (refrigeration systems)", slug="intermarche-cooperative-u",
        sector="Grocery retail", country="France", date="2026-10-12", date_note="night of Oct 11-12",
        category="ot", status="Confirmed", attacker="Unknown (Paris prosecutor / OFAC investigating)",
        impact="150-200 Intermarché stores and fewer than 100 Coopérative U stores had to throw away all fresh and frozen products. No data theft reported. Insurers may not cover the losses.",
        what="Attackers remotely forced refrigeration units into defrost across hundreds of stores overnight. One report says Danfoss refrigeration controls were targeted (unconfirmed).",
        root_cause="Refrigeration controllers or their remote-management platform were reachable and controllable from outside. Exact path not disclosed.",
        prevention=[
            "Never expose refrigeration or building-management controllers to the internet; use a brokered, MFA-protected vendor access path.",
            "Change default credentials and patch controller firmware.",
            "Set hard local temperature limits and alarms that a remote 'defrost' command can't override for hours.",
            "Run overnight alerting to on-call staff for mass setpoint or mode changes.",
        ],
        sources=["fr_sudradio", "fr_parismatch", "shark"],
    ),

    # ---------------- vector not disclosed ----------------
    dict(
        name="Quest Diagnostics (Quanum Lab Services Manager)", slug="quest-diagnostics",
        sector="Healthcare", country="US", date="2026-10-21", date_note="discovered Oct 21; 8-K filed Oct 22",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Patient personal information and records (PHI) taken. Count not disclosed. Quanum is used by about 500,000 clinicians across North America.",
        what="Unauthorized access to Quanum, Quest's lab ordering and billing system, which involved 'certain patient records'.",
        root_cause="Not disclosed.",
        prevention=[
            "Phishing-resistant MFA for every clinician and admin login to Quanum-type portals.",
            "Bulk-export detection on PHI systems.",
            "Quest's 2019 breach (11.9M records) came through a billing vendor; review third-party access to Quanum too.",
        ],
        sources=["quest_tc", "quest_ti"],
    ),
    dict(
        name="Capcom (CAPCOM ID)", slug="capcom-id",
        sector="Video games", country="Japan / Global", date="2026-10-19", date_note="detected Oct 19; disclosed Oct 22",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="11,774,247 CAPCOM ID records (emails, plus per some reports usernames, last-login time, login count and IP). Fuller data on 43 accounts. Attackers changed passwords on 196 accounts, which were then reset. No card data.",
        what="A third party accessed CAPCOM ID customer data. Games were unaffected.",
        root_cause="Not disclosed. The attackers were able to change account passwords, which suggests access to account-management functions, not just a read-only data copy.",
        prevention=[
            "Notify users and require re-verification on every password or email change.",
            "Offer MFA and passkeys on game accounts.",
            "Restrict and log admin or API paths that can change credentials.",
            "Users: expect Capcom-themed phishing emails.",
        ],
        sources=["capcom_ir", "capcom_hns", "capcom_sw"],
    ),
    dict(
        name="Ahold Delhaize (Food Lion, Giant Food, The GIANT Company, Stop & Shop, Hannaford, and others)", slug="ahold-delhaize",
        sector="Grocery retail", country="US / EU", date="2026-10-12", date_note="disclosed Oct 12; update Oct 19",
        category="undisclosed", status="Confirmed", attacker="Not identified",
        impact="Websites and apps went offline across most brands in Europe and the US, disrupting pickup and delivery. Stores stayed open. No data theft confirmed as of the Oct 19 update.",
        what="Suspicious activity led to precautionary shutdowns; the company later confirmed 'malicious actions of others'. This is its second major incident in two years (the 2024 INC Ransom attack affected 2.2M people).",
        root_cause="Not disclosed. The Register asked, without confirming, whether it is linked to the French refrigeration attacks the same weekend.",
        prevention=[
            "After a prior ransomware incident, run a full compromise assessment and rotate every credential; repeat incidents often reuse old footholds.",
            "Segment e-commerce from corporate IT, so a precautionary shutdown of one doesn't take down the other.",
            "Keep tested failover for online ordering.",
        ],
        sources=["ahold_bc", "ahold_reg", "nexora"],
    ),
    dict(
        name="Keio Corporation", slug="keio",
        sector="Transport / hospitality", country="Japan", date="2026-09-26", date_note="attack Sep 26; confirmed Sep 28",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Hospitality and payment business systems disrupted; network shut down for containment. Railway operations unaffected. About 59,000 email addresses reportedly exposed.",
        what="Ransomware hit Keio's business systems.",
        root_cause="Not disclosed.",
        prevention=[
            "Keep OT (rail) and IT segmented, which appears to have worked here.",
            "Use immutable backups for payment and hospitality systems.",
        ],
        sources=["cma", "techco"],
    ),
    dict(
        name="State Bank of India (SBI)", slug="sbi",
        sector="Banking", country="India", date="2026-10-16", date_note="alerts Oct 16; reported Oct 21",
        category="undisclosed", status="Partially confirmed", attacker="'Siriusim' (claimed)",
        impact="A 375,000-record dark-web dataset was reviewed; SBI identified 3,897 customer records with PII (name, mobile, DOB, email, address, customer ID, loan details). Core operations unaffected.",
        what="SBI investigated suspected customer-data exposure after alerts from threat intelligence, the Defence Cyber Agency and CERT-In.",
        root_cause="Not disclosed; may involve a subsidiary or vendor.",
        prevention=[
            "Monitor the dark web for your own data, which is how this was caught.",
            "Apply data-loss prevention to loan-processing and partner channels.",
        ],
        sources=["nexora", "shark"],
    ),
    dict(
        name="Ampath Laboratories", slug="ampath-laboratories",
        sector="Healthcare (pathology)", country="South Africa", date="2026-10-15", date_note="October 2026",
        category="undisclosed", status="Claimed (unverified)", attacker="BytetoBreach",
        impact="80M patient records claimed (names, ID numbers, DOB, sex, addresses, emails, phones). Unverified.",
        what="Ransomware attack and data-theft claim.",
        root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category.", "Apply data retention limits to historical lab-patient records."],
        sources=["shark"],
    ),
    dict(
        name="Skyticket (Adventure Inc.)", slug="skyticket-adventure",
        sector="Travel", country="Japan", date="2026-10-01", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="14.64M records: names, DOB, emails, phones, postal addresses, hashed passwords.",
        what="A cyberattack exposed customer information.", root_cause="Not disclosed.",
        prevention=["Use a modern password hashing algorithm, and force resets.", "Use the baseline controls for this category."],
        sources=["shark"],
    ),
    dict(
        name="Yakiniku King (Monogatari Corp.)", slug="yakiniku-king-monogatari",
        sector="Restaurants", country="Japan", date="2026-10-05", date_note="disclosed Oct 5",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Data of 10,788,963 app members.", what="Breach of member data for the official app.", root_cause="Not disclosed.",
        prevention=["Collect less app-member data, and expire inactive accounts.", "Use the baseline controls for this category."],
        sources=["shark"],
    ),
    dict(
        name="Mr.Max Holdings", slug="mr-max",
        sector="Retail", country="Japan", date="2026-10-06", date_note="reported Oct 6",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="1,735,154 members: IDs, names, emails, phones.", what="Unauthorized access to company servers.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="GMO Research & AI", slug="gmo-research",
        sector="Market research", country="Japan", date="2026-10-01", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Up to 948,500 members: names, emails, addresses.", what="A cyberattack exposed panel member data.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="GMO Internet (Onamae.com Desktop Cloud)", slug="gmo-onamae-desktop-cloud",
        sector="Hosting", country="Japan", date="2026-10-10", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="26,739 customer servers potentially affected; malicious programs installed in some. Trading-tool credentials saved on them may be exposed. Service suspended.",
        what="Unauthorized access led to malware being installed in customer desktop-cloud environments.",
        root_cause="Not disclosed. Pushing to many tenants at once suggests the shared management layer.",
        prevention=["Isolate the provider management plane, and alert on mass software deployment.", "Customers: don't save brokerage credentials in tools on shared desktop clouds; use MFA on trading accounts."],
        sources=["nexora"],
    ),
    dict(
        name="Zeabur", slug="zeabur",
        sector="Cloud deployment platform", country="Taiwan / Global", date="2026-10-14", date_note="disclosed Oct 14; shutdown announced Oct 17",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Unauthorized access to internal systems and some customer services, the second incident after one in August. The company is winding down: services stop from Dec 1, and all servers by Dec 31, 2026.",
        what="A repeat intrusion with broader scope than the August incident, followed by a decision to shut the company down.",
        root_cause="Not disclosed. The repeat incident suggests incomplete eradication after August.",
        prevention=["After an incident, do full eradication: rebuild from known-good images and rotate every secret, not just the obvious ones.", "Customers: keep portable deployments and exports, so a platform shutdown isn't fatal."],
        sources=["nexora"],
    ),
    dict(
        name="Aesto Health", slug="aesto-health",
        sector="Healthcare IT", country="US", date="2026-09-01", date_note="access Dec 2-18 2025; disclosed Sep 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="9,540,683 individuals: names, DOB, medical, insurance, government ID, financial account data, SSNs.",
        what="Unauthorized access to part of Aesto's AWS infrastructure.", root_cause="Not disclosed (AWS environment access).",
        prevention=["Use AWS GuardDuty and CloudTrail alerting, least-privilege IAM, and no long-lived access keys.", "Notify faster; nine months from access to disclosure is too long."],
        sources=["cma"],
    ),
    dict(
        name="AdaptHealth", slug="adapthealth",
        sector="Healthcare", country="US", date="2026-09-10", date_note="reported Sep 10",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="4.1M+ people: personal, health and insurance data.", what="An attacker accessed systems.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["cma"],
    ),
    dict(
        name="US Department of Defense (Defense Manpower Data Center)", slug="dod-dmdc",
        sector="Government", country="US", date="2026-09-30", date_note="reported Sep 30",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="2.76M living and 294,000 deceased individuals: SSNs and job details. No misuse found.",
        what="Breach of personnel data.", root_cause="Not disclosed.",
        prevention=["Purge or archive offline the records of deceased and long-separated personnel.", "Use the baseline controls for this category."],
        sources=["cma"],
    ),
    dict(
        name="Times Car Rental", slug="times-car-rental",
        sector="Car rental", country="Japan", date="2026-09-30", date_note="reported Sep 30",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="About 6.6M accounts; about 1.6M documents accessed, including ID-verification images.",
        what="Breach of accounts and stored documents.", root_cause="Not disclosed.",
        prevention=["Don't keep ID-verification images after verification; store only the result.", "Use the baseline controls for this category."],
        sources=["cma"],
    ),
    dict(
        name="Denmark Central Population Registry (CPR) and Technical University of Denmark (DTU)", slug="denmark-cpr-dtu",
        sector="Government / Education", country="Denmark", date="2026-10-10", date_note="October 2026",
        category="undisclosed", status="Reported (secondary sources)", attacker="Unknown",
        impact="CPR: 8.8M people (names, addresses, CPR numbers). DTU: about 200,000 people from identity and access management systems.",
        what="Reported breaches of the national civil registry and of DTU's identity and access management systems, with large-scale exfiltration at DTU.",
        root_cause="Not disclosed.",
        prevention=["Treat the IAM system itself as tier 0, with privileged-access workstations and MFA for admins.", "Monitor bulk directory exports."],
        sources=["shark", "techco"],
    ),
    dict(
        name="Nueva EPS", slug="nueva-eps",
        sector="Health insurance", country="Colombia", date="2026-10-04", date_note="Oct 4",
        category="undisclosed", status="Claimed (unverified)", attacker="Unknown seller",
        impact="Database of 11M+ people listed for sale: IDs, DOB, addresses, medical, disability and mental-health data.",
        what="Database offered on a hacking forum.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="Condé Nast", slug="conde-nast",
        sector="Media", country="US", date="2026-09-07", date_note="Sep 7",
        category="undisclosed", status="Claimed (unverified)", attacker="Unknown seller",
        impact="About 32.8M accounts offered for $15,000; a sample matched genuine 2025 data. Emails, names, addresses, DOB, phones; no passwords.",
        what="A user database was offered on a Russian-language forum. Not confirmed by the company.",
        root_cause="Not disclosed.", prevention=["Use the baseline controls for this category."], sources=["cma"],
    ),
    dict(
        name="IDScan", slug="idscan",
        sector="Identity verification", country="US", date="2026-09-10", date_note="Sep 10",
        category="undisclosed", status="Reported (secondary sources)", attacker="Unknown",
        impact="150M+ driver's licence records and photos reportedly on the dark web.",
        what="Hackers stole ID records from cloud systems.", root_cause="Not disclosed.",
        prevention=["ID-verification vendors should keep scan images only briefly, with encryption and strict deletion.", "Use the baseline controls for this category."],
        sources=["cma"],
    ),
    dict(
        name="Weverse (HYBE)", slug="weverse",
        sector="Entertainment", country="South Korea", date="2026-09-10", date_note="Sep 10",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="422,584 accounts: internal IDs and purchase, payment-method and refund details.",
        what="Account and transaction information compromised.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["cma"],
    ),
    dict(
        name="Novocure", slug="novocure",
        sector="Medical devices", country="US", date="2026-09-01", date_note="access mid-Aug; reported Sep 1",
        category="undisclosed", status="Confirmed", attacker="ShinyHunters",
        impact="Internal patient IDs from 1,400+ US records; identifying data for under 50 others; provider and employee contacts.",
        what="Unauthorized access to some information systems.",
        root_cause="Not disclosed. ShinyHunters' 2026 playbook is mostly vishing for SSO or SaaS credentials and exploiting PeopleSoft.",
        prevention=["Use the controls listed under the social-engineering category (help-desk verification, phishing-resistant MFA).", "Review OAuth app grants in SaaS tenants."],
        sources=["cma", "shiny_tracker"],
    ),
    dict(
        name="Astrana Health", slug="astrana",
        sector="Healthcare", country="US", date="2026-09-24", date_note="SEC filing Sep 24",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Potential exposure of confidential data; some systems restored from clean backups.",
        what="Unauthorized access to servers.", root_cause="Not disclosed.",
        prevention=["Clean, tested backups worked here; make them standard practice."], sources=["cma"],
    ),
    dict(
        name="Ludwig Maximilian University of Munich (LMU)", slug="lmu-munich",
        sector="Education", country="Germany", date="2026-09-21", date_note="Sep 21",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Student enrolment data: names, DOB, contacts, bank and health-insurance numbers, education records.",
        what="Attacker accessed the system holding enrolment data.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["cma"],
    ),
    dict(
        name="Mathspace", slug="mathspace",
        sector="EdTech", country="Australia", date="2026-09-07", date_note="Sep 7",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Over 1M students, staff and parents.", what="Systems breached and personal data stolen.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["cma"],
    ),
    dict(
        name="University of Illinois Chicago (College of Medicine)", slug="uic-college-of-medicine",
        sector="Education / Healthcare", country="US", date="2026-10-08", date_note="October 2026",
        category="undisclosed", status="Partially confirmed", attacker="Booba Project (claimed)",
        impact="344 GB of personal, research and academic data claimed; College of Medicine systems offline.",
        what="Cyberattack that forced systems offline.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="ASOS", slug="asos",
        sector="Retail (fashion)", country="UK", date="2026-10-08", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Names and contact details; volume under investigation.", what="Unauthorized access to a database.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="Georgia Power", slug="georgia-power",
        sector="Utilities", country="US", date="2026-10-08", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Some customer accounts accessed: names, addresses, phones, emails, last four SSN digits.",
        what="An unauthorized third party accessed some customer accounts.",
        root_cause="Not disclosed. Account-level access is typical of credential stuffing.",
        prevention=["Run credential-stuffing defences on customer portals (breached-password checks, bot detection, MFA).", "Don't display even partial SSNs in customer portals."],
        sources=["shark"],
    ),
    dict(
        name="MetaMask (Consensys)", slug="metamask",
        sector="Crypto wallet", country="Global", date="2026-10-01", date_note="disclosed Oct 1",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Some infrastructure affected; under investigation.", what="Cyberattack on infrastructure.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="UK fashion retail: The Foschini Group (Hobbs, Whistles) and Phase Eight", slug="uk-fashion-retail",
        sector="Retail (fashion)", country="UK", date="2026-10-08", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Some IT systems affected or taken offline; under investigation.", what="Separate cyberattacks on fashion retailers.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="Senture (US Department of Transportation contractor)", slug="senture-dot",
        sector="BPO / Government contractor", country="US", date="2026-10-08", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="The DOT took connected systems offline; under investigation.", what="Attack on the contractor.", root_cause="Not disclosed.",
        prevention=["Use the third-party category controls on the government side: scoped, quickly revocable contractor connectivity."], sources=["shark"],
    ),
    dict(
        name="Aryza", slug="aryza",
        sector="Fintech software", country="Ireland / UK", date="2026-10-23", date_note="leak-site listing Oct 23",
        category="undisclosed", status="Claimed (unverified)", attacker="Qilin",
        impact="Listed on Qilin's leak site.", what="Ransomware claim.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["aryza", "breachsense"],
    ),
    dict(
        name="Icon Oncology", slug="icon-oncology",
        sector="Healthcare", country="Australia", date="2026-10-08", date_note="October 2026",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="31,000+ documents with patient data.", what="Cyberattack exposed patient data.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["shark"],
    ),
    dict(
        name="Stadtwerke Landsberg", slug="stadtwerke-landsberg",
        sector="Utilities", country="Germany", date="2026-09-08", date_note="Sep 8",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Central IT network encrypted; office and communications disrupted; possible theft of customer and banking data. Essential services continued.",
        what="Encryption (ransomware) attack.", root_cause="Not disclosed.",
        prevention=["Segment utility OT from IT, which appears to have held here.", "Use immutable backups."], sources=["cma"],
    ),
    dict(
        name="Berlin state government (two departments)", slug="berlin-state-government",
        sector="Government", country="Germany", date="2026-09-05", date_note="Sep 5",
        category="undisclosed", status="Confirmed", attacker="Unknown ransomware group",
        impact="Stolen data published; extent under assessment.", what="Ransomware with data leak.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["cma"],
    ),
    dict(
        name="US municipalities: Heber City UT, Vicksburg MS, Radford VA, Everett MA; Springfield (MA) Public Schools", slug="us-municipalities",
        sector="Local government / Education", country="US", date="2026-10-10", date_note="Sep 8 to Oct 10",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Systems offline, including utility payments, email and phones; Springfield schools temporarily closed.",
        what="Separate cyber incidents disrupting local services.", root_cause="Not disclosed.",
        prevention=["Use the free CISA and MS-ISAC services for local governments (vulnerability scanning, MDBR, incident response).", "Phishing-resistant MFA on email, plus offline backups."],
        sources=["shark", "cma"],
    ),
    dict(
        name="Dyfed-Powys Police", slug="dyfed-powys-police",
        sector="Law enforcement", country="UK (Wales)", date="2026-09-25", date_note="Sep 25",
        category="undisclosed", status="Confirmed", attacker="Unknown",
        impact="Some non-emergency systems disrupted; staff information may have been accessed.",
        what="Cyberattack on police systems.", root_cause="Not disclosed.",
        prevention=["Use the baseline controls for this category."], sources=["cma"],
    ),
]

# Multi-victim campaigns (rendered into CAMPAIGNS.md)
CAMPAIGNS = [
    dict(
        name="AI-agent hacking spree (Cairn / DeepSeek / Claude Code)", period="From Sep 25, 2026; Reuters report Oct 19",
        victims="100+ companies in the US, Canada, Australia and Japan, including Deere, SharkNinja and Cummins. 1,200+ e-commerce sites targeted.",
        how="A single Chinese-speaking operator gave AI agents short natural-language instructions; the agents handled scanning, probing and exploitation, taking about 23 hours per breach and about $5,000 of tokens in total. A researcher found about two dozen internet-exposed instances of Cairn, an open-source AI agent platform, linked to the campaign. The exact weakness exploited on victim sites has not been confirmed.",
        prevent=["Assume attackers can probe every exposed endpoint continuously and cheaply. Patch faster and shrink your attack surface.", "Never expose self-hosted AI agent platforms without authentication.", "Add rate limits and logging that make sustained automated probing visible."],
        sources=["ai_ti"],
    ),
    dict(
        name="Storm-0940 'ARTEX' AI-accelerated Microsoft 365 attacks", period="Reported by Microsoft Oct 21, 2026",
        victims="2,250+ Microsoft 365 tenants targeted. Password spraying against 327 accounts at eight organisations described in detail. Being targeted does not mean being compromised.",
        how="A China-aligned actor used an agentic AI pentest framework for fast recon, password spraying, and abuse of applications with existing cloud access.",
        prevent=["Block legacy authentication, require phishing-resistant MFA, and use Entra ID smart lockout and password protection.", "Audit enterprise apps and service principals with broad Graph permissions."],
        sources=["nexora"],
    ),
    dict(
        name="ShinyHunters 2026 campaign (vishing, SSO/OAuth abuse, PeopleSoft)", period="All of 2026; Sep-Oct: FBI, Florida DAVID, Novocure, Clop leak-site hijack",
        victims="Dozens of companies, including Instructure/Canvas (30M+), Klue (about 200 downstream companies), and the FBI (claimed).",
        how="Voice phishing of help desks and employees for Okta and SSO credentials, malicious OAuth apps in SaaS tenants, and Oracle PeopleSoft exploitation (CVE-2026-35273, including WAF-rule bypass).",
        prevent=["Harden help-desk identity verification.", "Use phishing-resistant MFA.", "Restrict which OAuth apps users can authorise.", "Patch PeopleSoft and EBS."],
        sources=["shiny_tracker", "fbi_bc", "cma"],
    ),
    dict(
        name="Microsoft 365 help-desk vishing (PREY-0058)", period="Reported Sep 7, 2026",
        victims="Organisations in construction, healthcare, finance, real estate and professional services.",
        how="Callers posed as the IT help desk, got executives to hand over credentials and approve MFA prompts, then stole session tokens to reach SharePoint, OneDrive, Exchange and Box, and exfiltrated data for extortion.",
        prevent=["Use FIDO2 or passkeys (nothing to approve or read out), token protection or binding, and a policy that IT never calls you for MFA."],
        sources=["cma"],
    ),
    dict(
        name="Clop: PTC Windchill / FlexPLM and Oracle EBS exploitation", period="Ongoing through Sep-Oct 2026",
        victims="40+ organisations named (including Philips, GE and Shell, claimed), Bimbo Bakeries, and Matrix Document Imaging (leak-site listing Oct 22).",
        how="Mass exploitation of internet-exposed product-lifecycle and ERP systems for data theft and extortion.",
        prevent=["Take PLM and ERP systems off the public internet, and patch them immediately when Clop-targeted CVEs drop."],
        sources=["blackfog", "cma", "breachsense"],
    ),
    dict(
        name="Japan breach wave", period="Sep 25 to Oct 2026",
        victims="At least 36 Japanese organisations issued first breach notices between Sep 25 and Oct 8 alone (IDCF, JR East, Nikkei, Daiichi Kosho, Skyticket, Yakiniku King, Mr.Max, Citizen, Daiwa, Times Car, Keio, GMO, Capcom and others).",
        how="A mix of separate incidents. On Oct 19, a Japanese security firm tied part of the wave to a Chinese-developed AI penetration-testing tool.",
        prevent=["See the individual entries. The common threads are third-party and cloud concentration risk and stale credentials."],
        sources=["japan_wave", "idcf_rescana"],
    ),
    dict(
        name="Firewall / VPN credential theft (70,000+ credentials)", period="Reported Oct 2026; compromises mostly Feb-Jun 2026",
        victims="Enterprises using exposed network devices.",
        how="Group-IB and NyxLab found 70,000+ credentials tied to compromised network devices and LDAP dumps.",
        prevent=["Patch edge devices, rotate credentials stored on or passing through them, and don't bind VPNs to LDAP with over-privileged service accounts."],
        sources=["fw_thn"],
    ),
]

# Ransomware leak-site claims (unverified; rendered into LEAK-SITE-CLAIMS.md)
LEAK_CLAIMS = [
    ("2026-10-23", "Airtificial", "Qilin"), ("2026-10-23", "Annapath, Inc.", "Akira"),
    ("2026-10-23", "Dr. Schnell", "Rhysida"), ("2026-10-23", "Urologic Specialists of Oklahoma", "Everest"),
    ("2026-10-23", "AMSAM", "BravoX"), ("2026-10-22", "NBC Universal", "SCARLETTGROUP"),
    ("2026-10-22", "Whirlpool", "WhiteArmor"), ("2026-10-22", "Coastal Alabama Community College", "Interlock"),
    ("2026-10-22", "Matrix Document Imaging", "CL0P"), ("2026-10-22", "Smart & Biggar", "INC_RANSOM"),
    ("2026-10-22", "Adobe Insurance Brokers", "PEAR"), ("2026-10-21", "Haier Group", "Everest"),
    ("2026-10-21", "AVEVA Group", "Mimori"), ("2026-10-21", "St. James's Place plc", "Mimori"),
    ("2026-10-21", "Bruin", "EMPERADOR"), ("2026-10-21", "Aeroklas Duys", "DeadLock"),
    ("2026-10-20", "Baker Donelson", "REDACT"), ("2026-10-20", "Ultimate Health Plans", "LockBit"),
    ("2026-10-20", "Finzly", "n0n"), ("2026-10-20", "Memorial Hermann Endoscopy Center Kingwood", "n0n"),
    ("2026-10-19", "Amagi", "n0n"), ("2026-10-17", "Genesys", "SCARLETTGROUP"),
    ("2026-10-17", "ONEOK, Inc.", "REDACT"), ("2026-10-16", "Canva", "TheSevenDeadlySins"),
    ("2026-10-16", "Hospital Sírio-Libanês", "TheSevenDeadlySins"), ("2026-10-16", "Karix", "LockBit"),
    ("2026-10-15", "ODC Ltd", "KAIROS"), ("2026-10", "The Japan Times", "Eclipse"),
    ("2026-10", "Titus Germany", "Play"), ("2026-10", "Granja Avícola La Ponderosa", "Emperador"),
    ("2026-10", "Ömür Hırdavat", "Emperador"), ("2026-09-01", "Nutex Health", "Unnamed group"),
]


# The headline takeaways (title, evidence, fix) shown on the site
WHY = [
    ("Logins, not exploits",
     "Stolen, reused or never-rotated credentials (ETS, Nikkei, Florida DAVID, Veradigm), and help-desk vishing (ShinyHunters, PREY-0058).",
     "Phishing-resistant MFA everywhere, with no exceptions."),
    ("Through someone else",
     "IDCF Cloud took down 495 organisations at once. Scala exposed Citizen's customers. ShipMonk, Brevo, UpdraftPlus, the OVHcloud CLI and Railway's secret store were all used as ways in.",
     "Share as little data as possible, use scoped and revocable integration keys, and keep your own backups."),
    ("Edge boxes and enterprise apps",
     "Zero-days in VPNs, security appliances, PeopleSoft, EBS and TeamCity. Bitget lost $387.5M after two security appliances were compromised.",
     "Patch known-exploited bugs in days, keep management interfaces off the internet, and segment."),
    ("AI is speeding attackers up",
     "One operator with AI agents breached 100+ companies for about $5k. Storm-0940 used an agentic pentest tool against 2,250+ Microsoft 365 tenants.",
     "Assume constant, cheap probing, and shrink your attack surface."),
    ("Physical consequences",
     "Refrigeration controllers at hundreds of French supermarkets were forced into defrost overnight.",
     "Keep OT off the open internet, and enforce safety limits locally."),
]

# Top ten cross-cutting controls (title, detail), in rough order of payoff
TOP10 = [
    ("Phishing-resistant MFA (passkeys / FIDO2) on everything reachable from the internet.",
     "This includes SFTP, VPN, CI/CD, admin panels, SaaS and vendor portals. It defeats stolen passwords, MFA-fatigue and help-desk vishing, and would have stopped or blunted ETS, Nikkei, Florida DAVID, PREY-0058 and much of ShinyHunters."),
    ("Patch known-exploited vulnerabilities in days.",
     "Start with edge devices (VPNs, firewalls, security appliances) and enterprise apps (PeopleSoft, EBS, TeamCity, Windchill). Don't rely on WAF workarounds."),
    ("Keep management interfaces and OT off the internet.",
     "This covers appliance admin UIs, refrigeration and building controllers, databases, and self-hosted AI agent platforms."),
    ("Segment.",
     "A compromised appliance or web server must not be able to reach wallets, HR data, or the hypervisor (Bitget, IDCF)."),
    ("Replace static secrets with short-lived ones.",
     "Use OIDC workload identity and scoped, IP-restricted vendor keys, and rotate everything after any incident (Railway, Veradigm, Nikkei, Zeabur)."),
    ("Inventory third parties and minimise what they hold.",
     "Contracts should require MFA, logs, fast notification and deletion (Scala, ShipMonk, Daiwa, IDCF)."),
    ("Immutable backups outside your primary provider, with tested restores.",
     "The goal is to survive both ransomware and losing your cloud host."),
    ("Exfiltration detection.",
     "Alert on bulk downloads, API enumeration and unusual outbound transfers; several of these breaches ran for months."),
    ("Help-desk and legal-request verification.",
     "These processes must not be beatable by a convincing phone call or a real-looking government email (Revolut)."),
    ("Software supply-chain integrity.",
     "Use immutable, signed releases, verify what you install, and require hardware-key MFA for maintainers (OVHcloud CLI, UpdraftPlus)."),
]


# --------------------------------------------------------------------------
def src_md(keys):
    return "\n".join(f"- [{SRC[k][0]}]({SRC[k][1]})" for k in keys)


def render_incident(i):
    cat = CATEGORIES[i["category"]]
    return f"""# {i['name']}

| | |
|---|---|
| **Date** | {i['date']} ({i['date_note']}) |
| **Sector / country** | {i['sector']} · {i['country']} |
| **Attack type** | [{cat['title']}](../../PREVENTION-PLAYBOOK.md#{i['category']}) |
| **Status** | {i['status']} |
| **Attacker** | {i['attacker']} |

## What happened
{i['what']}

## Impact
{i['impact']}

## Why it happened (root cause)
{i['root_cause']}

## How it could have been prevented
{chr(10).join('- ' + p for p in i['prevention'])}

### Baseline controls for this attack type
{chr(10).join('- ' + p for p in cat['prevent'])}

## Sources
{src_md(i['sources'])}

_Compiled {AS_OF}. Details may change as investigations continue; claims by threat actors are unverified unless marked Confirmed._
"""


def render_readme():
    by_date = sorted(INCIDENTS, key=lambda x: x["date"], reverse=True)
    counts = Counter(i["category"] for i in INCIDENTS)
    known = sum(v for k, v in counts.items() if k != "undisclosed")
    rows = "\n".join(
        f"| {i['date']} | [{i['name']}](incidents/{i['category']}/{i['slug']}.md) | {i['sector']} | {CATEGORIES[i['category']]['title']} | {i['status']} |"
        for i in by_date
    )
    cat_rows = "\n".join(
        f"| [{c['title']}](PREVENTION-PLAYBOOK.md#{k}) | {counts.get(k, 0)} |" for k, c in CATEGORIES.items()
    )
    return f"""# Company Hacks: September to October 2026

A directory of organisations hacked or breached between **1 Sep and {AS_OF}**. Each entry says why it happened and how it could have been prevented.

- **{len(INCIDENTS)} incident files** in [`incidents/`](incidents/), grouped by how attackers got in
- **{len(CAMPAIGNS)} multi-victim campaigns** in [CAMPAIGNS.md](CAMPAIGNS.md)
- **{len(LEAK_CLAIMS)} unverified ransomware leak-site claims** in [LEAK-SITE-CLAIMS.md](LEAK-SITE-CLAIMS.md)
- **Cross-cutting fixes** in [PREVENTION-PLAYBOOK.md](PREVENTION-PLAYBOOK.md)
- **Website:** {SITE_URL} (source: [`site/index.html`](site/index.html), a single self-contained file with no dependencies)
- Machine-readable data in [`data/incidents.json`](data/incidents.json) and [`data/incidents.csv`](data/incidents.csv). Run `python3 build.py` to regenerate everything.

> This isn't literally every company. Ransomware trackers log roughly 700-800 victims a month (BlackFog counted 789 in September 2026 across 79 groups). This directory covers the notable, publicly reported cases, plus a list of leak-site claims.

## The short version: why companies are getting hacked right now

1. **Logins, not exploits.** Stolen, reused or never-rotated credentials (ETS, Nikkei, Florida DAVID, Veradigm), plus vishing of help desks (ShinyHunters, PREY-0058). Fix: phishing-resistant MFA everywhere, with no exceptions.
2. **Through someone else.** Cloud hosts (IDCF took down 495 organisations at once), support vendors (Scala to Citizen), fulfilment and email providers (ShipMonk, Brevo), plugins and CLIs (UpdraftPlus, OVHcloud), and PaaS secret stores (Railway). Fix: least data shared, scoped and revocable integration keys, and your own backups.
3. **Edge boxes and enterprise apps.** Zero-days in VPNs, security appliances, PeopleSoft, EBS and TeamCity (Bitget lost $387.5M after two security appliances were popped). Fix: patch known-exploited bugs in days, keep management interfaces off the internet, and segment.
4. **AI is speeding up attackers.** One operator with AI agents breached 100+ companies for about $5k. Storm-0940 used an agentic pentest tool against 2,250+ M365 tenants. Fix: assume constant, cheap probing, and shrink your attack surface.
5. **Physical consequences.** Refrigeration controllers at hundreds of French supermarkets were forced into defrost overnight. Fix: OT never on the open internet, with local safety limits.

Of the {len(INCIDENTS)} incidents, {known} have a publicly known entry vector; the other {counts.get('undisclosed', 0)} haven't been disclosed yet.

## By attack type
| Attack type | Incidents |
|---|---|
{cat_rows}

## All incidents (newest first)
| Date | Organisation | Sector | Attack type | Status |
|---|---|---|---|---|
{rows}

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

The social preview video (`site/og.mp4`, `site/og.png`) is rendered from the live hero animation: `cd tools && npm i && npm run og` (needs Node and ffmpeg).

Keep claims honest: use `Claimed (unverified)` for threat-actor posts, and don't guess at root causes the victim hasn't disclosed.

## License
Code is [MIT](LICENSE). Incident write-ups summarise public reporting; follow the linked sources for the originals.

_Compiled {AS_OF} from public reporting. Sources are listed in every file._
"""


def render_campaigns():
    parts = [f"# Multi-victim campaigns (Sep to Oct 2026)\n\nThese are operations that hit many organisations at once. See [README](README.md) for single incidents.\n"]
    for c in CAMPAIGNS:
        parts.append(f"""## {c['name']}
**When:** {c['period']}
**Victims:** {c['victims']}

**How:** {c['how']}

**Prevention:**
{chr(10).join('- ' + p for p in c['prevent'])}

**Sources:**
{src_md(c['sources'])}
""")
    return "\n".join(parts)


def render_playbook():
    sections = []
    for k, c in CATEGORIES.items():
        examples = ", ".join(
            f"[{i['name'].split(' (')[0]}](incidents/{k}/{i['slug']}.md)" for i in INCIDENTS if i["category"] == k
        )
        sections.append(f"""<a id="{k}"></a>
## {c['title']}
**Why it works:** {c['why']}

**Prevent it:**
{chr(10).join('- ' + p for p in c['prevent'])}

**Seen in:** {examples}
""")
    return f"""# Prevention Playbook

These fixes are grouped by how attackers got in during Sep to Oct 2026. If you only do ten things, do these, in roughly this order of payoff:

{chr(10).join(f'{n}. **{t}** {d}' for n, (t, d) in enumerate(TOP10, 1))}

{chr(10).join(sections)}
"""


def render_leaks():
    rows = "\n".join(f"| {d} | {v} | {g} |" for d, v, g in LEAK_CLAIMS)
    return f"""# Ransomware leak-site claims (unverified)

These organisations were **listed by ransomware or extortion groups** as victims in Sep to Oct 2026. Gangs sometimes exaggerate, recycle old data, or list companies they never breached, so treat every row as a claim only, until the company confirms it.

Root causes are unknown for all of these. The baseline controls in [PREVENTION-PLAYBOOK.md](PREVENTION-PLAYBOOK.md#undisclosed) apply.

| Listed | Organisation | Group |
|---|---|---|
{rows}

Sources: [{SRC['breachsense'][0]}]({SRC['breachsense'][1]}), [{SRC['shark'][0]}]({SRC['shark'][1]}), [{SRC['cma'][0]}]({SRC['cma'][1]}).
"""


def render_site():
    """Single self-contained dark HTML page, data embedded as JSON."""
    data = {
        "asOf": AS_OF,
        "repo": REPO_URL,
        "incidents": [{**i, "sources": [{"title": SRC[k][0], "url": SRC[k][1]} for k in i["sources"]]} for i in INCIDENTS],
        "campaigns": [{k: v for k, v in c.items() if k != "sources"} for c in CAMPAIGNS],
        "why": [{"t": t, "d": d, "f": f} for t, d, f in WHY],
        "categories": {k: {"title": c["title"], "prevent": c["prevent"]} for k, c in CATEGORIES.items()},
        "top10": TOP10,
        "claims": LEAK_CLAIMS,
    }
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = (ROOT / "site_template.html").read_text().replace("/*DATA*/", blob)
    return html.replace("/*SITE*/", SITE_URL.rstrip("/") + "/")


def main():
    inc_dir = ROOT / "incidents"
    for i in INCIDENTS:
        d = inc_dir / i["category"]
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{i['slug']}.md").write_text(render_incident(i))
    (ROOT / "README.md").write_text(render_readme())
    (ROOT / "CAMPAIGNS.md").write_text(render_campaigns())
    (ROOT / "PREVENTION-PLAYBOOK.md").write_text(render_playbook())
    (ROOT / "LEAK-SITE-CLAIMS.md").write_text(render_leaks())

    data_dir = ROOT / "data"
    data_dir.mkdir(exist_ok=True)
    out = [{**i, "category_title": CATEGORIES[i["category"]]["title"],
            "sources": [SRC[k][1] for k in i["sources"]]} for i in INCIDENTS]
    (data_dir / "incidents.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    fields = ["date", "name", "sector", "country", "category_title", "status", "attacker", "impact", "root_cause"]
    with open(data_dir / "incidents.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    site_dir = ROOT / "site"
    site_dir.mkdir(exist_ok=True)
    (site_dir / "index.html").write_text(render_site())
    print(f"Wrote {len(INCIDENTS)} incidents, {len(CAMPAIGNS)} campaigns, {len(LEAK_CLAIMS)} leak claims, site/index.html.")


if __name__ == "__main__":
    main()
