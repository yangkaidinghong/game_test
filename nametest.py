# 面试题2 测试代码
import re
import game_test


class NameTest(object):
    def __init__(self):
        pass

    def checkname(self, name):
        if len(name) != 6:
            return '不符合规定'
        else:
            return name

    def matchname(self, name):
        name = self.checkname(name)
        res = re.match(r'[A-Z]{2}[0-9]{4}', name)
        if res:
            return '符合规定的名字'
        else:
            return '名字格式错误'


if __name__ == '__main__':
    nametest = NameTest()
    name = game_test.start()
    res = nametest.matchname(name)
    print(name)
    print(res)



