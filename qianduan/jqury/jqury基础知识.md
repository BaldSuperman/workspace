#jquery
- jquery是一个函数库，一个js文件，页面用script标签引入这个js文件就可以使用
    -只需要 引入就可以使用
- jquery的加载：完整写法 $(document).ready(function(){ js代码}）等同于window.onload = function(){}
    简便写法   $(function(){})
- jquery获取对象 var $div = $('#div1');
- jquery选择器
    - $('#myId') 选择id为myId的网页元素
    - $('.myClass') 选择class为myClass的元素
    - $('li')  选择所有li元素
    - $('#ul1 li span) 选择id为ul1元素下的所有li下的span元素
    - $('input[name-first]') 选择name属性等于first的input元素
- 对选择集进行过滤
    - $('div').has('p') 选择包含p元素的div元素
    - $('div').not('.myClass') 选择class不等于myClass的div的元素
    - $('div').filter('.myClass') 选择class等于myClass的div元素
    - $('div').eq(5) 选择第6个div元素
- 选择集转移
    - $('div').prev() 选择div元素前面紧挨的同辈元素
    - $('div').prevAll() 选择div元素之前所有的同辈元素
    - $('div').next() 选择div元素后面紧挨的同辈元素
    - $('div').nextAll() 选择div元素后面所有的同辈元素
    - $('div').parent() 选择div的父类
    - $('div').children() 选择div的所有子类
    - $('div').siblings() 选择除了div的同级元素
    - $('div').find('.myClass') 选择div内的class等于myClass的元素
## jquery样式操作
- jquery用法思想二，同一个函数完成取值和赋值
- 操作行间样式
    - $('div').css('width') 取出div的width值
    - $('div').css('width':'300px') 给div的width赋值为300px
- 操作样式类名
    -$(this).prevAll().each(function())//对选中的每个元素进行操作
    - $('div').addClass('divClass2') 为id为div的兑现追加样式divClass2
    - $('div').removeClass('divClass') 移除id为div1的对象的class名为divClass的样式
    - $('div').removeClass('divClass2')  移除多个样式 
    - $('div').toggleClass('divClass2') 重复切换anotherClass样式
    - $('div').hasClass('divClass2') 检查当前div是否含有divClass2样式

- 绑定click事件
    - $('#btn1').click(function(){
        // 内部的this指的是原生对象
        
        //使用jquery对象用$(this),表示被单击的对象
        
    })
- 获取元素的索引值：使用index
    - $li.filter('.myli').index()
- jquery特殊效果
    - stop可以修复动画bug 
        $(this).next().stop().slideToggle()
    - 特殊效果都有参数
        - 例如 $('.box').fadeToggle(1000.'swing',function(){
            alert('done!');
        
         })
         其中 1000 是淡入淡出的时间 swing是运动的曲线 function()是回调函数
         
    - fadeIn() 淡入 一开始隐藏的东西
    - fadeOut() 淡出
    - fadeToggle() 切换淡入淡出
    - hide() 隐藏元素
    - show() 显示元素
    - toggle() 切换元素的可见状态
    - slideDown() 向下展开
    - slideUp() 向上卷起
    - slideToggle() 依次展开或卷起某个元素
- juqery的链式调用、
    - $('#div') //id为div1的元素
    .childreen('ul')//该元素下面的ul子元素
    .slideDown('fast') //高度从零变到实际高度来显示ul元素
    .parent()   //跳到ul的父元素，也就是id为div1的元素
    .siblings() //跳到div1元素平级的所有的兄弟元素
    .children('ul') //这些兄弟元素中的ul子元素
    .slideUp('fast');//高度实际高度变换到0来隐藏ul元素
- jquery动画
    - 
        $('#btn').click(function(){
            $('.box').animate({'width':'600px'},1000,function(){

                $('.box').animate({'height':'400px'})
            });

        })
     - 可以用表达式
     
            $('#btn2').click(function(){
             $('.box2').animate({'width':'+=100'})；
        })
- 获取和设置元素尺寸
    - width() height() 获取元素width和height
    - innerWidth() innerHeight() 包括padding的width和height
    - outerWidth() outerHeight() 包括padding和border的width和height
    - outerWidth(true) outerHeight(true) 包括padding和border以及margin的width和height
    - offset() 获取元素相对页面的绝对位置
- 读取标签里面内容
    - $count.html(); 读取$count对象标签里的内容
- 获取浏览器可视区宽度和高度
    - $(window).width()
    - $(window).height()
- 获取页面文档的宽度高度
    - $(document).width();
    - $(document).height();
- 获取页面滚动距离
    - $(document).scrollTop();
    - $(document).scrolLeft();
- 页面滚动事件
    - $(window).scroll(function(){
        ...........
    });
##jquery属性操作
- html()取出或设置html内容
    - var $htm = $('#div'),html();取出
    - $('#div'),html('<span>添加文字</span>')
- prop()取出或设置某个属性的值
    - var $src = $('#img1').prop('src');//取出图片地址
    - //设置图片的地址和alt属性 
      $('#img1').prop({src:'test.jpg',alt:'Test Image'}); 
- jquery循环
    - 对jquery选择的对象集合分别进行操作
        - $(function(){
            $('.listi li').each(function(){
                $(this).html(i)
            })   
        })   
## jquery 事件
- 事件函数列表：
    - blur 元素失去焦点
    - focus() 元素获得焦点
    - click()鼠标单击
    - mouseover() 鼠标进入(进入子子元素也出发)
    - mouseout()鼠标离开(离开子元素也触发)
    - mouseenter（）鼠标进入(进入子元素不触发)
    - mouseleave()鼠标离开（离开子元素不触发）
    - hover() 同时为mouseenter和mouseleaver事件指定处理函数
    - ready() Dom加载完成
    - resize() 浏览器窗口的大小发生改变//绑定在window上面
    - scroll() 滚动条的位置发生改变
    - submit() 用户递交表单
- 绑定事件的其他方法
    - $(function(){
        $('#div').bind('mouseover click', function(event){
            alert($(this).html()); 
        })
    })
 - 取消绑定事件
    - $(function(){
        $('#div').bind('mouseover click', function(event){
            alert($(this).html()); 
            
            //$(this).unbind()
            $(this).unbind('mouseover');
        })
    })
- 事件冒泡
    - 允许多个操作被集中处理（把事件处理添加到一个父级元素上，避免把世家你处理器添加到多个子级元素上），他还可以让你在对象层的不同级别捕获事件。
    - 事件冒泡机制有时候时不需要的，需要阻止掉，通过event.stopPropagation()来阻止
    - 一般直接使用return false来阻止
- 事件委托：可以提高性能，让新加入的子元素也可以拥有相同的操作
- jquery节点操作
    - 创建节点 var $div = $('<div>kkkkkk</div>')
                var $div = $('<div>')
    - 插入节点
        - append()和appendTo()在现存的元素内部，从后面加入元素
        - prepend()和prependTo()：在现存元素的内部，从前面插入元素
        - after()和insertAfter()：在现存元素的外部，从后面加入元素
        - before（）和insertBefore()在现存元素的外部，从前面插入元素
    - 删除节点 remove()
        $('#div1').remove();
- 滚轮事件与函数节流
    - 原生js中的鼠标滚轮事件不兼容，可以使用jquery的滚轮事件插件
    - jquery mousewheel.js
    - 函数节流：javascript中有些事件触发频率非常高，在短时间内多触发执行绑定函数，可以使用定时器减少触发的次数，实现函数节流
- 定时器
    - 创建定时器
    time = setInterval(function(){
        //定时器内部事件
        $nowli = $prevli+1;
          $(this).addClass('active').siblings().removeClass('active');
        move()
    },3000//时间) 
    - 移除定时器
          clearInterval(time);
- json 是一种数据格式,目前这种数据格式比较流行
    - javascript自定义对象：
        var oMan = {
            name:'tom',
            age:16,
            talk:function(s){
                alert('我会说');
            }
        }
        
        json格式数据
           {
            'name':'tom',
            'age':18
           }
        json的另一种数据格式是数组，和javascript中的数组字面量相同
        ['tom',18;"programer']
    
        