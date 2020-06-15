import numpy as np
import matplotlib.pyplot as plt
from helper import *


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities

    :param hist: list
    :return: list
    """
    prob_list=[]
    total_counts=sum(hist)

    for num in hist:
        prob=num/total_counts
        prob_list.append(prob)

    return prob_list


def computeJ(histo, width):
    """
    calculate computeJ for one bin width

    :param histo: list
    :param width: int
    :return: float
    """
    num_samples=sum(histo)
    prob_hist=norm_histogram(histo)

    sum_prob=sum(map(lambda i: i*i,prob_hist))
    J_result=((2/((num_samples-1)*width))-((num_samples+1)/((num_samples-1)*width)))*sum_prob

    return J_result


def sweepN (data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate computeJ for a full sweep [min_bins to max_bins]

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    J_list=[]

    for bins in range(min_bins,max_bins+1):
        hist_vals=plt.hist(data,bins,(minimum,maximum))
        J_comp=computeJ(hist_vals[0],((maximum-minimum)/bins))
        J_list.append(J_comp)


    return J_list


def findMin (l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """
    minNum=min(l)
    minIndx=l.index(minNum)

    return (minNum,minIndx)


if __name__ == '__main__':
    data = getData()  # reads data from inp.txt. This is defined in helper.py
    lo = min(data)
    hi = max(data)
    
    js = sweepN(data, lo, hi, 1, 100)

    # the values 1 and 100 represent the lower and higher bound of the range of bins.
    # They will change when we test your code and you should be mindful of that.
    
    print(findMin(js))

    # Include code here to plot js vs. the bin range

