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
  - *Finance* — journal entry prep, account reconciliation, financial statement generation, variance analysis, close management, audit support. Connects Snowflake, Databricks, BigQuery, Slack, Microsoft 365.
  - Source: [plugin directory](https://claude.com/plugins/marketing), [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins). Launched 2026-01-30.

### 3. One deployment covers everyone {#vp-coverage}
Every knowledge worker gets Cowork — across desktop, web, and mobile — working in Excel, PowerPoint, Chrome, and local files where it's installed. Every engineer gets Claude Code. One vendor, one deployment, full coverage.
- **RTB:** Claude Desktop enterprise deployment and controls, now extending to cloud-run Cowork (beta) for machines that could never run a desktop install — Windows-locked, VDI, or otherwise locked-down environments. A single vendor process and relationship across all functions — no shadow AI sprawl, no separate procurement cycle per team.

## Proof points

*Sourced from Anthropic's own published materials, all within the last ~60 days as of 2026-09-05. Update this section — and its `last_updated` note below — whenever these age past 90 days.*

**Usage data (Anthropic blog, July 7, 2026 — "Claude Cowork on web and mobile"):** Anthropic reported that more than 90% of Cowork usage wasn't software development — the largest categories were business operations and content creation, which together made up roughly half of all usage. The data was drawn from a sample of anonymized Cowork sessions across a large base of organizations, sampled in May 2026.

**Named customer example (same source):** A Ramp Customer Success team member described starting a client-tracking dashboard build on a laptop, then picking the same session up on their phone while waiting at baggage claim — the session held the thread across devices with no re-explaining needed. Illustrates the "your work follows you" claim concretely, from a real named customer at a real company.
> *Attribution: Armmand Hosseini, Customer Success, Ramp — quoted in Anthropic's July 7, 2026 blog post. Paraphrased here rather than reproduced verbatim; see source for the original wording.*

**Governance/compliance signal (Anthropic blog, August 11, 2026 — "Compliance API coverage extends to Claude Cowork and Claude Code"):** Anthropic extended its Compliance API to cover Cowork sessions across desktop, web, and mobile (beta for Enterprise customers at time of writing, GA as of an August 26, 2026 update), letting security/compliance teams pull Cowork session content and metadata the same way they already do for Claude chats — without separate logging infrastructure per surface. Directly supports the "one deployment, no shadow AI sprawl" value prop with a concrete, recent capability rather than just a claim.

**Function-level proof, first-party (Anthropic blog, July 8, 2026 — marketing operations):** Anthropic's own marketing ops team reduced a weekly metrics review from one to two days down to roughly two hours, and compressed multi-day event/campaign builds across Salesforce, HubSpot, Swoogo and Asana into an automated workflow. Notably the design is governed rather than autonomous: a separate audit agent (a fresh Claude instance) verifies output, a proofreading skill validates figures against verified sources, and a human approves before anything ships. Useful against the "AI produces unreviewable volume" objection, because the control structure is part of the described workflow rather than a promise.

**Freshness check:** as of 2026-09-05, all four points above are ≤60 days old. Re-verify or replace before ~2026-12-05 (90-day ceiling) or sooner if Anthropic publishes newer usage data.
