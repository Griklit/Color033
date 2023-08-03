from typing import Callable


class Color033:
    COLOR_TABLE = {'black': ';30', 'red': ';31', 'green': ';32', 'yellow': ';33', 'blue': ';34', 'purple': ';35',
                   'aqua': ';36', 'white': ';37'}
    BACK_COLOR_TABLE = {'black': ';40', 'red': ';41', 'green': ';42', 'yellow': ';43', 'blue': ';44', 'purple': ';45',
                        'aqua': ';46', 'white': ';47'}

    def __init__(self, text: str = '', color: str | int = '', back_color: str | int = '', high_light: bool = False,
                 low_light=False, under_line: bool = False, twinkle: bool = False, inversion: bool = False,
                 blanking: bool = False, reset: bool = True):
        self.text = text
        self.start = '\033['
        if color:
            self.start += f';{color}' if isinstance(color, int) else self.COLOR_TABLE.get(color, '')
        if back_color:
            self.start += f';{back_color}' if isinstance(back_color, int) else self.BACK_COLOR_TABLE.get(back_color, '')
        if high_light:
            self.start += ';1'
        if low_light:
            self.start += ';2'
        if under_line:
            self.start += ';4'
        if twinkle:
            self.start += ';5'
        if inversion:
            self.start += ';7'
        if blanking:
            self.start += ';8'
        self.start += 'm'
        self.end = '\033[0m' if reset else ''

    @staticmethod
    def reset():
        print('\033[0m', end='', flush=True)

    def color_text(self, text: str) -> str | object:
        if not text.startswith('__') and text.endswith('__'):
            return f'{self.start}{text}{self.end}'
        elif text == '__info__':
            return f'{self.__repr__()}  {self.__str__()}'
        elif text == '__obj__':
            return self
        else:
            return f'{self.start}{text}{self.end}'

    def __str__(self) -> str:
        return f'{self.start}{self.text or "This is an example."}{self.end}'

    def __repr__(self) -> str:
        """
        不常用函数，优先牺牲时间
        @return: 类名、字体样式参数
        """
        reverse_table = {'0': 'reset', '1': 'high_light', '2': 'low_light', '4': 'under_line',
                         '5': 'twinkle', '7': 'inversion', '8': 'blanking'}
        reverse_color_table = {v: k for k, v in self.COLOR_TABLE.items()}
        reverse_back_color_table = {v: k for k, v in self.BACK_COLOR_TABLE.items()}
        tags = self.start[3:-1].split(';')
        tags.extend(self.end[2:-1].split(';'))
        d = {}
        for tag in tags:
            if name := reverse_table.get(tag):
                d[name] = True
            elif name := reverse_color_table.get(f';{tag}'):
                d['color'] = name
            else:
                d['back_color'] = reverse_back_color_table[f';{tag}']
        return "\033[0m<\033[34mclass \033[0m'\033[34;1mColor033\033[0m' " + \
            ', '.join([f'\033[31m{k}\033[0m=\033[36m{v}\033[0m' for k, v in d.items()]) + '\033[0m>'


def color033(color: str | int = '', back_color: str | int = '', high_light: bool = False, low_light=False,
             under_line: bool = False, twinkle: bool = False, inversion: bool = False, blanking: bool = False,
             reset: bool = True
             ) -> Callable[[str], str]:
    """
    返还一个方法，该方法可以将文字转换为设定的样式。此函数会创建一个Color033实例
    @param color: 文字颜色
    @param back_color: 背景颜色
    @param high_light: 高亮度显示
    @param low_light: 低亮度显示
    @param under_line: 下划线
    @param twinkle: 闪烁（无效）
    @param inversion: 反显
    @param blanking: 消隐（无效）
    @param reset: 是否在打印完成后重置颜色
    @return: src.color_text
    """
    return Color033(color=color, back_color=back_color, high_light=high_light, low_light=low_light,
                    under_line=under_line, twinkle=twinkle, inversion=inversion, blanking=blanking,
                    reset=reset).color_text
