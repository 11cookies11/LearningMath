class Flags:
    FLAG_ATTACK = 0x01  # 0001
    FLAG_B = 0x02  # 0010
    FLAG_C = 0x04  # 0100
    FLAG_D = 0x08  # 1000

    # 你可以根据需要添加更多的标志位

    def __init__(self):
        self.flags = 0

    def set_flag(self, flag):
        self.flags |= flag

    def clear_flag(self, flag):
        self.flags &= ~flag

    def clear_all_flags(self):
        self.flags = 0x0

    def toggle_flag(self, flag):
        self.flags ^= flag

    def is_flag_set(self, flag):
        return self.flags & flag != 0

    # 使用示例

if __name__ == '__main__':
    flags = Flags()

    # 设置标志位
    flags.set_flag(Flags.FLAG_ATTACK)
    flags.set_flag(Flags.FLAG_C)

    # 检查标志位
    print(flags.is_flag_set(Flags.FLAG_ATTACK))  # 输出: True
    print(flags.is_flag_set(Flags.FLAG_B))  # 输出: False

    # 清除标志位
    flags.clear_flag(Flags.FLAG_ATTACK)

    # 再次检查标志位
    print(flags.is_flag_set(Flags.FLAG_ATTACK))  # 输出: False

