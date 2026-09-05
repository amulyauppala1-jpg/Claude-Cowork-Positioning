# Refresh Tasks — Keeping `products/cowork-enterprise.md` Current

Three scheduled tasks, not one, because "is this file stale" is actually three different questions at three different cadences. Each is written as a Cowork scheduled-task prompt you'd set up once manually, confirm the output, then turn recurring with `/schedule`.

**Assumption:** these prompts assume a GTM team has these connectors available — swap in whatever your org actually has connected. The point isn't the specific tool, it's matching the *kind* of staleness to the *kind* of source that can actually catch it. A web-search task will never find a real customer quote sitting in a sales call; a call-recording tool will never tell you a competitor just shipped the same feature.

---

## 1. Proof points — monthly

**Why this cadence:** the file's own freshness note gives proof points a 90-day shelf life. Monthly catches expiry with room to spare before anything goes stale in front of a prospect.

**Assumed connectors:** a call-recording/conversation-intelligence tool (e.g. Gong), a testimonial platform (e.g. UserEvidence), a public review site (e.g. G2).

**Task prompt:**
> Check `products/cowork-enterprise.md`'s Proof Points section for any entry older than 75 days. For each one nearing expiry: search [call-recording tool] for recent customer calls mentioning Cowork, check [testimonial platform] for new sourced quotes, and check [review site] for recent reviews mentioning multi-step task execution or plugin configuration. Only use a quote or stat that's genuinely dated and attributable — never draft a placeholder. Open a pull request with proposed replacements; do not push to main.

---

## 2. Market/competitive positioning — quarterly

**Why this cadence:** differentiation claims ("unlike chat assistants that just answer questions...") don't go stale week to week — they go stale when a competitor ships something that closes the gap. That's a slower-moving signal.

**Assumed connector:** web search (this is the one job web search is actually well-suited for — it's a public-web question, not an internal-data question).

**Task prompt:**
> Search for recent product launches or positioning from agentic-workspace competitors (e.g. Microsoft Copilot, Glean, Sierra). Compare against the "Differentiation" and "Value props and reasons to believe" sections of `products/cowork-enterprise.md`. Flag anything that suggests a claim in the file is no longer a clean differentiator, with sources. Don't rewrite the file — draft a short summary as a GitHub issue for the owner to review.

---

## 3. Internal drift signal — weekly (or event-driven, if your Slack connector supports it)

**Why this cadence:** this isn't about finding new information — it's about catching the moment someone *notices* the file is wrong before it quietly causes a bad conversation with a prospect.

**Assumed connector:** Slack, watching a specific team feedback channel.

**Task prompt:**
> Scan [#gtm-feedback or equivalent channel] for messages suggesting Cowork positioning, pricing, or use-case language doesn't match what reps are actually seeing in the field. Summarize any such mentions from the past week, with links back to the original messages. Don't attempt to resolve them — flag for the owner.

---

## Shared rule across all three

None of these tasks should ever push directly to `main`. A scheduled task finding a stale proof point and a human merging the replacement are two different steps on purpose — automating the *check* is safe; automating the *judgment call* about what counts as on-positioning is exactly the thing this whole repo exists to keep a human in charge of.
