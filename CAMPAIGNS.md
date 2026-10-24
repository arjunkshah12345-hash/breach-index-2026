# Multi-victim campaigns (Sep to Oct 2026)

These are operations that hit many organisations at once. See [README](README.md) for single incidents.

## AI-agent hacking spree (Cairn / DeepSeek / Claude Code)
**When:** From Sep 25, 2026; Reuters report Oct 19
**Victims:** 100+ companies in the US, Canada, Australia and Japan, including Deere, SharkNinja and Cummins. 1,200+ e-commerce sites targeted.

**How:** A single Chinese-speaking operator gave AI agents short natural-language instructions; the agents handled scanning, probing and exploitation, taking about 23 hours per breach and about $5,000 of tokens in total. A researcher found about two dozen internet-exposed instances of Cairn, an open-source AI agent platform, linked to the campaign. The exact weakness exploited on victim sites has not been confirmed.

**Prevention:**
- Assume attackers can probe every exposed endpoint continuously and cheaply. Patch faster and shrink your attack surface.
- Never expose self-hosted AI agent platforms without authentication.
- Add rate limits and logging that make sustained automated probing visible.

**Sources:**
- [Tech Insider: AI agent hacker breaches 100+ firms (citing Reuters)](https://tech-insider.org/ai-agent-hacker-breach-100-companies-2026/)

## Storm-0940 'ARTEX' AI-accelerated Microsoft 365 attacks
**When:** Reported by Microsoft Oct 21, 2026
**Victims:** 2,250+ Microsoft 365 tenants targeted. Password spraying against 327 accounts at eight organisations described in detail. Being targeted does not mean being compromised.

**How:** A China-aligned actor used an agentic AI pentest framework for fast recon, password spraying, and abuse of applications with existing cloud access.

**Prevention:**
- Block legacy authentication, require phishing-resistant MFA, and use Entra ID smart lockout and password protection.
- Audit enterprise apps and service principals with broad Graph permissions.

**Sources:**
- [CyberNexora: Black October 2026, 14 cyber incidents](https://blog.cybernexora.com/black-october-2026-cybersecurity-incidents/)

## ShinyHunters 2026 campaign (vishing, SSO/OAuth abuse, PeopleSoft)
**When:** All of 2026; Sep-Oct: FBI, Florida DAVID, Novocure, Clop leak-site hijack
**Victims:** Dozens of companies, including Instructure/Canvas (30M+), Klue (about 200 downstream companies), and the FBI (claimed).

**How:** Voice phishing of help desks and employees for Okta and SSO credentials, malicious OAuth apps in SaaS tenants, and Oracle PeopleSoft exploitation (CVE-2026-35273, including WAF-rule bypass).

**Prevention:**
- Harden help-desk identity verification.
- Use phishing-resistant MFA.
- Restrict which OAuth apps users can authorise.
- Patch PeopleSoft and EBS.

**Sources:**
- [State of Surveillance: ShinyHunters 2026 breach tracker](https://stateofsurveillance.org/news/shinyhunters-2026-breach-tracker-salesforce-carnival-canvas-campaign/)
- [BleepingComputer: ShinyHunters claims FBI hack via PeopleSoft](https://bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach)
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

## Microsoft 365 help-desk vishing (PREY-0058)
**When:** Reported Sep 7, 2026
**Victims:** Organisations in construction, healthcare, finance, real estate and professional services.

**How:** Callers posed as the IT help desk, got executives to hand over credentials and approve MFA prompts, then stole session tokens to reach SharePoint, OneDrive, Exchange and Box, and exfiltrated data for extortion.

**Prevention:**
- Use FIDO2 or passkeys (nothing to approve or read out), token protection or binding, and a policy that IT never calls you for MFA.

**Sources:**
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)

## Clop: PTC Windchill / FlexPLM and Oracle EBS exploitation
**When:** Ongoing through Sep-Oct 2026
**Victims:** 40+ organisations named (including Philips, GE and Shell, claimed), Bimbo Bakeries, and Matrix Document Imaging (leak-site listing Oct 22).

**How:** Mass exploitation of internet-exposed product-lifecycle and ERP systems for data theft and extortion.

**Prevention:**
- Take PLM and ERP systems off the public internet, and patch them immediately when Clop-targeted CVEs drop.

**Sources:**
- [BlackFog: The state of ransomware, September 2026](https://www.blackfog.com/the-state-of-ransomware-september-2026/)
- [Cyber Management Alliance: Major cyber attacks, September 2026](https://www.cm-alliance.com/cybersecurity-blog/major-cyber-attacks-data-breaches-ransomware-attacks-september-2026)
- [Breachsense: Data breaches in October 2026](https://www.breachsense.com/breaches/2026/october/)

## Japan breach wave
**When:** Sep 25 to Oct 2026
**Victims:** At least 36 Japanese organisations issued first breach notices between Sep 25 and Oct 8 alone (IDCF, JR East, Nikkei, Daiichi Kosho, Skyticket, Yakiniku King, Mr.Max, Citizen, Daiwa, Times Car, Keio, GMO, Capcom and others).

**How:** A mix of separate incidents. On Oct 19, a Japanese security firm tied part of the wave to a Chinese-developed AI penetration-testing tool.

**Prevention:**
- See the individual entries. The common threads are third-party and cloud concentration risk and stale credentials.

**Sources:**
- [Malware News: Japan data breaches 2026, inside the October surge](https://malware.news/t/japan-data-breaches-2026-inside-the-october-surge/126558)
- [Rescana: IDCF Cloud ransomware amid wider Japan attack wave](https://www.rescana.com/post/idcf-cloud-ransomware-japan-attack-wave-october-2026)

## Firewall / VPN credential theft (70,000+ credentials)
**When:** Reported Oct 2026; compromises mostly Feb-Jun 2026
**Victims:** Enterprises using exposed network devices.

**How:** Group-IB and NyxLab found 70,000+ credentials tied to compromised network devices and LDAP dumps.

**Prevention:**
- Patch edge devices, rotate credentials stored on or passing through them, and don't bind VPNs to LDAP with over-privileged service accounts.

**Sources:**
- [The Hacker News: Hackers breach enterprise firewalls and VPNs, 70,000+ credentials](https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html)
