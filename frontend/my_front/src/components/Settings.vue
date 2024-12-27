<template>
    <div id="page1" class="page active">
        <h1 style="position: absolute;top: 30px;">参数设置</h1>
        <div class="user_name">
            <label 
                :class="['userNameTip', userNameTipClass]" 
                for="userName"
            >
                请输入您的用户ID(最高200)
            </label>
            <input 
                type="number" 
                id="userName" 
                v-model="userName" 
                @focus="handleUserNameFocus" 
                @blur="handleUserNameBlur"
                style="border-radius: 10px;height: 45px;"
            >
        </div>
        <div class="goods_number">
            <label 
                :class="['goodsNumberTip', goodsNumberTipClass]" 
                for="goodsNumber"
            >
                请输入您需要推荐商品的个数(最高100)
            </label>
            <input 
                type="number"
                id="goodsNumber" 
                v-model="goodsNumber" 
                @focus="handleGoodsNumberFocus" 
                @blur="handleGoodsNumberBlur"
                style="border-radius: 10px;height: 45px;"
            >
        </div>
        <button id="submitBtn" @click="handleClick" style=" z-index: 10;margin-top: 30px;margin-left: 0px; width: 100px;height: 50px;">提交</button>
    </div>
</template>

<script>
export default {
        data() {
        return {
            userName: '',
            goodsNumber: '',
            isUserNameFocused: false,
            isGoodsNumberFocused: false
        };
    },
    computed: {
        userNameTipClass() {
            return this.isUserNameFocused || this.userName
                ? 'userNameTipA'
                : '';
        },
        goodsNumberTipClass() {
            return this.isGoodsNumberFocused || this.goodsNumber
                ? 'goodsNumberTipA'
                : '';
        }
    },
    methods: {
        handleUserNameFocus() {
            this.isUserNameFocused = true;
            console.log("用户ID输入框获得焦点");
        },
        handleUserNameBlur() {
            this.isUserNameFocused = false;
            if (!this.userName) {
                // 当输入为空时移除提示类
                // 通过计算属性自动处理
            }
        },
        handleGoodsNumberFocus() {
            this.isGoodsNumberFocused = true;
            console.log("推荐商品个数输入框获得焦点");
        },
        handleGoodsNumberBlur() {
            this.isGoodsNumberFocused = false;
            if (!this.goodsNumber) {
                // 当输入为空时移除提示类
                // 通过计算属性自动处理
            }
        },
        handleClick(){
            // 提交按钮
            // 获取用户ID和商品个数
            let userId = this.userName;
            let n = this.goodsNumber;
            // 确保用户ID和商品个数都已填写
            // 确保用户ID和商品个数都已填写
            if (!userId || !goodsNumber) {
                    alert("请填写完整的用户ID和商品个数！");
                    return;
                }
            console.log("提交按钮被点击"+"用户ID："+userId+" 推荐商品个数："+n);
           this.$emit('submit',userId,n);
        },
    }
};
</script>

<style>
    .page{
        /* background-color: yellow; */
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .user_name {
        position: absolute;
        top: 200px;
        width: 400px;
        height: 50px;
        /* background-color: yellowgreen; */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .goods_number{
        /* margin-top: 50px; */
        position: absolute;
        top: 300px;
        width: 400px;
        height: 50px;
        /* background-color: aqua; */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    /* .user_name{
        width: 200px;
        height: 50px;
        position: absolute;
        top: 200px;
        left: 760px;
        font-size: 20px;
    }
    .goods_number{
        width: 200px;
        height: 50px;
        position: absolute;
        top: 300px;
        left: 760px;
        font-size: 20px;
    } */
    #userName{
        display: inline-block;
        width: 300px;
        height: 30px;
        color: orange;
        font-size: 20px;
        border: 0px transparent;
        border-bottom: 2px solid #fff;
        background-color: rgb(54, 54, 54);
    }
    #goodsNumber{
        display: inline-block;
        width: 300px;
        height: 30px;
        color: orange;
        font-size: 20px;
        border: 0px transparent;
        border-bottom: 2px solid #fff;
        background-color: rgb(54, 54, 54);
    }
    #userName:focus{
        outline: none;
        border-bottom: 2px solid orange;
    }
    #goodsNumber:focus{
        outline: none;
        border-bottom: 2px solid orange;
    }
    .userNameTip{        position: absolute;
        top: 13px;
        left: 55px;
        font-size: 15px;
        color: #fff;
        transition: all 0.1s linear;
    }
    .goodsNumberTip{
        position: absolute;
        top: 13px;
        left: 55px;
        font-size: 15px;
        color: #fff;
        transition: all 0.1s linear;
    }
    @keyframes user {
        from{
            top: 0px;
            font-size: 20px;
        }
        to{
            top: -20px;
            font-size: 12px;
            color: rgba(0, 0, 0, .9);    
        }
    }
    @keyframes goods {
        from{
            top: 0px;
            font-size: 20px;
        }
        to{
            top: -20px;
            font-size: 12px;
            color: rgba(0, 0, 0, .9);    
        }
    }
    .userNameTipA{
        animation: user 0.1s linear normal forwards;
        animation-iteration-count: 1;
    }
    .goodsNumberTipA{
        animation: goods 0.1s linear normal forwards;
        animation-iteration-count: 1;
    }
</style>
