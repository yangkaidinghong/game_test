# 面试题3 压力测试代码
import game_test
import time
import timeit


def pressuretest():
    for i in range(10000):
        game_test.start()


if __name__ == '__main__':
    # 可以利用time模块测试出一次的时间
    start = time.time()
    pressuretest()
    end = time.time()
    print('运行时间：%0.6f' % (end - start))
    # 也可以利用timeit模块重复测试多次
    timer1 = timeit.Timer("pressuretest()", "from __main__ import pressuretest")
    cost1 = timer1.timeit(1)
    print("运行时间: %f" % (cost1))

    # 面试题4 跨进程思路
    #
    # 1.由单进程任务更改为多进程任务
    # 2.将存储用户名方式更改为存储至数据库中
    # 3.判断数据库中是否存储相同数据，如果已存在相同数据则不进行存储，反之则进行存储

