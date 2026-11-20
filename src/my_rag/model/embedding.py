from langchain_core.embeddings import Embeddings
from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model() -> Embeddings:
    embeddings = HuggingFaceEmbeddings(
        model_name = "IEITYuan/Yuan-embedding-2.0-en",
        # 数据截止于2026/11/16，在参数1B以下的模型之中，综合retrival, rerank以及STS分数，该模型表现最优
        model_kwargs = {'device' : 'cuda'},
        encode_kwargs = {'normalize_embeddings':True} # 归一化，后续直接算内积即可，加快响应
    )
    print('The embedding Model is loaded successfully') # 检验参数是否下载到GPU
    return embeddings
