args = {
  "lookback_pattern": 10,
  "look_forward": 5,
  "epoch": 50,
  "lr": 0.001,
  "weight_decay": 0.001,
  "n_country": 45,
  "all_num_fea": 1,
  "fig_day": 5,
  "node_fea" : 1,

  #预测多少个特征
  "pre_fea" : 1,

  "train_percentage":0.7,

  "val_percentage":0.15,

  "test_percentage":0.15,
}

class Parameters:
  def __init__(self):
    self.n_country = args['n_country']
    self.test_percentage = args['test_percentage']
    # self.country_name = args['country_name']
    self.all_num_fea = args['all_num_fea']
    self.node_fea = args['node_fea']
    self.lookback_pattern = args['lookback_pattern']
    self.pre_fea = args['pre_fea']
    self.epoch = args['epoch']
    self.lr = args['lr']
    self.weight_decay = args['weight_decay']
    self.train_percentage = args['train_percentage']
    self.val_percentage = args['val_percentage']
    self.fig_day = args['fig_day']
    # self.c_value = args['c_value']
    self.look_forward= args['look_forward']
  def get_optimizer(self, model_params):
    return self.optimizer(model_params, self.learning_rate)