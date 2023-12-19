import pandas as pd
import numpy as np

# 输入的数据是一个国家的一列
def lube(data, step):
    all_uppers, all_meds, all_lowers = [], [], []
    t_data=data.T
    t_data = np.array(t_data)
    all_day = t_data.shape[1] - (t_data.shape[1] % step)
    t_data = t_data[:, :all_day - 1]
    for i in t_data:
        uppers = []
        meds = []
        lowers = []
        for j in range(0, len(i), step):
            upper = i[j:j + step].max()
            med = np.median(i[j:j + step])
            lower = i[j:j + step].min()
            uppers.append(upper)
            meds.append(med)
            lowers.append(lower)
        all_uppers.append(uppers)
        all_meds.append(meds)
        all_lowers.append(lowers)
    return np.array(all_meds),np.array(all_lowers),np.array(all_uppers)

#
# country_data_cases = pd.read_csv('../dataset/country_data_cases.csv', delimiter=",")
# uppers, meds, lowers = lube(country_data_cases.iloc[:, 1], 7)
# all_result = np.array([uppers, meds, lowers]).T
# print("uppers shape:", len(uppers))
# print(uppers)
# print("meds shape:", len(meds))
# print(meds)
# print("lowers shape:", len(lowers))
# print(lowers)
