// 引入axios
import axios from 'axios';

//请求推荐商品
export const getRecommendGoods = (userId,n) => {
    const data = {
        user_id: userId,
        n: n
    };

    return axios.post('http://localhost:8000/recommend', data)
    .then(response => {
        alert("推荐商品请求成功！");
        return response.data;
    })
    .catch(error => {
        console.error(error);
    });
    
}
export const getHistoryGoods = (userId) => {
    const data = {
        user_id: userId,
    };
    return axios.post('http://localhost:8000/history', data)
    .then(response => {
        alert("用户购买历史请求成功！");
        return response.data;
    })
    .catch(error => {
        console.error(error);
    });
}