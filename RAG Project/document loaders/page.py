from langchain_community.document_loaders import WebBaseLoader
url="https://docs.blackbox.ai/features/vscode-agent/introduction"
data=WebBaseLoader(url)
docs=data.load()
print(docs[0].page_content)