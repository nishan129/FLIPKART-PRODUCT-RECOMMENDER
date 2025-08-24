from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from flipkart.data_convertor import DataConvertor
from flipkart.config import Config

class DataIngestore:
    def __init__(self):
        self.embeddings = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vstore = AstraDBVectorStore(
            embedding=self.embeddings,
            collection_name="flipkart_database",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace = Config.ASTRA_DB_KEYSPACE
        )
        
    def ingest(self,load_existing=True):
        if load_existing == True:
            self.vstore
            
        docs = DataConvertor(file_path="data/flipkart_product_review.csv").convert_to_documents()
        
        self.vstore.add_documents(docs)
        
        return self.vstore

if __name__ == "__main__":
    ingestor = DataIngestore()
    ingestor.ingest()
    