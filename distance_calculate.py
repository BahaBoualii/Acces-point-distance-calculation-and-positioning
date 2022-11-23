import numpy as np

from signal_result import read_data_from_cmd


# this function is for calculating the distance to an AP
# from the signal strength percentage

# PS: there's no exact conversion formula because there are different approaches

def estimate_distance(power_received_percentage):

    power_received_dbm = (int(power_received_percentage) / 2) - 100

    path_loss_exps = (2.0, 3.0, 4.0)

    d_ref = 1.0
    power_ref = -50.5
    path_loss_exp = path_loss_exps[0]

    d_est = d_ref*(10**(-(power_received_dbm - power_ref)/(10 * path_loss_exp)))

    return (np.round(d_est,2))

# pr=read_data_from_cmd()
# print(estimate_distance(pr))
