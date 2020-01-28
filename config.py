# coding: utf8
import os
import torch
import warnings


class DefaultConfig(object):
    model = 'MyVggNet16'  # The model used, the name must match the name in models/__ init__.py
    env = model
    ATTACK = 1
    GENUINE = 0
    train_filelists = [
        ['E:\\Data\\face_anti_spoofing\\ClientRaw',
            'E:\\Data\\face_anti_spoofing\\client_train_raw.txt', GENUINE],
        ['E:\\Data\\face_anti_spoofing\\ImposterRaw',
         'E:\\Data\\face_anti_spoofing\\imposter_train_raw.txt', ATTACK]
    ]
    test_filelists = [
        ['E:\\Data\\face_anti_spoofing\\ClientRaw',
            'E:\\Data\\face_anti_spoofing\\client_test_raw.txt', GENUINE],
        ['E:\\Data\\face_anti_spoofing\\ImposterRaw',
         'E:\\Data\\face_anti_spoofing\\imposter_test_raw.txt', ATTACK]
    ]

    # load_model_path = 'checkpoints/model.pth' # The path to load the pre-trained model. If None, it means no loading.
    load_model_path = None  # The path to load the pre-trained model. If None, it means no loading.

    batch_size = 16  # batch size
    use_gpu = torch.cuda.is_available()  # use GPU or not
    num_workers = 8  # how many workers for loading data
    print_freq = 20  # print info every N batch
    debug_file = os.path.join('tmp', 'debug')  # if os.path.exists(debug_file): enter ipdb
    result_name = 'result'

    max_epoch = 10
    lr = 0.01  # initial learning rate
    lr_decay = 0.5  # when val_loss increase, lr = lr*lr_decay
    lr_stepsize = 3  # learning step size
    weight_decay = 1e-5  # Loss function
    cropscale = 3.5
    image_size = 224


def parse(self, kwargs):
    '''
    Update config parameters according to dictionary kwargs
    '''
    # Update configuration parameters
    for k, v in kwargs.items():
        if not hasattr(self, k):
            # Warning or error, depending on your personal preference
            warnings.warn("Warning: opt has not attribut %s" % k)
        setattr(self, k, v)

    # Print configuration information
    print('user config:')
    for k, v in self.__class__.__dict__.items():
        if not k.startswith('__'):
            print(k, getattr(self, k))


DefaultConfig.parse = parse
opt = DefaultConfig()
