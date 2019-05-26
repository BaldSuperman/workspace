# Xpath
- 在xml文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
- W3C网站
# xpath 开发工具
- 开源的xpath表达式编辑工具，XMLQuire
- Chrom插件：Xpath Helper
- Firefox插件：Xpath Checker
# 选取节点
- nodename:选取此节点的所有子节点
- /：从根节点开始选取
- //：选取节点，不考虑位置
- .:选取当前节点
- ..：选取当前节点的父节点
- @：选取属性
- xpath中一般按照路径进行查找，以下爱是路径表示方法
        school/teacher ：寻找任意school下的teacher系欸但
        //student:选取所有student的节点，不考虑位置
        student//age:选取school后代所有的节点
        //@other:选取other属性
        //age[@detail]:选取带有detail属性的age元素
- 位于-Predicates
- /School/Student[1]:选取school下面的第一个节点
- /School/Student[last()]:选取最后一个student节点
- /School/Student[position<3]：选取Student下面的前两个节点
- //Student[@score]:选取带有属性score的Student结点
- //Student[@score="99"] : 选取带有属性score且score+99的Student结点
- //Student[@score]/age:选取带有score属性的School节点下的age节点  

# Xpath的一下操作
- |:或者
    //Student[@score] | //Teacher：选取带有属性score的Student节点或者teacher节点
- 其余不常见xpath运算符包括+ - * /