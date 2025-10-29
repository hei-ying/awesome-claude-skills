---
name: pocketflow
description: PocketFlow - A 100-line minimalist LLM framework for building multi-agent systems, workflows, and RAG applications with zero dependencies
---

# Pocketflow Skill

Comprehensive assistance with pocketflow development, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with pocketflow
- Asking about pocketflow features or APIs
- Implementing pocketflow solutions
- Debugging pocketflow code
- Learning pocketflow best practices

## Quick Reference

### Common Patterns

**Pattern 1:** Agent received: System status: all systems operational | timestamp_0 Agent received: Memory usage: normal | timestamp_1 Agent received: Network connectivity: stable | timestamp_2 Agent received: Processing load: optimal | timestamp_3

```
Agent received: System status: all systems operational | timestamp_0
Agent received: Memory usage: normal | timestamp_1
Agent received: Network connectivity: stable | timestamp_2
Agent received: Processing load: optimal | timestamp_3
```

**Pattern 2:** Usage example:

```
shared = {
    "files": ["doc1.txt", "doc2.txt"],  # any text files
}
OfflineFlow.run(shared)
```

**Pattern 3:** Usage example:

```
# Suppose we already ran OfflineFlow and have:
# shared["all_chunks"], shared["index"], etc.
shared["question"] = "Why do people like cats?"

OnlineFlow.run(shared)
# final answer in shared["answer"]
```

### Example Code Patterns

**Example 1** (python):
```python
def fixed_size_chunk(text, chunk_size=100):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **agents.md** - Agents documentation
- **api.md** - Api documentation
- **other.md** - Other documentation
- **patterns.md** - Patterns documentation
- **rag.md** - Rag documentation
- **workflows.md** - Workflows documentation

Use `view` to read specific reference files when detailed information is needed.

## Working with This Skill

### For Beginners
Start with the getting_started or tutorials reference files for foundational concepts.

### For Specific Features
Use the appropriate category reference file (api, guides, etc.) for detailed information.

### For Code Examples
The quick reference section above contains common patterns extracted from the official docs.

## Resources

### references/
Organized documentation extracted from official sources. These files contain:
- Detailed explanations
- Code examples with language annotations
- Links to original documentation
- Table of contents for quick navigation

### scripts/
Add helper scripts here for common automation tasks.

### assets/
Add templates, boilerplate, or example projects here.

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information
