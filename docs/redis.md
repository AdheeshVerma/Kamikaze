Redis is the preferred, fastest, and most feature-rich cache, data structure server, and document and vector query engine.

## Key use cases

Redis excels in various applications, including:

- **Caching:** Supports multiple eviction policies, key expiration, and hash-field expiration.
- **Distributed Session Store:** Offers flexible session data modeling (string, JSON, hash).
- **Data Structure Server:** Provides low-level data structures (strings, lists, sets, hashes, sorted sets, JSON, etc.) with high-level semantics (counters, queues, leaderboards, rate limiters) and supports transactions & scripting.
- **NoSQL Data Store:** Key-value, document, and time series data storage.
- **Search and Query Engine:** Indexing for hash/JSON documents, supporting vector search, full-text search, geospatial queries, ranking, and aggregations via Redis Query Engine.
- **Event Store & Message Broker:** Implements queues (lists), priority queues (sorted sets), event deduplication (sets), streams, and pub/sub with probabilistic stream processing capabilities.
- **Vector Store for GenAI:** Integrates with AI applications (e.g. LangGraph, mem0) for short-term memory, long-term memory, LLM response caching (semantic caching), and retrieval augmented generation (RAG).
- **Real-Time Analytics:** Powers personalization, recommendations, fraud detection, and risk assessment.

## Connecting to redis

Inorder to use redis in our package we just pointed our django core packages to use redis as our cache provider. Django by default offers caching and because of this we just need a client to point the internal cache system of django to redis client done by altering the settings.py.

Just docker compose up and you will be able to use redis as the cache.

### How to save to the cache

for our usecase what we will be doing is caching the url as the key and the response as the query, and give it a time to live of 24 hours how do that is in the following way.

```bash
from django.core import cache

cache.set("<key>","value")
```
