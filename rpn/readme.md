rpn.py
==
Description:
----
知道创宇_测试题

用Python写一个将中缀表达式转换为逆波兰表达式的程序，并用unittest模块为它配上单元测试
Usage:
----
run test:
`python rpn.py`

具体描述如下：

函数torpn()将一个合法的中缀表达式`infix expression`处理成后缀表达式`rpn/postfix expression`。函数postfix()则将一个合法的后缀表达式计算出最终结果。
函数假设输入格式及其逻辑均合法。其中torpn的输出可以作为postfix的输入
暂时支持的算术为：+，-，*，/，^,其中^表示指数运算。具体参见源代码
TODO
-----
参数验证，前缀表达式的转化及其计算

Links
----
 * [RPN](http://en.wikipedia.org/wiki/Reverse_Polish_notation)