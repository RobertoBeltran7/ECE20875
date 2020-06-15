import numpy as np
import matplotlib.pyplot as plt

# bars: list of length number of bins, with each entry having its histogram value
# filename: file to save plot to (in .png format)
# minrange: minimum value of leftmost bin
# maxrange: maximum value of rightmost bin


def plotHisto (bars, filename, minrange=0.0, maxrange=100.0, plotinline=False):
	mrange = maxrange - minrange
	binsize = mrange/len(bars)
	
	# this is a "list comprehension" -- it's a quick way to process one
	# list to produce another list
	labels = [(mrange / len(bars)) * i + minrange for i in range(len(bars))]
	
	plt.bar(labels, bars, align='edge', width=binsize)
	if plotinline :
		plt.show()
	else:
		plt.savefig(filename)
		# plt.show()
		plt.clf()


def getData(filename='inp.txt'):
	return np.loadtxt(filename)
