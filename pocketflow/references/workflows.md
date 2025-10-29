# Pocketflow - Workflows

**Pages:** 1

---

## Workflow

**URL:** https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html

**Contents:**
- Workflow
  - Example: Article Writing

Many real-world tasks are too complex for one LLM call. The solution is to Task Decomposition: decompose them into a chain of multiple Nodes.

You usually need multiple iterations to find the sweet spot. If the task has too many edge cases, consider using Agents.

For dynamic cases, consider using Agents.

**Examples:**

Example 1 (python):
```python
class GenerateOutline(Node):
    def prep(self, shared): return shared["topic"]
    def exec(self, topic): return call_llm(f"Create a detailed outline for an article about {topic}")
    def post(self, shared, prep_res, exec_res): shared["outline"] = exec_res

class WriteSection(Node):
    def prep(self, shared): return shared["outline"]
    def exec(self, outline): return call_llm(f"Write content based on this outline: {outline}")
    def post(self, shared, prep_res, exec_res): shared["draft"] = exec_res

class ReviewAndRefine(Node):
    def prep(self, shared): return shared["draft"]
    def exec(self, draft): return call_llm(f"Review and improve this draft: {draft}")
    def post(self, shared, prep_res, exec_res): shared["final_article"] = exec_res

# Connect nodes
outline = GenerateOutline()
write = WriteSection()
review = ReviewAndRefine()

outline >> write >> review

# Create and run flow
writing_flow = Flow(start=outline)
shared = {"topic": "AI Safety"}
writing_flow.run(shared)
```

---
