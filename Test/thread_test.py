# encoding: UTF-8
import threading
import time

product = list()


# 生产者方法
def produce():
    for i in range(2, 101):
        print('标号为{}的商品被生产了\r\n'.format(i))
        product.append(i)


# 消费者方法
def consume():
    while True:
        if product:
            for i in product:
                product.remove(i)
                print('标号为{}的商品被消费了\r\n'.format(i))


t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)

t1.start()
t2.start()
