---
product: Cowork
positioning_type: function-agnostic
buyer: Enterprise (already deployed AI broadly)
owner: TBD
last_updated: 2026-09-05
status: draft # positioning language still needs an owner's sign-off; proof points below are sourced and dated
category: agentic workspace
---

# Cowork — Enterprise Positioning (function-agnostic)

## Positioning statement

Structured to Geoffrey Moore's framework (*Crossing the Chasm*). Personas below
inherit this shape and narrow it — see each persona's own value proposition.

> **For** enterprises that have deployed AI broadly but still see it used as an
> expensive search bar
> **that need** work completed rather than assisted
> **Cowork** **is an** agentic workspace
> **that** executes multi-step work and delivers finished outputs, deployed once
> by IT and configured per function.

> **Unlike** chat assistants and point copilots that answer questions and leave
> the work to the employee
> **Cowork provides** multi-step execution across the tools a team already uses,
> with the output finished rather than drafted.

**Category matters here.** "Agentic workspace" and "AI assistant" get evaluated
against different things — the first against outcomes, the second against
answers. Don't let an asset drift into the second.

### Long form
For enterprises that have deployed AI but still see it used as an expensive search bar or chat, Cowork is the agentic workspace that turns Claude into a task-doing coworker for every knowledge worker — deployed once by IT and configured with plugins for how each function actually works.

## Differentiation
Unlike chat assistants and point copilots that answer questions and leave the work to the employee, Cowork executes multi-step work and delivers finished outputs.

## Buyer problem
"We've deployed AI broadly and people are using it like a fancy search bar. We're months away from anything actually working. And when it does, no one uses it because it doesn't know how we do things here."

## Key message
Agents for every knowledge worker. Deployed once, configured for your org.

## Primary CTA
Get Cowork for your team

## Use cases
- Delegate multi-step work: research briefs from many sources, cross-source financial analysis, contract and vendor review, polished decks and docs.
- Scheduled tasks for recurring reports (weekly pipeline snapshot, Monday headcount summary).

## Connectors
- Microsoft 365 (SharePoint/OneDrive/Outlook/Teams, read-only)
- Slack (read/write)
- Google Workspace (Drive/Gmail/Calendar, read-only in Cowork)
- GitHub, Atlassian/Jira, HubSpot, Notion, Salesforce, Snowflake, Databricks, BigQuery, Box/Egnyte (via legal plugin)
- DocuSign, LegalZoom, Apollo, Outreach, MSCI, FactSet

## Value props and reasons to believe

### 1. Agent that executes, not just answers {#vp-executes}
Assign Cowork a task and it handles research, analysis, documentation and reporting autonomously while your team focuses on higher-value work.
- **RTB:** Multi-step execution without hand-holding — Claude handles the whole chain in the background, not just one step, and delivers high-quality outputs. Scheduled tasks let teams set recurring work once and have it delivered automatically.

### 2. Configured for how your org works {#vp-configured}
Plugins allow you to deploy Cowork pre-configured for your org. Employees get an agent that already knows how to work at your company, on day one.
- **RTB:** Plugins by job function and/or company-specific plugins that connect to org tools and include skills to perform specialized tasks. IT can manage the configuration.
- **RTB — shipped, open-source plugin roster** (11 as of 2026-09-05): productivity, sales, customer-support, product-management, marketing, legal, finance, data, enterprise-search, bio-research, cowork-plugin-management. Plus financial-services plugins covering comps, DCF, LBO and 3-statement models. This matters because "configured for your org" is otherwise an abstract promise — the roster is what makes it checkable.
  - *Marketing* — `/draft-content`, `/campaign-plan`, `/brand-review`, `/competitive-brief`, `/performance-report`, `/seo-audit`, `/email-sequence`. Connects Slack, Canva, Figma, HubSpot, Amplitude, Ahrefs, Klaviyo.
  - *Sales* — `/call-summary`, `/forecast`, `/pipeline-review`, plus contextual skills for account research, call prep, daily pipeline briefings, research-based outreach, and competitive intelligence (differentiation matrices and talk tracks). Connects via MCP to CRM, email, call transcription, enrichment and chat tools — and **runs standalone on notes, CSVs and pasted text when those aren't connected**, so value doesn't wait on a data-cleanup project.
  - *Legal* — `/review-contract` (clause-by-clause against your playbook, GREEN/YELLOW/RED with redlines), `/triage-nda`, `/vendor-check`, `/brief`, `/respond`. MCP connectors for document management, chat and project tracking, plus 20+ legal-specific ones spanning contract lifecycle (Ironclad, Docusign, Definely), document management (iManage, NetDocuments), e-discovery (Relativity, Everlaw, Consilio), research (Midpage, Trellis) and Harvey. Twelve practice-area plugins, each opening with a setup interview that learns the team's playbook, escalation chain, risk calibration and house style. Source: [Claude for the legal industry, 12 May 2026](https://claude.com/blog/claude-for-the-legal-industry). Product framing is explicit that **all outputs should be reviewed by licensed attorneys** — state this rather than softening it.
  - *Human Resources* — performance review drafting, compensation benchmarking, structured onboarding plans (30-60-90), policy summarization. Note that the first two sit in the most legally exposed HR domains; see `personas/chro.md` before leading with them.
  - *Finance* — journal entry prep, account reconciliation, financial statement generation, variance analysis, close management, audit support. Connects Snowflake, Databricks, BigQuery, Slack, Microsoft 365.
  - Source: [plugin directory](https://claude.com/plugins/marketing), [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins). Launched 2026-01-30.

### 3. One deployment covers everyone {#vp-coverage}
Every knowledge worker gets Cowork — across desktop, web, and mobile — working in Excel, PowerPoint, Chrome, and local files where it's installed. Every engineer gets Claude Code. One vendor, one deployment, full coverage.
- **RTB:** Claude Desktop enterprise deployment and controls, now extending to cloud-run Cowork (beta) for machines that could never run a desktop install — Windows-locked, VDI, or otherwise locked-down environments. A single vendor process and relationship across all functions — no shadow AI sprawl, no separate procurement cycle per team.

## Proof points

*Sourced from Anthropic's own published materials, all within the last ~60 days as of 2026-09-05. Update this section — and its `last_updated` note below — whenever these age past 90 days.*

**Usage data ([Anthropic blog, July 7, 2026 — "Claude Cowork on web and mobile"](https://claude.com/blog/cowork-web-mobile)):** Anthropic reported that more than 90% of Cowork usage wasn't software development — the largest categories were business operations and content creation, which together made up roughly half of all usage. The data was drawn from a sample of anonymized Cowork sessions across a large base of organizations, sampled in May 2026.

**Named customer example ([same source](https://claude.com/blog/cowork-web-mobile)):** A Ramp Customer Success team member described starting a client-tracking dashboard build on a laptop, then picking the same session up on their phone while waiting at baggage claim — the session held the thread across devices with no re-explaining needed. Illustrates the "your work follows you" claim concretely, from a real named customer at a real company.
> *Attribution: Armmand Hosseini, Customer Success, Ramp — quoted in Anthropic's July 7, 2026 blog post. Paraphrased here rather than reproduced verbatim; see source for the original wording.*

**Governance/compliance signal ([Anthropic blog, August 11, 2026 — "Compliance API coverage extends to Claude Cowork and Claude Code"](https://claude.com/blog/compliance-api-cowork-and-claude-code)):** Anthropic extended its Compliance API to cover Cowork sessions across desktop, web, and mobile (beta for Enterprise customers at time of writing, GA as of an August 26, 2026 update), letting security/compliance teams pull Cowork session content and metadata the same way they already do for Claude chats — without separate logging infrastructure per surface. Directly supports the "one deployment, no shadow AI sprawl" value prop with a concrete, recent capability rather than just a claim.

**Function-level proof, first-party ([Anthropic blog, July 8, 2026 — marketing operations](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds)):** Anthropic's own marketing ops team reduced a weekly metrics review from one to two days down to roughly two hours, and compressed multi-day event/campaign builds across Salesforce, HubSpot, Swoogo and Asana into an automated workflow. Notably the design is governed rather than autonomous: a separate audit agent (a fresh Claude instance) verifies output, a proofreading skill validates figures against verified sources, and a human approves before anything ships. Useful against the "AI produces unreviewable volume" objection, because the control structure is part of the described workflow rather than a promise.

**Function-level proof, first-party — SALES ([Anthropic blog, May 20, 2026](https://claude.com/blog/how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book)):** Travis Bryant, Head of US Mid-Market GTM, uses Cowork to run a 4,000-account book. Account propensity scoring across all 4,000 accounts ran overnight against five-dimension rubrics combining web research, Salesforce and BigQuery, producing an interactive dashboard with rationales — work previously requiring "hundreds of hours across RevOps, FP&A, and marketing." Also ~90 minutes/day of micro-optimizations and ~3 hours/week on forecast prep.
> **STALE — 108 days old as of 2026-09-05, past the 90-day ceiling.** Flag on use and seek a newer sales example. Kept because it is the only first-party sales evidence available and the alternative is third-party category research.
> `TODO(source)`: internal adoption rate of the Sales plugin at Anthropic is worth sourcing — it would be the strongest available answer to the rep-adoption objection. No dated, citable figure located.

**Function-level adoption, first-party — LEGAL (Anthropic AGC, interviewed 2026-05-12):** Following the February legal plugin launch, legal became the number-one power-user job function in Claude Cowork, at over three times the usage of any other function; a single April webinar drew over 20,000 registrations. Claude is reported at 90.9% on BigLaw Bench with particular strength in grounding and citation faithfulness. Useful as an existence proof that legal can lead adoption — not as a profile of any given legal team, and not a benchmark to measure a cautious one against.
> **STALE — 116 days old as of 2026-09-05.** Flag on use. Benchmark figure is vendor-reported; say so.
> `TODO(source)`: the repo has no counsel-reviewed position on privilege or work product. It is a standard question from legal buyers and currently routes to escalation. See `personas/general-counsel.md`.

**Commercial model:** see `pricing/cowork-enterprise.md`. It is `SYNTHETIC` — structure and placeholders only, no figures. Assets must say terms are unavailable rather than estimate them.

**Freshness check:** as of 2026-09-05, the original three points and the marketing-ops example are ≤60 days old; the sales example is 108 days old and flagged stale above. Re-verify or replace before ~2026-12-05 (90-day ceiling) or sooner if Anthropic publishes newer usage data.
