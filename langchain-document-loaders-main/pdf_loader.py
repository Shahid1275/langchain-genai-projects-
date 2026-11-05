import warnings

warnings.filterwarnings("ignore", message=".*langchain-community.*", category=DeprecationWarning)

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)