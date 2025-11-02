---
name: nacos
description: Nacos dynamic service discovery, configuration management, and service management platform. Use for microservices registration, configuration center, service discovery, and distributed systems.
---

# Nacos Skill

Comprehensive assistance with nacos development, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with nacos
- Asking about nacos features or APIs
- Implementing nacos solutions
- Debugging nacos code
- Learning nacos best practices

## Quick Reference

### Common Patterns

**Pattern 1:** When customizing the key, it is recommended to set the configuration item to a Base64 encoded string, and the length of the original key must not be less than 32 characters. For example the following example:

```
### The default token(Base64 String):
nacos.core.auth.default.token.secret.key=VGhpc0lzTXlDdXN0b21TZWNyZXRLZXkwMTIzNDU2Nzg=
```

### Example Code Patterns

**Example 1** (bash):
```bash
unzip nacos-source.zip
cd nacos/
mvn -Prelease-nacos clean install -U  
cd nacos/distribution/target/nacos-server-1.3.0/nacos/bin
```

**Example 2** (bash):
```bash
unzip nacos-server-1.3.0.zip or tar -xvf nacos-server-1.3.0.tar.gz
  cd nacos/bin
```

**Example 3** (bash):
```bash
unzip nacos-server-$version.zip  OR tar -xvf nacos-server-$version.tar.gz
  cd nacos/bin
```

**Example 4** (bash):
```bash
unzip nacos-server-$version.zip  OR tar -xvf nacos-server-$version.tar.gz
  cd nacos/bin
```

**Example 5** (java):
```java
### If turn on auth system:
nacos.core.auth.enabled=false
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **administration.md** - Administration documentation
- **api.md** - Api documentation
- **architecture.md** - Architecture documentation
- **community.md** - Community documentation
- **configuration.md** - Configuration documentation
- **deployment.md** - Deployment documentation
- **getting_started.md** - Getting Started documentation
- **integration.md** - Integration documentation
- **other.md** - Other documentation
- **service_discovery.md** - Service Discovery documentation

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
