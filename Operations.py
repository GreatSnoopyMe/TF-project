from collections import namedtuple
from recordclass import recordclass

G = -1
T = -2
N = -3

OperationInfo = recordclass('OperationInfo',['name','relation_list','weight'])

TF_OERATIONS = [
    OperationInfo(name='tf.add',
                  relation_list=[T,T],
                  weight=1),
    OperationInfo(name='tf.gather',
                  relation_list=[G,N],
                  weight=2),
    OperationInfo(name='tf.transpose',
                  relation_list=[G],
                  weight=3),
    OperationInfo(name='tf.ones',
                  relation_list=[N],
                  weight=4),
]