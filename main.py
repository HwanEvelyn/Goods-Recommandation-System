from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from recommendation import hybrid_recommend  # 引入混合推荐系统函数（你提供的代码）
from starlette.middleware.cors import CORSMiddleware

# 允许指定的源进行跨域访问
origins = [
    "http://127.0.0.1:5173",  # 前端地址
    "http://localhost:5173",   # 如果前端用的是localhost，也可以添加
]

app = FastAPI(title="Hybrid Goods Recommendation System API")

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许访问的源
    allow_credentials=True,
    allow_methods=["*"],    # 允许所有的HTTP方法
    allow_headers=["*"],    # 允许所有的请求头
)

# 加载数据
most_popular = pd.read_excel('./data/most_popular.xlsx')
purchase_matrix = pd.read_excel('./data/purchase_matrix.xlsx', index_col='user_id')
product = pd.read_excel('./data/product.xlsx')
log = pd.read_excel('./data/processed_log.xlsx')

# 商品描述数据处理
product_descriptions = product[['item_id', 'title']].copy()
product_descriptions["title"].fillna("", inplace=True)
product_descriptions["title"] = product_descriptions["title"].astype(str)

# TF-IDF向量化
vectorizer = TfidfVectorizer()
X1 = vectorizer.fit_transform(product_descriptions["title"])

# K-means聚类
true_k = 10
kmeans = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=10, random_state=42)
product_descriptions['cluster'] = kmeans.fit_predict(X1)

# 将聚类标签合并到商品数据中
product = product.merge(product_descriptions[['item_id', 'cluster']], on='item_id')

# 训练SVD模型用于内容推荐
svd_content = TruncatedSVD(n_components=10, random_state=42)
svd_content.fit(X1)

# 定义请求体模型
class RecommendRequest(BaseModel):
    user_id: int  # 用户ID
    n: int = 10  # 推荐数量

class RecommendResponse(BaseModel):
    recommended_items: list  # 推荐的商品列表

class PurchaseHistoryRequest(BaseModel):
    user_id: int  # 用户ID

class PurchaseHistoryResponse(BaseModel):
    purchased_items: list  # 用户购买的商品列表
@app.post("/recommend", response_model=RecommendResponse)
def recommend(request: RecommendRequest):
    """
    基于混合推荐系统生成推荐商品
    参数：
        user_id: 用户ID
        n: 推荐商品数量
    返回：
        推荐商品列表（item_id, title, pict_url）
    """
    user_id = request.user_id
    n_recommend = request.n

    # 使用混合推荐系统
    recommended_items = hybrid_recommend(
        user_id=user_id,
        item_id=None,  # 可以选择传入特定商品ID进行商品间推荐
        purchase_matrix=purchase_matrix,
        product=product,
        vectorizer=vectorizer,
        kmeans_model=kmeans,
        svd_model=svd_content,
        n_recommend=n_recommend,
        weights=(0.4, 0.3, 0.2, 0.1)
    )

    # 获取推荐的商品详细信息
    recommended_products = product[product['item_id'].isin(recommended_items)].loc[:, ['item_id', 'title', 'pict_url']]

    # 将推荐的商品转化为字典格式
    recommended_list = recommended_products.to_dict(orient="records")

    return RecommendResponse(recommended_items=recommended_list)

@app.post("/history", response_model=PurchaseHistoryResponse)
def purchase_history(request: PurchaseHistoryRequest):
    """
    根据用户ID获取历史购物商品，包括商品的标题、图片URL、item_id和购买次数。
    参数：
        user_id: 用户ID
    返回：
        用户历史购买的商品列表
    """
    user_id = request.user_id

    # 根据用户ID从日志数据中筛选该用户的购买记录
    user_purchase_log = log[log['user_id'] == user_id]

    # 如果该用户没有购买记录，返回空列表
    if user_purchase_log.empty:
        raise HTTPException(status_code=200, detail="该用户没有历史购买记录")

    # 统计每个商品的购买次数
    purchase_counts = user_purchase_log.groupby('item_id').size().reset_index(name='count')

    # 合并商品详情（title, pict_url）
    purchase_details = purchase_counts.merge(product[['item_id', 'title', 'pict_url']], on='item_id', how='left')

    # 转换为字典格式
    purchased_items = purchase_details.to_dict(orient="records")

    return PurchaseHistoryResponse(purchased_items=purchased_items)


# 根路径访问
@app.get("/")
def read_root():
    return {"message": "欢迎使用混合推荐系统 API"}

