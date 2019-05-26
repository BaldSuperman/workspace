#结构化文件存储
- xml,json
- 为了解决不同设备之间的信息交换
- xml
- json
# XML文件
- 参考：上网
- XML(extensibieMarkupLanguage) 可扩展的标记语言
    - 标记语言：语言中使用尖括号括起来的文本字符串标记
    - 可扩展： 用户可以自己定义需要的标记
    -例如：
            <Teacher>
                自定义的标记Teacher
                在两个标记之间任何内容都因该和Teacher相关
            </Teacher>
    - 是W3C组织制定的一个标准
    - XML描述的是数据本身，即数据的结构和予以
    - HTML则侧重于如何显示WEB页面的数据
- XML文件的构成
    - 处理指令 （可以认为一个文件只有一个处理指令）
        - 最多只有一行
        - 必须在第一行
        - 内容是与xml本身处理相关的声明或者指令
        - 以xml关键字开头
            - version属性是必须的
            - encoding 属性可以选择   
    - 根元素（一个文件内容只有一个根元素）
        - 在xml文件中可以看成一个树形结构
        - xml文件有且只有一个跟
    - 子元素
    - 属性
    - 内容
        - 表明标签所存储的信息
    - 注释
        - 起说明作用的信息
        - 注释只能其说明作用
        - 注释不能嵌套在标签里
        - --只有在注释的开头和结尾使用
        - ---只能出现在开头
- 保留字符的处理
    - XML中使用的符号可能会与实际符号冲突
    - 使用实体引用（EntityReference）来表示保留字符
        - 例 5 >6 不能使用> 使用5&gt;6
    - 把含有保留字符的部分放在CDATA块内容中,CDATA把内容信息视为不需要转义
        <![CDATA[
            内容
         ]]>
    - 需要转义的保留字符对应的实体引用：
        - & ：&amp
        - < :&lt
        - > :&gt
        - ' :&apos
        - " :&quot
- XML标签的命名规则
    - Passcal命名法
    - 用单词表示， 第一个字母大写
    - 大小写严格区分
    - 配对的标签必须一致
- 命名空间
    - 为了防止命名冲突
        <Student  > 
            <Name>hahhah</Name>
            <age>18</age>
        </Student>
        <Room>
            <Name>204 </Name>
            
        </Room>
    - 为了归并以上内容，可能会产生冲突
        <Student  > 
            <Name>hahhah</Name>
            <age>18</age>
            <Name>204 </Name>
        </Student>
    - 为了避免冲突，需要给可能产生冲突的元素添加命名空间
    - XMLNS xml name space的缩写
        <Student xmlns:student="http://my_student" xmlns:room="http://my_room" > 
            <student:Name>hahhah</student:Name>
            <age>18</age>
            <room:Name>204 </room:Name>
        </Student>
# XML访问

## 读取
- XML读取分两个主要技术，SAX,DOM
- SAX（simple API for XML）
    - 基于事件驱动
    - 利用SAX解析文档设计到解析器和事件处理两个部分
    - 特点：
        - 快
        - 流式读取
- DOM
    - 是W3C规定的XML编程接口
    - 一个XML文件在缓存中以树形结构保存 
    - 用途
        - 定位XML文件任意一个节点的位置
        - 添加删除相应内容
    - minidom
        - xml.minidom.parse(filename):加载读取的XML文件，filename也可以是xml代码
        - doc.documentElement:获取xml文档对象，一个xml文件只有一个对应的文档对象
        - node.getAttribute(attr_name):获取xml结点的属性值
        - node。getElementByTagName（tage_name)得到一个节点对象的集合
        - node.childNodes:得到所有孩子节点
        - node.childNodes[index].nodevalue:获取单个节点
        - node.firstNode:得到第一个节点，等价于nodechiildNodes[0]
        - node.attributes[tage_name] :得到节点的所有属性
    - etree
        - 以树形结构表示XML
        - xm.etree.parse(filename):加载读取的XML文件
        - root.getiterator:得到相应的可迭代的node集合
        - root.iter
        - find(node_name):查找指定node_name的节点，返回一个node
        - root.findall(node_name):返回多个node_name的节点
        - node.tag:node对应的tagename(节点名字)
        - node.text:node的文本值(设置node的文本内容)
        - node.attrib: 是node的属性的字典类型的内容  (设置node的属性)
- xml文件的写入
    - 更改
        - ele.set:修改属性
        - ele.append:追加一个子元素
        - ele.remove:删除子元素
    - 生成创建
        - Elemnet(name):生成一个name名字的属性的xml
        - subElement(par_name,cild_name):给par_name生成一个叫cild_name的子元素
        - dump:存入
    
        - minidom 写入
        -etree 写入
        - _setroot(node):设置为根节点
             