#css文本设置
- 常用的应用文本的css样式
    - color 设置文字的颜色
    - font-size：设置字体的大小
    - font-family 设置文字的字体
    - font-style 设置字体是否倾斜 如：font-style：'normal'设置不倾斜,font-style:'italic'设置字体倾斜
    - font-weight 设置字体是否加粗 如 font-weight：bold 设置加粗 font-weight：normal设置不加粗
    - line-height 设置文字的行高，设置行高相当于在每行文字的上下同时加间距
    - font 同时设置文字的几个属性 书写顺序：font：是否加粗 字号/行高 如 font：normal 20px/40px 'Microsoft yahei'
    - text—decoration 设置文字的下划线 如 text-decoration：none 将文字的下划线去掉
    - text- text-indent:设置文字首行缩进
    - text-align：设置文字水平对齐方式，如text-align：center 设置文字水平居中
    - 设置圆 border-radius:14px;
    - 设置透明度： opacity:0.5;
#css颜色表示法
    -1 颜色名表示： 比如red
    - 2 rgb表示 比如：rgb（255，0，0）表示红色
    - 16进制数值表示 比如#f0000表示红色 可简写为#f00
# css选择器
    - id选择器：    
         #div1{
            color:#ffff00;
        }
    - 类选择器
         .green{
            color:#f6f8f0;
        }
    - 层次选择器:
        
#盒子模型
     /*边框*/

            /*border-top-color:#000;*/
           /* border-top-width:10px;*/
            /*实线：solid 虚线： dashed 点线：dotted*/
           /* border-top-style:solid;*/
           /*边框三局和成一句*/
            /*
            border-top:10px solid #000;
            border-left:10px dashed #f09092;
            border-right:10px dotted #fa0978;
            border-bottom:10px solid #000;
            */
            /*设置4个边的边框一样*/
            border:10px solid #000;

            /*设置单个方向的内边距*/
            /*
            padding-top:30px;
            padding-lef:40px;
            padding-right:80px;
            padding-bottom:100px;
            */
             /*设置所有的内边距,按顺时针方向设置 上 右 下 左*/
            /*padding:20px 80px 100px 40px;*/
            /*如果只有3个值 则左右用同一个值80*/
            /*padding:20px 80px 100px;*/
            /*如果只有2个值上下公用一个值，左右公用一个值*/
            /*padding:20px 80px;*/
            /*如果只有一个值，则公用一个值*/
            padding:20px;
            /*设置外间距 margin和padding用法一致*/
            margin-top:100px;
 