function $(id) {return document.getElementById(id)}

function show(obj){ obj.style.display = 'block'}

function hide(obj){ obj.style.display = 'none'}
// 封装单个属性运动框架
function animate_0(obj,attr,target){
        clearInterval(obj.timer);
        obj.timer = setInterval(function (){
        	var current = parseInt(getStyle(obj,attr));
            var step = (target - current)/10;
            step = step > 0 ? Math.ceil(step) : Math.floor(step);
            obj.style[attr] =  current + step + "px";
            if(current == target){
                clearInterval(obj.timer);
            }
        },30)
    }
// 多属性运动框架含（回调函数,透明度）
function animate_json(obj,json,fn){
        clearInterval(obj.timer);
        obj.timer = setInterval(function (){
        	var flag = true;
        	for (var attr in json){
        		var current = 0;
        		if (attr =="opacity") {
        			current = Math.round(parseInt(getStyle(obj,attr)*100)) || 0;
        		} else {
        			current = parseInt(getStyle(obj,attr));
        		}
        		
        		var step = (json[attr] - current)/10;
        		step = step > 0 ? Math.ceil(step) : Math.floor(step);
        		// 添加透明度
        		if (attr == "opacity") {
        			if ("opacity" in obj.style) {
        				obj.style.opacity = (current + step)/100;
        			}
        			else{
        				obj.style.filter = "alpha(opacity = "+(current + step)*100+")"
        			}
        		}
        		else if (attr == "zIndex") {
        			obj.style.zIndex = json[attr];
        		}
        		else{
		            obj.style[attr] =  current + step + "px";

        		}
	            if(current != json[attr]){
	            	flag = false;
        		}

            }
            while (flag) {
				clearInterval(obj.timer);
				// 添加回调函数
				if (fn) {
					fn();
				}
            }	
        },30)
    }

// 返回样式的函数
function getStyle (obj,attr){
	if (obj.cuurentStyle) {
		return obj.currentStyle[attr];
	}
	else {
		return window.getComputedStyle(obj, null)[attr];
	}
}
// 获取可视区域宽度
function client(){
	if (window.innerWidth !=null) {
		return {
			width = window.innerWidth,
			height = window.innerHeight
		}
	}
	else if (document.compatMode=="CSS1Copat") {
		return {
			width:document.documentElement.clientWidth,
			height:document.documentElement.clientHeight
		}
	}
	return {
		width:document.body.clientWidth,
		height:document.body.clientHeight
	}
}
// 滚动
function scroll(){
	if (window.pageYOffset != null) {
			return{
				left: window.pageXOffset,
				top: window.pageYOffset
			}
		}
		//判断是否是怪异模式浏览器--就是没有<!DCUTYPE html>
		else if (document.compatMode =="CSS1Copat") //声明了DTD
		{
			return{
				left: document.documentElement.scrollLeft,
				top: document.documentElement.scrollTop
			}
		}
		return{
			left: document.body.scrollLeft,
			top: docment.body.scrollTop
		}
}

function tab(odj){
	var terget =document.getElementById(odj);
	var spans =terget.getElementsByTagName("span");
	var lis =terget.getElementsByTagName("li");
	for(var i=0;i<spans.length;i++){
		spans[i].index=i;
		spans[i].onmouseover=function(){
			for(var j=0;j<spans.length;j++){
				spans[j].className="";
				lis[j].style.display="none";
			}
				this.className="current";
				lis[this.index].style.display="block";
		}
	}
}
//封装getClass类
function getClass(classname){
	if(document.getElementsByClassName)
	{
		return document.getElementsByClassName(classname);
	}
	var arr = [];
	var dom = document.getElementsByTagName("*");
	for (var i = 0; i <dom.length; i++)
	{	
		var txtarr = dom[i].className.split(" ");
		for (var j = 0; j < txtarr.length; j++) {
			if(txtarr[j] == classname)
			{
				arr.push(dom[j]);
			}
		}
		
	}
	return arr;
}

function getClass(classname,id){
	if(document.getElementsByClassName)
	{
		if(id)
		{
			var getId = document.getElementById(id);
			return getId.getElementsByClassName(classname);
		}else {
			return document.getElementsByClassName(classname);
		}
	}
	
	if(id){
		var getId = document.getElementById(id);
		var dom = getId.getElementsByTagName("*");
	}else {
		var dom = document.getElementsByTagName("*");
	}
	var arr = [];
	for (var i = 0; i < dom.length; i++) {
		var txtarr = dom[i].className.split(" ");
		for (var j = 0; j < txtarr.length; j++) {
			if(txtarr[j] == classname)
			{
				arr.push(dom[j]);
			}
		}
	}
	return arr;
}
//封装的$类

// function $(str) {
// 	var s = str.charAt(0);
// 	var ss = str.substr(1);
// 	switch (s) {
// 		case "#":
// 			return document.getElementById(ss)
// 			break;
// 		case ".":
// 			return getClass(ss);
// 			break;
// 		default:
// 			return document.getElementsByTagName(str);
// 			break;
// 	}
// }
