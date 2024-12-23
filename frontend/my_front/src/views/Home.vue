<template>
    <div class="container">
        <div class="sidebar-container">
            <Sidebar @page_clicked="handlePageClicked"/>
        </div>
        <div class="content-container">
            <!-- <h1 style="display: flex;align-items: center;justify-content: center;">Home</h1> -->
            <component :is="currentPage" v-if="currentPage" @submit="handleSubmit" :RecommendedList="RecommendedList"/>
        </div>
    </div>
    
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import Settings from '@/components/Settings.vue';
import Recommended from '@/components/Recommended.vue';
import { getRecommendGoods } from '@/api/api';
export default {
  components: {
    Sidebar,
    Settings,
    Recommended
  },
  data() {
    return {
        currentPage:null,
        RecommendedList:[],
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
      console.log("推荐商品列表:",this.RecommendedList);
      console.log("用户ID:",userId);
      console.log("推荐商品个数:",n);
  }
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
    width: 200px;
    background-color: #fff;
    border-right: 1px solid #eee;
}

.content-container {
    margin-left: 250px;
    margin-top: 50px;
    width: 80%;
    height: 100%;
    padding: 20px;
    /* background-color: rgba(0, 0, 0, .3); */
}
</style>