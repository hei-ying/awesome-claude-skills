---
name: liteflow
description: Use this skill when working with LiteFlow, a lightweight rule engine and orchestration framework for Java. Provides guidance on rule configuration, component development, orchestration patterns, and integration with Spring Boot.
---

# Liteflow Skill

Comprehensive assistance with liteflow development, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with liteflow
- Asking about liteflow features or APIs
- Implementing liteflow solutions
- Debugging liteflow code
- Learning liteflow best practices

## Quick Reference

### Common Patterns

*Quick reference patterns will be added as you use the skill.*

### Example Code Patterns

**Example 1** (properties):
```properties
liteflow.fast-load=false
```

**Example 2** (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-apollo</artifactId>
    <version>2.15.1</version>
</dependency>
```

**Example 3** (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    chainNamespace: chainConfig
    scriptNamespace: scriptConfig
```

**Example 4** (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-etcd</artifactId>
    <version>2.15.1</version>
</dependency>
```

**Example 5** (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    endpoints: http://127.0.0.1:2379
    chainPath: /liteflow/chain
    scriptPath: /liteflow/script
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **components.md** - Components documentation
- **configuration.md** - Configuration documentation
- **getting_started.md** - Getting Started documentation
- **orchestration.md** - Orchestration documentation

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
