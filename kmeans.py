import os
import sys
from pyspark import SparkContext
import numpy as np


def k_means(file1, file2):
    """
    Compute the k-means clustering for specified data and centroids
    :param file1: file that contains data points
    :param file2: file that contains centroid points
    :return: write final seeds to a file
    """
    max_iter = 100

    data = sc.textFile(file1).map(lambda line: [float(x) for x in line.split(' ')]).cache()
    centroids = sc.textFile(file2).map(lambda line: [float(x) for x in line.split(' ')]).collect()

    for i in range(max_iter):
        data_label = data.map(
            lambda d: (np.argmin([np.linalg.norm(np.array(d) - np.array(c)) for c in centroids]), [np.array(d), 1]))
        centroids = data_label.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])).sortByKey(ascending=True).map(
            lambda x: x[1][0] / x[1][1]).collect()

    res = centroids

    file = open("result_centroids.txt", "w")
    for c in res:
        s = ''
        for x in c:
            s = s + str(x) + " "
        file.write(s + "\n")
    file.close()
    return None


if __name__ == '__main__':
    sc = SparkContext(appName='kmeans')
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    k_means(file1, file2)
    sc.stop()
