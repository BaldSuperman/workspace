$(function(){
    //选中包裹幻灯片的盒子
    var $slide = $('.slide_con');
    //选中所有小圆点
    var $li = $('.slide li');
    //获取幻灯片个数
    var $len = $li.length;
    //选择小圆点容器
    var $points_con = $('.points');
    //要运动过来的幻灯片的索引值
    var $nowli = 0;
    //要离开的幻灯片的索引值
    var $prevli = 0;
    // 获取上一页，下一页
    var $next = $('.next');
    var $prev = $('.prev');
    //定时器
    var time=null;
    //防止暴力操作
    var ismove = false;
    //根据幻灯片个数动态创建小圆点
    for(var i=0;i<$len;i++){
        var $newli = $('<li>');
        //第一个小圆点含有'active'样式
        if(i==0){
            $newli.addClass('active');
        }
        $newli.appendTo($points_con);
    }
    //除去第一个，其他的都放到left：760
    $li.not(':first').css({left:760});
    //获取所有小圆点
    var $points = $('.points li');
    //小圆点被单击事件
    $points.click(function(){
        $nowli = $(this).index();
        //修复重复点击的bug
        if($nowli==$prevli){
            return;
        }
        $(this).addClass('active').siblings().removeClass('active');
        move()
    })
    //向前的按钮
    $prev.click(function(){
        if(ismove){
            return;
        }
        ismove = true;
        $nowli=$prevli-1;
        move();
        $points.eq($nowli).addClass('active').siblings().removeClass('active');


    })
    //向后的按钮
    $next.click(function(){
        if(ismove){
            return;
        }
        ismove = true;
        $nowli=$prevli+1;
        move();
        $points.eq($nowli).addClass('active').siblings().removeClass('active');


    })
    //开个定时器，用来设置幻灯片自己动
    time = setInterval(autoplay,3000);
    $slide.mouseenter(function(){
        clearInterval(time);
    });
     $slide.mouseleave(function(){
        time = setInterval(autoplay,3000);
     });
    function autoplay(){
        $nowli = $prevli+1;
        $points.eq($nowli).addClass('active').siblings().removeClass('active');
        move()
    }
    function move(){
        //第一种幻灯片往前
        if($nowli<0){
            $nowli=$len-1;
            $prevli = 0;
            $li.eq($nowli).css({"left":-760});
            $li.eq($nowli).animate({'left':0});
            $li.eq($prevli).animate({'left':760},function(){
                ismove =false;
            });
            $prevli = $nowli;
            return;
        }
         //最后一张幻灯片往后
        if($nowli>$len-1){
            $nowli=0;
            $prevli = $len-1;
            $li.eq($nowli).css({"left":760});
            $li.eq($nowli).animate({'left':0});
            $li.eq($prevli).animate({'left':-760},function(){
                ismove =false;
            });
            $prevli = $nowli;
            return;
        }

        if($nowli>$prevli){
            $li.eq($nowli).css({"left":760});
            $li.eq($nowli).animate({'left':0});
            $li.eq($prevli).animate({'left':-760},function(){
                ismove =false;
            });
            $prevli = $nowli;

        }
        else {
            $li.eq($nowli).css({"left":-760});
            $li.eq($nowli).animate({'left':0});
            $li.eq($prevli).animate({'left':760},function(){
                ismove =false;
            });
            $prevli = $nowli;
        }



    }

})