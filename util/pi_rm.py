# 区间预测的评估指标
import math
import pandas as pd

# 总体变量说明
# pred_lower：预测得到的下界，是指一个国家的数据，即（batch,1）
# pred_upper：预测得到的上界,（batch,1）
# pred_med：预测得到的中值
# real_med：实际的中值
#为了计算A ，导入最大值和最小值
import numpy as np


def PINRW (pred_upper,pred_lower,a):
    up_low_sum = 0
    n = len(pred_lower)
    for i in range(n):
        temp = pred_upper[i]-pred_lower[i]
        up_low_sum = up_low_sum + abs(temp)
    pinrw = up_low_sum/n/a
    return pinrw*100

def PINAW(pred_upper,pred_lower,a):
    up_low_sum = 0
    n = len(pred_lower)
    for i in range(n):
        temp = pred_upper[i] - pred_lower[i]
        up_low_sum = up_low_sum + temp
    pinaw = (up_low_sum / n)/a * 100
    return pinaw

def PICP(real_med, pred_upper, pred_lower):
    up_low_sum = 0
    n = len(pred_upper)
    for i in range(n):
        if real_med[i] <= pred_upper[i] and real_med[i] >= pred_lower[i]:
            temp = 1
        else: #real_med[i]>pred_upper[i] or real_med[i] < pred_lower[i]:
            temp = 0
        up_low_sum = up_low_sum + temp
    picp = up_low_sum / n
    return picp


def PINAD(pred_upper,pred_lower,real_med,a):
    n = len(real_med)
    up_low_sum = 0
    temp = 0
    for i in range(n):
        if real_med[i]<pred_lower[i]:
            temp = pred_lower[i] - real_med[i]
        if real_med[i]>pred_upper[i]:
            temp = real_med[i] - pred_upper[i]
        if real_med[i]>pred_lower[i] and real_med[i]<pred_upper[i]:
            temp = 0
        up_low_sum = up_low_sum + temp
    pinad = up_low_sum/n/a
    return pinad

def PIARW(pred_upper, pred_lower, pred_med):
    # PIARW = 1/n * sum( (Ui-Li)/yi)  * 100%
    n = len(pred_upper)
    up_low_sum = 0
    for i in range(n):
        temp = (pred_upper[i] - pred_lower[i]) / pred_med[i]
        up_low_sum = up_low_sum + temp
    piarw = up_low_sum / n * 100
    return piarw


def PPP(pred_upper, pred_lower, real_upper, real_lower):
    n = len(pred_upper)
    up_low_sum = 0
    for i in range(n):
        temp1 = abs(pred_upper[i] - real_upper[i])
        temp2 = abs(pred_lower[i] - real_lower[i])
        up_low_sum = up_low_sum + temp1 + temp2
    return up_low_sum / n
