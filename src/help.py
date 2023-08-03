from .default_style import warning, info, error, message
from . import color033, Color033


def print_help():
    my_style = color033(color='purple', back_color='aqua', under_line=True, high_light=True, inversion=True)  # 自定义样式
    print(my_style('This is my style!'))  # 打印套用自定义样式的文本
    print()
    print(error('This is a error example.'))  # 打印默认错误样式文本
    print(warning('This is a warning example.'))  # 打印默认警告样式文本
    print(info('This is a info example.'))  # 打印默认信息样式文本
    print(message('This is a message example.'))  # 打印默认消息样式文本
    print()
    print(Color033('This is a src example.', color='green', under_line=True))  # 不通过样式模板创建带样式文本
    print()
    print(Color033(color='blue', back_color='red', under_line=True).__repr__())  # 打印样式参数
    print(my_style('__info__'))  # 打印样式参数
    print(my_style('__obj__'))  # 获取自身对象
    print()
    colors = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'aqua', 'white', '']  # 全部颜色
    # 打印全部样式
    for back in colors:
        for under_line in [False, True]:
            for high_light in [False, True]:
                for color in colors:
                    print(Color033('A%b', color=color, back_color=back, high_light=high_light, under_line=under_line),
                          end='')
                print(end='' if high_light else '    ')
            print(end='    ')
        print()
    print()
    print('src:', color033.__doc__)  # 文档
