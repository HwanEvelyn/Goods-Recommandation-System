<template>
     <div class="recommended-items">
    <h2>推荐商品</h2>
    <div v-if="RecommendedList.length > 0" class="items-list">
      <div v-for="item in RecommendedList" :key="item.item_id" class="item">
        <img :src="item.pict_url" :alt="item.title" class="item-image" />
        <h3 class="item-title">{{ item.title }}</h3>
        <p class="item-id">商品ID: {{ item.item_id }}</p>
      </div>
    </div>
    <p v-else>暂无推荐商品。</p>
  </div>
</template>
<style>
    .recommended-items {
        display: flex;
        flex-direction: column;
    }
    .items-list {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .item{
        display: flex;
        padding: 10px;
    }
    .item-image{
        width: 100px;
        height: 100px;
        border-radius: 15px;
        border: 2px solid #ccc;
    }
    .item-title{
        margin-left: 50px;
        margin-top: 20px;
        width: 50%;
    }
    .item-id{
        margin-left: 50px;
        margin-top: 20px;
    }
</style>

<script>
export default {
    props: {
        RecommendedList:{
            type:Array,
            default:() => [],
        }, 
  },
}
</script>