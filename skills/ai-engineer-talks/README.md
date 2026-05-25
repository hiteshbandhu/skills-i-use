# AI engineer talks

**34** actionable skills from ingested [@aiDotEngineer](https://www.youtube.com/@aiDotEngineer) playlists ([ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills)).

**Publish hygiene:** validate via [create-a-skill](../create-a-skill/SKILL.md) before ingest `./scripts/sync-skills.sh` ([docs/PUBLISH.md](https://github.com/hiteshbandhu/ingest-into-skills/blob/main/docs/PUBLISH.md)).

**Gaps / retry collect:** [ingest `playlists/_retry-later.json`](https://github.com/hiteshbandhu/ingest-into-skills/blob/main/playlists/_retry-later.json)

## Install

**Recommended — Skills CLI** (discovered via repo [`.claude-plugin/marketplace.json`](../../.claude-plugin/marketplace.json)):

```bash
# List all 34 skills (grouped under "Ai Engineer Talks")
npx skills add hiteshbandhu/skills-i-use --list

# Install one skill
npx skills add hiteshbandhu/skills-i-use --skill build-rag-search-stacks -a cursor -g
```

**Manual copy** (any agent):

```bash
cp -r skills/ai-engineer-talks/<skill-name> ~/.claude/skills/
cp -r skills/ai-engineer-talks/<skill-name> ~/.cursor/skills/
cp -r skills/ai-engineer-talks/<skill-name> ~/.codex/skills/
```

## Skills

| Skill | Topic |
|-------|--------|
| [`architect-enterprise-ai`](architect-enterprise-ai/) | Enterprise AI architecture, agents, voice, CIAM |
| [`author-agent-skills`](author-agent-skills/) | Authoring and scaling agent skills |
| [`build-agent-harnesses`](build-agent-harnesses/) | Agent harness design & maturity |
| [`build-aiewf-2024-rag`](build-aiewf-2024-rag/) | AIEWF 2024 RAG & frameworks |
| [`build-generative-media`](build-generative-media/) | Generative image/video products |
| [`build-multimodal-products`](build-multimodal-products/) | Multimodal & voice products |
| [`build-rag-search-stacks`](build-rag-search-stacks/) | Production RAG / AI search |
| [`build-robotics-ai`](build-robotics-ai/) | Robotics & autonomy |
| [`build-with-deepmind`](build-with-deepmind/) | Gemini, Gemma, DeepMind stack |
| [`build-with-microsoft-ai`](build-with-microsoft-ai/) | Microsoft agents & observability |
| [`build-with-openai`](build-with-openai/) | OpenAI APIs, voice, Codex |
| [`deploy-public-sector-ai`](deploy-public-sector-ai/) | Government / public-sector AI |
| [`design-agent-skills`](design-agent-skills/) | Skills + MCP, Langfuse |
| [`evaluate-with-braintrust`](evaluate-with-braintrust/) | Braintrust evals & observability |
| [`lead-ai-engineering-teams`](lead-ai-engineering-teams/) | AI-era engineering leadership |
| [`lead-ai-transformation`](lead-ai-transformation/) | Enterprise AI transformation |
| [`learn-summit-2023-remote`](learn-summit-2023-remote/) | Summit 2023 remote talks |
| [`learn-summit-2023-talks`](learn-summit-2023-talks/) | Summit 2023 main stage |
| [`navigate-aie-europe-2026`](navigate-aie-europe-2026/) | AIE Europe 2026 keynotes |
| [`navigate-aiewf-2024-keynotes`](navigate-aiewf-2024-keynotes/) | AIEWF 2024 keynotes |
| [`observe-ai-production`](observe-ai-production/) | Arize / production observability |
| [`operate-agent-memory`](operate-agent-memory/) | Agent context & memory |
| [`operate-legal-ai-agents`](operate-legal-ai-agents/) | Legal AI beyond chat |
| [`operate-openclaw-agents`](operate-openclaw-agents/) | OpenClaw deploy & security |
| [`optimize-llm-inference`](optimize-llm-inference/) | GPU & inference |
| [`plan-sovereign-ai`](plan-sovereign-ai/) | Sovereign AI planning |
| [`price-ai-products`](price-ai-products/) | AI product pricing |
| [`run-aiewf-2024-evals`](run-aiewf-2024-evals/) | AIEWF 2024 evals & LLM ops |
| [`run-llm-evals`](run-llm-evals/) | LLM & agent evaluation |
| [`run-summit-2023-workshops`](run-summit-2023-workshops/) | Summit 2023 workshops |
| [`secure-ai-agents`](secure-ai-agents/) | Agent security & red team |
| [`ship-ai-as-pm`](ship-ai-as-pm/) | AI product management |
| [`ship-aiewf-2024-agents`](ship-aiewf-2024-agents/) | AIEWF 2024 agents |
| [`train-llms-locally`](train-llms-locally/) | Train LLM from scratch locally |
