# 面试题1 功能代码
import random

# 游戏ID储存列表
name_list = []


# 创建游戏ID
def game_test():
    # 随机生成用户名
    rd = random.sample('ABCDEFGHJIKLMNOPQRSTUVWXYZ', 2)
    part1 = ''.join(rd)
    part2 = '%04d' % random.randint(0, 9999)
    username = part1 + part2
    # 判断用户ID是否重复
    if username in name_list:
        return None
    else:
        # 将生成的游戏ID添加到游戏ID储存列表中，并返回数据
        name_list.append(username)
        return username


def start():
    while True:
        result = game_test()
        if result is None:
            continue
        else:
            return result

if __name__ == '__main__':
        res = start()
        print(res)






