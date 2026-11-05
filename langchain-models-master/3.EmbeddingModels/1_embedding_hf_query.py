from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

result = embedding.embed_query("Islamabad is the capital of Pakistan")

print(str(result))
