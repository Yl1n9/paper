import torch
import numpy as np
#NRMSE
#MSE
#mase2_loss
#mae_loss
from numpy import mean

def rmse_loss(output, label):
    return torch.sqrt(torch.mean(torch.square(output - label)))
def NRMSE(yhat,y):
    return torch.sqrt(torch.mean(((yhat-y)/torch.std(yhat,0))**2))

def MSE(yhat,y):
    return torch.mean((yhat-y)**2)

def mase2_loss(output, label, mean=None):
    # Extreme 2: all people equal
    # X = (x_1 + x_2 + … + x_N)
    # Y = (y_1 + y_2 + … + y_N)
    # L = (X - Y)^2 / Y
    #label = label[:, 0]
    X = torch.sum(output)
    Y = torch.sum(label)
    if Y == 0 and not mean is None:
        return torch.abs(X - Y) / torch.sum(mean)
    elif Y == 0:
        return torch.abs(X - Y)
    else:
        return torch.abs(X - Y) / Y
def mase1_loss(output, label, mean=None):
    # Extreme 1: all countries equal
    # L_i = (x_i - y_i)^2 / y_i
    # L = (L_1 + L_2 + … + L_N) / N
    #label = label[:, 0]
    output[1] = output[1].reshape(output[1].shape[0])
    label_mean = torch.mean(label)
    #mean = mean.cuda()  #111111
    if not mean is None:
        return torch.mean(torch.abs(output - label) / mean)
    if label_mean == 0:
        return torch.mean(torch.abs(output - label))
    else:
        return torch.mean(torch.abs(output - label)) / label_mean


def mape_loss(pred,actual):
    return torch.mean(torch.abs((actual - pred) / actual)) * 100

def mae_loss(output, label):
    return torch.mean(torch.abs(output - label))

