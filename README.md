# Goods-Recommandation-System
This is a e-commece system with goods recommdation algorithm.
## 设计

1. 用户冷启动\用户未登录：商品受欢迎度排序，也是通过下面对于大量用户行为分析得到的

2. 基于模型的用户购买历史相似度分析（基于用户的协同过滤）：

   - 模型训练：电商购物用户行为分析数据https://tianchi.aliyun.com/dataset/181615
   - 基于商品的协同过滤

3. 三个表：goods、user、userBehavior
30个user、500个商品、300条购买记录
   - 商品数据、用户行为数据：https://tianchi.aliyun.com/dataset/140281
   - 用户数据、用户行为数据随机生成

4. 完整的推荐流程包括召回和排序。召回是指从海量的待推荐候选集中，选取待推荐列表。排序是指对待推荐列表的每个Item与User的关联程度进行排序。

## 实现
商品数据、用户行为数据：https://tianchi.aliyun.com/dataset/140281
1. **用户冷启动 / 未登录推荐**
    - 对商品受欢迎程度进行排序
    - 获取最受欢迎的商品列表
2. **基于协同过滤的推荐（Collaborative Filtering Recommendation）**

    - 使用奇异值分解（SVD）对商品购买矩阵进行降维。
    - 计算商品之间的余弦相似度。
    - 根据相似度为目标商品推荐最相似的商品。

3. **基于K-means聚类的推荐（Clustering-Based Recommendation）**

    - 使用TF-IDF向量化商品描述，并通过K-means对商品进行聚类。
    - 为每个商品分配一个簇标签。
    - 基于目标商品所属的簇，推荐同簇内的其他商品。

4. **基于内容的推荐（Content-Based Recommendation）**

    - 使用TF-IDF和SVD对商品描述进行降维和相似度计算。
    - 根据商品描述的相似度推荐相关商品。

5. **混合推荐系统（Hybrid Recommendation System）**

    - 分别调用上述四种推荐方法，获取各自的推荐列表。
    - 为每种推荐方法分配一个权重（`weights`），反映其在最终推荐中的重要性。这里设置为协同过滤40%、聚类30%、内容推荐20%、受欢迎度10%。
    - 通过加权累加各推荐方法的推荐结果，生成一个综合评分。
    - 根据综合评分对推荐商品进行排序，选取前N个作为最终推荐结果。
## 后端部署

在后端根目录下命令行运行：

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 前端采用VUE框架

- 参数设置界面：

![屏幕截图 2024-12-23 165706](https://github.com/user-attachments/assets/ae1157aa-ff8c-4bfb-8d42-b000be34c7c7)

- 推荐商品界面：

![image](https://github.com/user-attachments/assets/7bfd02af-ad50-4972-a1c3-cbeeb8b14857)


