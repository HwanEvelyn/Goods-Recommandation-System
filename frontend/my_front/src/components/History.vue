<template>
    <div class="history-items">
    <h2 style="margin-top: 10px;height: 50px;">购物历史</h2>
    <div v-if="HistoryList.length > 0" class="items-list">
      <div v-for="item in HistoryList" :key="item.item_id" class="item">
        <img :src="item.pict_url" :alt="item.title" class="item-image" />
        <h3 class="item-title">{{ item.title }}</h3>
        <p class="item-number">购买数量: {{ item.count }}</p>
        <p class="item-id">商品ID: {{ item.item_id }}</p>
      </div>
    </div>
    <p v-else>该用户没有购买商品。</p>
  </div>
</template>

<script>
export default { 
    props: {
        HistoryList:{
            type:Array,
            default:() => [],
        }, 
    }
}
</script>
<style>
.history-items {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        /* background-color: yellowgreen; */
    }
    .item-id{
        position: absolute;
        margin-top: 30px;
        left: 1300px;
    }
    .item-number{
        position: absolute;
        margin-top: 30px;
        left: 1100px;
    }
</style>