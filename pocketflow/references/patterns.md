# Pocketflow - Patterns

**Pages:** 3

---

## Map Reduce

**URL:** https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html

**Contents:**
- Map Reduce
  - Example: Document Summarization

MapReduce is a design pattern suitable when you have either:

and there is a logical way to break the task into smaller, ideally independent parts.

You first break down the task using BatchNode in the map phase, followed by aggregation in the reduce phase.

Performance Tip: The example above works sequentially. You can speed up the map phase by running it in parallel. See (Advanced) Parallel for more details.

**Examples:**

Example 1 (python):
```python
class SummarizeAllFiles(BatchNode):
    def prep(self, shared):
        files_dict = shared["files"]  # e.g. 10 files
        return list(files_dict.items())  # [("file1.txt", "aaa..."), ("file2.txt", "bbb..."), ...]

    def exec(self, one_file):
        filename, file_content = one_file
        summary_text = call_llm(f"Summarize the following file:\n{file_content}")
        return (filename, summary_text)

    def post(self, shared, prep_res, exec_res_list):
        shared["file_summaries"] = dict(exec_res_list)

class CombineSummaries(Node):
    def prep(self, shared):
        return shared["file_summaries"]

    def exec(self, file_summaries):
        # format as: "File1: summary\nFile2: summary...\n"
        text_list = []
        for fname, summ in file_summaries.items():
            text_list.append(f"{fname} summary:\n{summ}\n")
        big_text = "\n---\n".join(text_list)

        return call_llm(f"Combine these file summaries into one final summary:\n{big_text}")

    def post(self, shared, prep_res, final_summary):
        shared["all_files_summary"] = final_summary

batch_node = SummarizeAllFiles()
combine_node = CombineSummaries()
batch_node >> combine_node

flow = Flow(start=batch_node)

shared = {
    "files": {
        "file1.txt": "Alice was beginning to get very tired of sitting by her sister...",
        "file2.txt": "Some other interesting text ...",
        # ...
    }
}
flow.run(shared)
print("Individual Summaries:", shared["file_summaries"])
print("\nFinal Summary:\n", shared["all_files_summary"])
```

---

## Pocket Flow

**URL:** https://the-pocket.github.io/PocketFlow/

**Contents:**
- Pocket Flow
- Core Abstraction
- Design Pattern
- Utility Function
- Ready to build your Apps?

A 100-line minimalist LLM framework for Agents, Task Decomposition, RAG, etc.

We model the LLM workflow as a Graph + Shared Store:

From there, it’s easy to implement popular design patterns:

We do not provide built-in utilities. Instead, we offer examples—please implement your own:

Why not built-in?: I believe it’s a bad practice for vendor-specific APIs in a general framework:

Check out Agentic Coding Guidance, the fastest way to develop LLM projects with Pocket Flow!

---

## Structured Output

**URL:** https://the-pocket.github.io/PocketFlow/design_pattern/structure.html

**Contents:**
- Structured Output
  - Example Use Cases
- Prompt Engineering
  - Example Text Summarization
  - Why YAML instead of JSON?

In many use cases, you may want the LLM to output a specific structure, such as a list or a dictionary with predefined keys.

There are several approaches to achieve a structured output:

In practice, Prompting is simple and reliable for modern LLMs.

When prompting the LLM to produce structured output:

Besides using assert statements, another popular way to validate schemas is Pydantic

Current LLMs struggle with escaping. YAML is easier with strings since they don’t always need quotes.

**Examples:**

Example 1 (unknown):
```unknown
product:
  name: Widget Pro
  price: 199.99
  description: |
    A high-quality widget designed for professionals.
    Recommended for advanced users.
```

Example 2 (unknown):
```unknown
summary:
  - This product is easy to use.
  - It is cost-effective.
  - Suitable for all skill levels.
```

Example 3 (unknown):
```unknown
server:
  host: 127.0.0.1
  port: 8080
  ssl: true
```

Example 4 (javascript):
```javascript
class SummarizeNode(Node):
    def exec(self, prep_res):
        # Suppose `prep_res` is the text to summarize.
        prompt = f"""
Please summarize the following text as YAML, with exactly 3 bullet points

{prep_res}

Now, output:
```yaml
summary:
  - bullet 1
  - bullet 2
  - bullet 3
```"""
        response = call_llm(prompt)
        yaml_str = response.split("```yaml")[1].split("```")[0].strip()

        import yaml
        structured_result = yaml.safe_load(yaml_str)

        assert "summary" in structured_result
        assert isinstance(structured_result["summary"], list)

        return structured_result
```

---
