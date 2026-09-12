# Vault V2

Vault V2 is an experimental personal knowledge system and digital garden built around Markdown, Obsidian-compatible notes, structured categorization, and static-site publishing.

The project explores how a personal knowledge base can evolve from a collection of notes into a more organized system for learning, research, and long-term knowledge retrieval.

The published site is powered by **Quartz**, while the knowledge structure, content organization, categorization rules, and experiments in AI-assisted note processing are developed separately within this repository.

## Purpose

Traditional note collections often become difficult to navigate as they grow.

Vault V2 explores a workflow where information can move through a structured process:

```text
Raw information
      ↓
Capture
      ↓
Categorization
      ↓
Structured Markdown
      ↓
Links and metadata
      ↓
Knowledge graph
      ↓
Searchable digital garden
```

The goal is to make knowledge easier to revisit, connect, and extend over time.

## Current Status

**Experimental knowledge-management system / active prototype.**

The current repository contains:

* Quartz-based digital garden infrastructure
* Markdown knowledge notes
* Obsidian-compatible internal links
* Topic-based categorization
* Frontmatter metadata
* Early AI-assisted note-processing rules
* Static-site generation and publishing infrastructure

The system is still being reorganized, and some older notes remain in broad single-file formats that will gradually be converted into smaller connected notes.

## Current Knowledge Areas

The vault currently includes material across areas such as:

* Computer science
* Programming
* Artificial intelligence
* Science
* Technology
* Finance and budgeting
* IoT
* Engineering

The taxonomy will continue to evolve as more knowledge is added.

## AI-Assisted Categorization

An experimental workflow is defined for processing incoming information and placing it into appropriate knowledge categories.

For example:

```text
Incoming note
     ↓
Topic analysis
     ↓
Category selection
     ↓
Nested path generation
     ↓
Markdown formatting
     ↓
Tags + metadata
```

Current categorization concepts include structures such as:

```text
content/
├── programming/
│   ├── python/
│   ├── c++/
│   └── javascript/
│
├── science/
│   ├── physics/
│   ├── chemistry/
│   └── biology/
│
├── agriculture-iot/
└── finance/
```

The intention is for automation to assist with organization while keeping the resulting knowledge readable and editable as ordinary Markdown.

## Repository Structure

```text
vault-v2/
├── content/          # Knowledge notes
├── docs/             # Documentation
├── quartz/           # Quartz publishing engine
├── public/           # Static assets
│
├── quartz.config.ts
├── quartz.layout.ts
├── CLAUDE.md         # Experimental note-processing instructions
├── package.json
└── README.md
```

The exact structure may evolve as the knowledge system is refined.

## Content Philosophy

Vault V2 follows several principles.

### Markdown First

Knowledge should remain readable without requiring a proprietary database or application.

Markdown makes notes:

* portable
* version-controlled
* searchable
* scriptable
* compatible with many tools

### Small Connected Notes

Large reference documents are useful during collection, but important concepts should gradually become smaller notes connected through links.

Instead of:

```text
one enormous AI document
```

the long-term structure should become closer to:

```text
Artificial Intelligence
├── Machine Learning
│   ├── Supervised Learning
│   ├── Regression
│   └── Classification
│
├── Neural Networks
│   ├── Activation Functions
│   ├── Backpropagation
│   └── Transformers
│
└── AI Engineering
    ├── Evaluation
    ├── RAG
    └── Agents
```

This creates a knowledge graph rather than only a document archive.

### Human-Readable Automation

Automation should help organize knowledge without making the vault dependent on the automation system itself.

Generated notes should therefore remain:

* understandable by humans
* editable manually
* valid Markdown
* independently usable

## Quartz

Vault V2 uses [Quartz](https://quartz.jzhao.xyz/) as its publishing engine.

Quartz provides the static-site generation and digital-garden infrastructure, including features such as:

* Markdown rendering
* backlinks
* graph navigation
* search
* tags
* Obsidian-compatible syntax
* static-site generation

Quartz itself is an open-source project maintained separately.

Vault V2 focuses on the knowledge architecture, content, automation experiments, and customized publishing workflow built on top of it.

## Development

The project currently requires Node.js 22 or newer.

Install dependencies:

```bash
npm install
```

Run the Quartz development server:

```bash
npx quartz build --serve
```

Run project checks:

```bash
npm run check
```

## Current Limitations

The vault is still undergoing structural refinement.

Current limitations include:

* some large monolithic notes
* inconsistent taxonomy between older and newer content
* incomplete homepage/navigation design
* experimental automation rules
* limited validation of automatically categorized notes
* remaining upstream Quartz metadata that needs customization

These are being addressed progressively rather than through a complete rewrite.

## Roadmap

### Phase 1 — Repository Cleanup

* Replace default Quartz branding
* Replace default homepage content
* Document the project accurately
* Preserve Quartz attribution
* Normalize repository metadata

### Phase 2 — Knowledge Structure

* Define stable taxonomy
* Split large notes into focused topics
* Improve links between related concepts
* Standardize frontmatter
* Introduce indexes / maps of content

### Phase 3 — Capture Workflow

Develop a reliable flow for:

```text
capture
→ classify
→ summarize
→ link
→ review
→ publish
```

### Phase 4 — Assisted Knowledge Processing

Experiment with AI-assisted:

* categorization
* tag suggestions
* summaries
* related-note discovery
* duplicate detection
* knowledge linking

AI-generated changes should remain reviewable rather than silently modifying the knowledge base.

### Phase 5 — Knowledge Intelligence

Longer-term experiments may include:

* semantic search
* embeddings
* knowledge graph extraction
* source tracking
* research workflows
* agent-assisted discovery

## Relationship to Future Systems

Vault V2 represents an earlier experiment in structured personal knowledge management.

Ideas learned from this project may inform future knowledge and agent systems, but Vault V2 remains preserved as its own implementation rather than being rewritten to represent later architectures.

## License and Attribution

The publishing infrastructure is based on the open-source Quartz project.

Quartz and its original components remain subject to their respective licensing and attribution requirements.

Content and custom knowledge-management experiments in this repository are maintained separately from the upstream Quartz project.
