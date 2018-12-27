import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'


matrix1 = tf.constant([[1.,2.]])
matrix2 = tf.constant([[2.],[3.]])

product = tf.matmul(matrix1,matrix2)


sess = tf.Session()
print(sess.run(matrix1))
print(sess.run(matrix2))
print(sess.run(product))

sess.close()