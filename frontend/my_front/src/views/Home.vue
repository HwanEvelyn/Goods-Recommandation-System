<template>
    <div class="container">
        <div class="sidebar-container">
            <Sidebar @page_clicked="handlePageClicked"/>
        </div>
        <div class="content-container">
            <!-- <h1 style="display: flex;align-items: center;justify-content: center;">Home</h1> -->
            <component :is="currentPage" v-if="currentPage" @submit="handleSubmit" :RecommendedList="RecommendedList" :HistoryList="HistoryList"/>
        </div>
    </div>
    
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import Settings from '@/components/Settings.vue';
import Recommended from '@/components/Recommended.vue';
import History from '@/components/History.vue';
import { getRecommendGoods } from '@/api/api';
import { getHistoryGoods } from '../api/api';
export default {
  components: {
    Sidebar,
    Settings,
    Recommended,
    History,
  },
  data() {
    return {
        currentPage:null,
        RecommendedList:[],
        HistoryList: [],
    };
  },
  methods: {
    handlePageClicked(page) {
      console.log(page);
      this.currentPage = page;
    },
    handleSubmit(userId,n) {
      getRecommendGoods(userId,n).then(res=>{
        this.RecommendedList = res.recommended_items;
        console.log(res);
      })
      console.log("推荐商品列表:",this.RecommendedList.length);
      // console.log("用户ID:",userId);
      // console.log("推荐商品个数:",n);
      getHistoryGoods(userId).then(res=>{
        if (res.detail === "该用户没有历史购买记录") {
          this.HistoryList = [];
          console.log("该用户没有历史购买记录");
          // 可以在这里添加其他处理逻辑，比如显示提示信息给用户
        } else {
          this.HistoryList = res.purchased_items;
          console.log("购买历史商品列表:", this.HistoryList.length);
        }
        // this.HistoryList = res.purchased_items;
        // console.log("购买历史商品列表:",this.HistoryList.length);
        console.log(res);
      })
    },

  },
  
};
</script>

<style scoped>
.container{
    position: absolute;
    /* background-color: yellowgreen; */
    width: 100%;
    height: 100%;
}
.sidebar-container {
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    width: 13%;
    background-color: #fff;
    border-right: 1px solid #eee;
    /* background-color: violet; */
}

.content-container {
    margin-left: 200px;
    /* margin-top: 50px; */
    width: 87%;
    height: 100%;
    /* padding: 20px; */
    background-color:  #fff;
}
</style>