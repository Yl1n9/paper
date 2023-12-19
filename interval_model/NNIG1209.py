#重写一个版本
import numpy as np
class nn_fuzzy_information_granular1209():
    def __init__(self, country_data_case):
        self.country_data_case = country_data_case

    def data_process(self,data):
        data.sort()
        min_value = data.min()
        max_value = data.max()
        min_set = np.delete(data, np.where(data == min_value))
        max_set = np.delete(data, np.where(data == max_value))
        return data,min_set,max_set

    def min_feijinlin(self,min_set, data):
        min_set_distance = []
        for i in range(1, len(min_set)):
            min_set_distance.append([i - 1, min_set[i] - min_set[i - 1]])
        min_set_distance = np.array(min_set_distance)
        if len(min_set_distance.shape) > 1:
            best_min_set_distance = min_set_distance[:, 1].max()
            best_min_set_distance_index = np.where(min_set_distance[:, 1] == best_min_set_distance)[0][0]
            min_fjl_set = data[best_min_set_distance_index:]
        else:  # 这个时候是空值
            best_min_set_distance_index = int(len(data) / 2 + 1)
            min_fjl_set = data[best_min_set_distance_index:]
        return min_fjl_set

    def max_feijinlin(self,max_set, data):
        max_set_distance = []
        for i in range(1, len(max_set)):
            max_set_distance.append([i - 1, max_set[i] - max_set[i - 1]])
        max_set_distance = np.array(max_set_distance)
        if len(max_set_distance.shape) > 1:
            best_max_set_distance = max_set_distance[:, 1].max()
            best_max_set_distance_index = np.where(max_set_distance[:, 1] == best_max_set_distance)[0][0]
            max_fjl_set = data[:best_max_set_distance_index+1]
        else:
            best_max_set_distance_index = int(len(data) / 2 + 1)
            max_fjl_set = data[:best_max_set_distance_index]
        return max_fjl_set

    def compute_kernel(self,data, min_fjl_set, max_fjl_set):
        length = len(max_fjl_set) + len(min_fjl_set)
        sum_set = sum(min_fjl_set) + sum(max_fjl_set)
        avg = sum_set / length
        data_avg_distance = []
        for i in range(len(data)):
            data_avg_distance.append([abs(data[i] - avg), i])
        data_avg_distance = np.array(data_avg_distance)
        min_distance = data_avg_distance[:, 0].min()
        best_index = np.where(data_avg_distance[:, 0] == min_distance)[0][0]
        kernel = data[best_index]
        # 计算支撑下界
        support_lower_set = data[:best_index]
        support_upper_set = data[best_index + 1:]
        if len(support_lower_set) != 0:
            lower = 2 * sum(support_lower_set) / len(support_lower_set) - kernel
        else:
            support_lower_set = data[:int(len(data) /2)]
            lower = 2 * sum(support_lower_set) / len(support_lower_set) - kernel

        # 计算支撑上界
        if len(support_upper_set) != 0:
            upper = 2 * sum(support_upper_set) / len(support_upper_set) - kernel
        else:
            support_upper_set =  data[int(len(data)/2):]
            upper = 2*sum(support_upper_set)/len(support_upper_set)-kernel        
        return lower, kernel, upper

    def get_FIG_result(self,country_data_case, fig_day):
        country_data_case = np.array(country_data_case)
        all_day = country_data_case.shape[1] - (country_data_case.shape[1] % fig_day)
        country_data_case = country_data_case[:, :all_day - 1]
        lower_list, med_list, upper_list = [], [], []
        country_data_case = np.array(country_data_case)
        for i in range(country_data_case.shape[0]):
            lower_set, med_set, upper_set = [], [], []
            for j in range(0, country_data_case.shape[1], fig_day):
                data = country_data_case[i, j:j + fig_day]
                data, min_set, max_set = self.data_process(data)
                min_fjl_set = self.min_feijinlin(min_set, data)
                max_fjl_set = self.max_feijinlin(max_set, data)
                lower, kernel, upper = self.compute_kernel(data, min_fjl_set, max_fjl_set)
                lower_set.append(lower)
                med_set.append(kernel)
                upper_set.append(upper)
            lower_list.append(lower_set)
            med_list.append(med_set)
            upper_list.append(upper_set)
        return np.array(lower_list), np.array(med_list), np.array(upper_list)
