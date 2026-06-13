# graphify (arch fork)

Fork of [safishamsi/graphify](https://github.com/safishamsi/graphify) — the AI coding assistant that turns any folder of code, docs, papers, images, or videos into a queryable knowledge graph.

## What is graphify?

Type `/graphify` in your AI coding assistant and it maps your entire project into a knowledge graph you can query instead of grepping through files. Works in Claude Code, Codex, Gemini CLI, Cursor, and many more.

## Why this fork?

This fork adds a **plugin system** that enables [graphify-arch](https://github.com/Celestios/graphify-arch) — an architecture enforcement plugin that:

- Defines layers, tiers, and dependency constraints in a JSON config
- Audits violations on every graphify run
- Provides semantic search and context compilation for AI agents

### Changes from upstream

- Plugin lifecycle hooks (`on_post_build`, `on_post_analyze`, `on_report`, `on_export`)
- Plugin CLI handler support (`graphify arch`, `graphify query --semantic`)
- Weight-aware clustering (edge weights for community detection)
- MCP resources for architecture reports (`graphify://arch-report`, `graphify://arch-json`)
- `graphify-arch` as optional `arch` extra dependency

## Installation

```bash
# With arch plugin
uv tool install --from "git+https://github.com/Celestios/graphify.git" "graphifyy[arch]"

# Without arch plugin (just the fork)
uv tool install --from "git+https://github.com/Celestios/graphify.git" graphifyy
```

## Upstream

Original: https://github.com/safishamsi/graphify
License: MIT
