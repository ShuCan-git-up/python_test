#coding=utf-8

import tensorflow as tf
t0 = tf.constant(3, dtype=tf.int32)
t0L = tf.constant(4, dtype=tf.int32)
t1 = tf.constant([3., 4.1, 5.2], dtype=tf.float32)
t1L = tf.constant([4., 5.1, 6.2], dtype=tf.float32)
t2 = tf.constant([['1', '2'],['3', '4']], dtype=tf.string)
t2L = tf.constant([['5', '6'],['7', '8']], dtype=tf.string)
t3 = tf.constant([[[5],[6],[7],[8]]])
W = tf.Variable(4, dtype=tf.float32)
b = tf.Variable(5, dtype=tf.float32)
# 创建 x 节点，用来输入实验中的输入数据
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
# 创建线性模型
linear_model = W*x + b

# 创建 y 节点，用来输入实验中得到的输出数据，用于损失模型计算
y = tf.placeholder(tf.float32)
# 创建损失模型
loss = tf.reduce_sum(tf.square(linear_model - y))
optimizer = tf.train.GradientDescentOptimizer(0.002)
train = optimizer.minimize(loss)
x_train = [1, 2, 3, 6, 8]
y_train = [4.8, 8.5, 10.4, 21.0, 25.3]
with tf.Session() as sess:
    # 必须要初始化才能使用，初始化和定义变量是两部在这个里面
    sess.run(tf.global_variables_initializer())
    # print(sess.run(linear_model, {x: [1, 2, 3, 6, 8]}))
    # print(sess.run(b))
    # print sess.run(x + y, {x:[1,2,3,4,5], y:[2,3,4,5,6]})
    for i in range(10000):
        sess.run(train, {x: x_train, y: y_train})
    for i in range(10000):
        print('W: %s, b: %s, loss: %s' %(sess.run(W), sess.run(b), sess.run(loss, {x:x_train, y:y_train})))


