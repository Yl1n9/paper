import numpy as np
import pandas as pd


class fuzzy_information_granular():
    def __init__(self, data, step):
        self.data = data
        self.step = step


    def upper_lower_med(self, data):
        step = self.step
        meds = []
        uppers = []
        lowers = []

        for i in range(0, len(data), step):
            sub_data = data[i:i + step]
            med = np.median(sub_data)
            lower_set, upper_set = [], []
            for j in range(len(sub_data)):
                if sub_data[j] < med:
                    lower_set.append(sub_data[j])
                if sub_data[j] > med:
                    upper_set.append(sub_data[j])
            lower_sum = np.array(lower_set).sum()
            upper_sum = np.array(upper_set).sum()
            if lower_sum==0 or upper_sum==0:
                med = data[int(len(data)/2)]
                support_upper_set =  data[int(len(data)/2):]
                support_lower_set =  data[:int(len(data)/2)]
                upper = 2*sum(support_upper_set)/len(support_upper_set)-med
                lower = 2*sum(support_lower_set) / len(support_lower_set)-med
            else:
                lower = (2 * lower_sum / (len(lower_set))) - med
                upper = (2 * upper_sum / (len(upper_set))) - med
            meds.append(med)
            uppers.append(upper)
            lowers.append(lower)
        return lowers, meds, uppers

    def get_FIG_result(self,fig_day):
        lower_list, med_list, upper_list = [], [], []
        all_data = self.data.T
        all_data = np.array(all_data)
        all_day = all_data.shape[1] - (all_data.shape[1] % fig_day)
        all_data = all_data[:, :all_day - 1]
        for i in all_data:
            lowers, meds, uppers = self.upper_lower_med(i)
            lower_list.append(lowers)
            med_list.append(meds)
            upper_list.append(uppers)
        return np.array(lower_list), np.array(med_list), np.array(upper_list)

# country_data_cases = pd.read_csv('../dataset/country_data_cases.csv', delimiter=",")
# tttt = country_data_cases.iloc[:, 1][:364]
# fig = fuzzy_information_granular(tttt, 7)
# lowers, meds, uppers = fig.upper_lower_med(tttt, 7)
# print(len(meds))
# print('lowers', lowers)
# print('meds', meds)
# print('uppers', uppers)
