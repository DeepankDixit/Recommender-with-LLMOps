from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path:str, persist_dir:str="chroma_db"): #persist_dir is the path where vectorstore will get saved
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

    #let's create two more methods: one for building the vectorstore and one for loading the vectorstore if already created

    #To create a new vector store
    def build_and_save_vectorstore(self):
        loader = CSVLoader(
            file_path = self.csv_path,
            encoding = 'utf-8',
            metadata_columns = []
        )
        data = loader.load()

        splitter = CharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 0,
        )
        text = splitter.split_documents(data)

        db = Chroma.from_documents(
            documents = text,
            embedding = self.embedding,
            persist_directory = self.persist_dir
        )
        db.persist() #save vector store to local disk. It persists in the persist_directory

    #To load an existing vector store (obviously from persist directory)
    def load_vectorstore(self):
        return Chroma(
            persist_directory = self.persist_directory,
            embedding_function = self.embedding
        )