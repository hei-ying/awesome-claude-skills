# Pocketflow - Rag

**Pages:** 2

---

## Embedding

**URL:** https://the-pocket.github.io/PocketFlow/utility_function/embedding.html

**Contents:**
- Embedding
- Example Python Code
  - 1. OpenAI
  - 2. Azure OpenAI
  - 3. Google Vertex AI
  - 4. AWS Bedrock
  - 5. Cohere
  - 6. Hugging Face
  - 7. Jina

Below you will find an overview table of various text embedding APIs, along with example Python code.

Embedding is more a micro optimization, compared to the Flow Design.

It’s recommended to start with the most convenient one and optimize later.

**Examples:**

Example 1 (python):
```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")
response = client.embeddings.create(
    model="text-embedding-ada-002",
    input=text
)
    
# Extract the embedding vector from the response
embedding = response.data[0].embedding
embedding = np.array(embedding, dtype=np.float32)
print(embedding)
```

Example 2 (unknown):
```unknown
import openai

openai.api_type = "azure"
openai.api_base = "https://YOUR_RESOURCE_NAME.openai.azure.com"
openai.api_version = "2023-03-15-preview"
openai.api_key = "YOUR_AZURE_API_KEY"

resp = openai.Embedding.create(engine="ada-embedding", input="Hello world")
vec = resp["data"][0]["embedding"]
print(vec)
```

Example 3 (python):
```python
from vertexai.preview.language_models import TextEmbeddingModel
import vertexai

vertexai.init(project="YOUR_GCP_PROJECT_ID", location="us-central1")
model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")

emb = model.get_embeddings(["Hello world"])
print(emb[0])
```

Example 4 (unknown):
```unknown
import boto3, json

client = boto3.client("bedrock-runtime", region_name="us-east-1")
body = {"inputText": "Hello world"}
resp = client.invoke_model(modelId="amazon.titan-embed-text-v2:0", contentType="application/json", body=json.dumps(body))
resp_body = json.loads(resp["body"].read())
vec = resp_body["embedding"]
print(vec)
```

---

## RAG (Retrieval Augmented Generation)

**URL:** https://the-pocket.github.io/PocketFlow/design_pattern/rag.html

**Contents:**
- RAG (Retrieval Augmented Generation)
- Stage 1: Offline Indexing
- Stage 2: Online Query & Answer

For certain LLM tasks like answering questions, providing relevant context is essential. One common architecture is a two-stage RAG pipeline:

We create three Nodes:

**Examples:**

Example 1 (python):
```python
class ChunkDocs(BatchNode):
    def prep(self, shared):
        # A list of file paths in shared["files"]. We process each file.
        return shared["files"]

    def exec(self, filepath):
        # read file content. In real usage, do error handling.
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        # chunk by 100 chars each
        chunks = []
        size = 100
        for i in range(0, len(text), size):
            chunks.append(text[i : i + size])
        return chunks
    
    def post(self, shared, prep_res, exec_res_list):
        # exec_res_list is a list of chunk-lists, one per file.
        # flatten them all into a single list of chunks.
        all_chunks = []
        for chunk_list in exec_res_list:
            all_chunks.extend(chunk_list)
        shared["all_chunks"] = all_chunks

class EmbedDocs(BatchNode):
    def prep(self, shared):
        return shared["all_chunks"]

    def exec(self, chunk):
        return get_embedding(chunk)

    def post(self, shared, prep_res, exec_res_list):
        # Store the list of embeddings.
        shared["all_embeds"] = exec_res_list
        print(f"Total embeddings: {len(exec_res_list)}")

class StoreIndex(Node):
    def prep(self, shared):
        # We'll read all embeds from shared.
        return shared["all_embeds"]

    def exec(self, all_embeds):
        # Create a vector index (faiss or other DB in real usage).
        index = create_index(all_embeds)
        return index

    def post(self, shared, prep_res, index):
        shared["index"] = index

# Wire them in sequence
chunk_node = ChunkDocs()
embed_node = EmbedDocs()
store_node = StoreIndex()

chunk_node >> embed_node >> store_node

OfflineFlow = Flow(start=chunk_node)
```

Example 2 (unknown):
```unknown
shared = {
    "files": ["doc1.txt", "doc2.txt"],  # any text files
}
OfflineFlow.run(shared)
```

Example 3 (python):
```python
class EmbedQuery(Node):
    def prep(self, shared):
        return shared["question"]

    def exec(self, question):
        return get_embedding(question)

    def post(self, shared, prep_res, q_emb):
        shared["q_emb"] = q_emb

class RetrieveDocs(Node):
    def prep(self, shared):
        # We'll need the query embedding, plus the offline index/chunks
        return shared["q_emb"], shared["index"], shared["all_chunks"]

    def exec(self, inputs):
        q_emb, index, chunks = inputs
        I, D = search_index(index, q_emb, top_k=1)
        best_id = I[0][0]
        relevant_chunk = chunks[best_id]
        return relevant_chunk

    def post(self, shared, prep_res, relevant_chunk):
        shared["retrieved_chunk"] = relevant_chunk
        print("Retrieved chunk:", relevant_chunk[:60], "...")

class GenerateAnswer(Node):
    def prep(self, shared):
        return shared["question"], shared["retrieved_chunk"]

    def exec(self, inputs):
        question, chunk = inputs
        prompt = f"Question: {question}\nContext: {chunk}\nAnswer:"
        return call_llm(prompt)

    def post(self, shared, prep_res, answer):
        shared["answer"] = answer
        print("Answer:", answer)

embed_qnode = EmbedQuery()
retrieve_node = RetrieveDocs()
generate_node = GenerateAnswer()

embed_qnode >> retrieve_node >> generate_node
OnlineFlow = Flow(start=embed_qnode)
```

Example 4 (unknown):
```unknown
# Suppose we already ran OfflineFlow and have:
# shared["all_chunks"], shared["index"], etc.
shared["question"] = "Why do people like cats?"

OnlineFlow.run(shared)
# final answer in shared["answer"]
```

---
