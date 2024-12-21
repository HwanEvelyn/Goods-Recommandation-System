# Goods-Recommandation-System
This is a e-commece system with goods recommdation algorithm.
## 设计

1. 用户冷启动\用户未登录：商品受欢迎度排序，也是通过下面对于大量用户行为分析得到的

2. 基于模型的用户购买历史相似度分析（基于用户的协同过滤）：

   - 模型训练：电商购物用户行为分析数据https://tianchi.aliyun.com/dataset/181615
   - https://tianchi.aliyun.com/dataset/140281
   - 基于商品的协同过滤

3. 三个表：goods、user、userBehavior

   - 商品数据：淘宝爬虫

   - 用户数据、用户行为数据随机生成

4. 完整的推荐流程包括召回和排序。召回是指从海量的待推荐候选集中，选取待推荐列表。排序是指对待推荐列表的每个Item与User的关联程度进行排序。
