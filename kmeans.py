import os
import sys
from pyspark import SparkContext


def spark_matrix_multiplication(file_A, file_x):
    """
    perform matrix multiplication
    :param file_A: file of matrix
    :param file_x: file of vector
    :return: the rdd of result vector
    """
    rdd_A = sc.textFile(file_A)
    rdd_x = sc.textFile(file_x)
    rdd_A = rdd_A.map(lambda l: [float(x) for x in l.split(',')]).cache()
    rdd_x = rdd_x.map(lambda l: [float(x) for x in l.split(',')]).cache()
    n_col = len(rdd_A.collect()[0])
    rdd_A = rdd_A.map(lambda l: [(l[j], j) for j in range(n_col)])
    rdd_x = rdd_x.map(lambda l: [(l[j], j) for j in range(n_col)])
    rdd_A = rdd_A.zipWithIndex()
    rdd_A = rdd_A.flatMap(lambda x: [(y[1], (x[1], y[0])) for y in x[0]])
    rdd_x = rdd_x.flatMap(lambda l: [(x[1], x[0]) for x in l])
    rdd_join = rdd_A.join(rdd_x)
    rdd_prod = rdd_join.map(lambda l: (l[1][0][0], l[1][0][1]*l[1][1]))
    res = rdd_prod.reduceByKey(lambda x,y: x+y).map(lambda x: x[1])
    return res


if __name__ == '__main__':
    sc = SparkContext(appName='Matrix')
    file_A = sys.argv[1]
    file_x = sys.argv[2]
    res = spark_matrix_multiplication(file_A, file_x)
    print(res.collect())
    sc.stop()
