import chromadb
from chromadb.config import Settings

chroma_client = chromadb.HttpClient(host="chroma", port = 8000, settings=Settings(allow_reset=True, anonymized_telemetry=False))

collection_status = False
while collection_status != True:
    try:
        document_collection = chroma_client.get_or_create_collection(name="sample_collection")
        collection_status = True
    except Exception as e:
        pass

results = document_collection.query(query_texts="Tell me above the ancient city of Rome?", n_results=3)
result_documents = results["documents"][0]
for doc in result_documents:
    print(doc)