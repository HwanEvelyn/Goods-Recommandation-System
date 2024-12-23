<style>
        * {
            margin: 0;
            padding: 0;
        }
 
        .sidebar {
            position: relative;
            width: 1200px;
            height: 900px;
            /* margin: 50px auto; */
            color: #ffffff;
        }
 
        .sidebar ul {
            width: 200px;
            height: 100%;
            background-color: rgba(0, 0, 0, .3);
        }
 
        .sidebar ul li {
            list-style: none;
            height: 50px;
            padding: 10px 0;
            transition: all .5s;
        }
 
        .sidebar ul li p {
            float: left;
            margin-left: 50px;
        }
 
        .sidebar ul li span {
            float: right;
            margin-right: 20px;
        }
 
        .sidebar ul li:hover {
            background-color: orange;
            padding-left: 20px;
            cursor: pointer;
        }
 
        .sidebar ul li:hover .sidebar-mask {
            display: block;
        }
 
 
    </style>

    <template>
        <div class="sidebar">
            <ul>
                <li>
                    <h4 style="text-align: center;">侧边栏</h4>
                </li>
                <li @click="handleClick('Settings')">
                    <p>参数设置</p>
                    <span>></span>
                </li>
                <li @click="handleClick('Recommended')">
                    <p>商品推荐</p>
                    <span>></span>
                </li>
                <li @click="handleClick('page3')">
                    <p>用户购买记录</p>
                    <span>></span>

                </li>
            </ul>
        </div>
    </template>

    <script>
        export default {
            methods: {
                handleClick(page) {
                    this.page = page
                    this.$emit('page_clicked',page)
                }
            }
        }
    </script>