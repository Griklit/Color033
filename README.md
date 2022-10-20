# Color033

通过`\033`字符实现彩色文字样式打印，并提供了默认样式可供参考使用，仅适用于支持`\033`的IDE使用。

```python
from color033.default_style import warning, info, error, message
from color033 import color033, Color033

my_style = color033(color='purple', back_color='aqua', under_line=True, high_light=True, inversion=True)  # 自定义样式
print(my_style('This is my style!'))  # 打印套用自定义样式的文本
print()
print(error('This is a error example.'))  # 打印默认错误样式文本
print(warning('This is a warning example.'))  # 打印默认警告样式文本
print(info('This is a info example.'))  # 打印默认信息样式文本
print(message('This is a message example.'))  # 打印默认消息样式文本
print()
print(Color033('This is a Color033 example.', color='green', under_line=True))  # 不通过样式模板创建带样式文本
print()
print(Color033(color='blue', back_color='red', under_line=True).__repr__())  # 打印样式参数
print(my_style('__info__'))  # 打印样式参数
print(my_style('__obj__'))  # 获取自身对象
print()
COLORS = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'aqua', 'white', '']  # 全部颜色
# 打印全部样式
for back in COLORS:
    for under_line in [False, True]:
        for high_light in [False, True]:
            for color in COLORS:
                print(Color033('A%b', color=color, back_color=back, high_light=high_light, under_line=under_line),
                      end='')
            print(end='' if high_light else '    ')
        print(end='    ')
    print()
print()
print('color033:', color033.__doc__)  # 文档

```

![image](/example.png)
***创建样式后使用样式打印字符串比频繁创建新样式字符串可以节省大量时间与内存开销。***

(虽然一共也没有多少开销罢了)