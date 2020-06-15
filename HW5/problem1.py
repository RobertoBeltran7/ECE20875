import numpy as np
from scipy.stats import norm, t


def read_files():
    with open('eng0.txt') as openENG0, open('eng1.txt') as openENG1:
        ENG0 = openENG0.readlines()
        ENG1 = openENG1.readlines()

        openENG0.close()
        openENG1.close()

    return ENG0, ENG1


def data_process_1(file):
    data = [float(x) for x in file]
    # Problem 1, Questions 1-2
    mu = 0.75
    samp_size = len(data)
    avg = np.mean(data)
    sd = np.std(data, ddof=1)

    stand_err = sd / np.sqrt(samp_size)
    z_score = (avg - mu) / stand_err
    p_val = 2 * norm.cdf(-abs(z_score))

    # Problem 1, Question 3
    new_p = 0.05
    z_c = norm.ppf(new_p / 2)
    # new Standard Error with p < 0.05
    new_SE = (avg - mu) / z_c

    new_samp_size = np.square(sd / new_SE)

    return samp_size, avg, sd, stand_err, z_score, p_val, z_c, new_SE, new_samp_size


def data_process_2(file1, file2):
    # Problem 1, Questions 4-5
    data_0 = [float(x) for x in file1]
    data_1 = [float(x) for x in file2]
    mu = 0
    samp_size_0 = len(data_0)
    samp_size_1 = len(data_1)

    avg_0 = np.mean(data_0)
    avg_1 = np.mean(data_1)
    avg_total = avg_0 - avg_1

    sd_0 = np.std(data_0, ddof=1)
    sd_1 = np.std(data_1, ddof=1)
    sd_0_sqrd = np.square(sd_0)
    sd_1_sqrd = np.square(sd_1)
    sd_total = np.sqrt((sd_0_sqrd / samp_size_0) + (sd_1_sqrd / samp_size_1))

    stand_err = sd_total
    z_score = (avg_total - mu) / stand_err
    p_val = 2 * norm.cdf(-abs(z_score))

    return samp_size_0, samp_size_1, avg_0, avg_1, avg_total, sd_total, stand_err, z_score, p_val


if __name__ == "__main__":
    data_1 = data_process_1(read_files()[1])
    print("Problem 1 Questions 1-2 results:")
    print("n = {}, mean = {}, s.d = {}, S.E = {}, z-score = {}, p-value = {}".format(data_1[0], data_1[1], data_1[2],
                                                                                     data_1[3], data_1[4], data_1[5]))

    print()
    print("Problem 1 Question 3 results:")
    print("z_score(p=0.05) = {}, S.E(p=0.05) = {}, n(p=0.05)= {}".format(data_1[6], data_1[7], data_1[8]))

    data_2 = data_process_2(read_files()[0], read_files()[1])

    print()
    print("Problem 1 Questions 4-5 results:")
    print("n_0 = {}, n_1 = {}, mean_0 = {}, mean_1 = {}, mean_total = {},"
          " s.d_total = {}, S.E = {}, z-score = {}, p-value = {}".format(
        data_2[0], data_2[1], data_2[2],
        data_2[3], data_2[4], data_2[5],
        data_2[6], data_2[7], data_2[8]))
