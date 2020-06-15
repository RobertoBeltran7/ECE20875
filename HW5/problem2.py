import numpy as np
from scipy.stats import norm, t


def data_process_3():
    data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]

    # Problem 2 Question 1
    # confidence interval
    c1 = 0.95

    samp_size = len(data)
    avg = np.mean(data)
    sd = np.std(data, ddof=1)

    stand_err = sd / np.sqrt(samp_size)
    t_c = t.ppf(1 - (1 - c1) / 2, df=samp_size - 1)

    intervals = (avg - (t_c * sd) / np.sqrt(samp_size), avg + (t_c * sd) / np.sqrt(samp_size))

    # Problem 2 Question 2
    c2 = 0.9
    t_c_2 = t.ppf(1 - (1 - c2) / 2, df=samp_size - 1)

    intervals2 = (avg - (t_c_2 * sd) / np.sqrt(samp_size), avg + (t_c_2 * sd) / np.sqrt(samp_size))

    # Problem 2 Question 3
    new_sd = 16.836
    new_std_err = new_sd / np.sqrt(samp_size)
    z_c = norm.ppf(1 - (1 - c1) / 2)

    intervals3 = (avg - (z_c * new_sd) / np.sqrt(samp_size), avg + (z_c * new_sd) / np.sqrt(samp_size))

    # Problem 2 Question 4
    # solve for t_c when lower interval endpoint is zero (mu = 0)
    t_c_new = avg / (sd / np.sqrt(samp_size))

    # find p value
    p_val = 2 * t.cdf(-abs(t_c_new), df=samp_size - 1)
    new_c = 1 - p_val
    intervals4 = (avg - (t_c_new * sd) / np.sqrt(samp_size), avg + (t_c_new * sd) / np.sqrt(samp_size))

    return (samp_size, avg, sd, stand_err, t_c, intervals), (t_c_2, intervals2), (avg, new_std_err, z_c, intervals3), (
    t_c_new, p_val, new_c, intervals4)


if __name__ == "__main__":
    data1 = (data_process_3()[0])
    data2 = (data_process_3()[1])
    data3 = (data_process_3()[2])
    data4 = (data_process_3()[3])

    print("Problem 2 Question 1 results:")
    print("n = {}, mean = {}, s.d = {}, S.E = {}, t-value = {},"
          " interval = {}".format(data1[0], data1[1], data1[2], data1[3], data1[4], data1[5]))

    print()
    print("Problem 2 Question 2 results:")
    print("t_value = {}, interval = {}".format(data2[0], data2[1]))

    print()
    print("Problem 2 Question 3 results:")
    print("mean = {}, S.E = {}, z-value = {}, interval = {}".format(data3[0], data3[1], data3[2], data3[3]))

    print()
    print("Problem 2 Question 4 results:")
    print("t-value = {}, p-value = {}, confidence_level = {}, interval = {}".format(data4[0], data4[1], data4[2],
                                                                                    data4[3]))
