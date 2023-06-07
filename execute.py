import numpy as np
import tensorflow as tf
import operator
from ast import literal_eval
from torch import tensor
import warnings
warnings.filterwarnings('ignore')


TF_PREFIX = 'tf.'


def convert_to_tensor(tensor_like):
    if isinstance(tensor_like,tf.Tensor):
        return tensor_like
    return tf.constant(literal_eval(tensor_like))


def get_tf_function(function_name):
    """Returns a TensorFlow function object given its name.

    Args:
        function_name: The string name of the function, e.g., "tf.matmul". Must
        start with "tf.". Nested modules are allowed, e.g., "tf.nn.softmax".

    Returns:
        The function object corresponding to function_name.

    Raises:
        ValueError: If the function name does not start with "tf.", or the function
        could not be found.
    """
    if not function_name.startswith(TF_PREFIX):
        raise ValueError('get_tf_function() called with function {}, which does ''not start with "tf.".'.format(function_name))
    function_name_without_prefix = function_name[len(TF_PREFIX):]
    try:
        tf_function = operator.attrgetter(function_name_without_prefix)(tf)
        if tf_function is None:
            raise ValueError('Could not find TF function {}'.format(function_name))
        return tf_function
    except AttributeError:
        raise ValueError('AttributeError encountered in get_tf_function for name {}'.format(function_name))


def _find_ins(k,input_dict):
    pos = int(k[2:])-1
    return input_dict['input_t'][pos]


def fix_format(s: str):
    return s.replace(" ","").replace(",",", ")


def parse_inputs(s: str, input_dict: dict):
    """
    Description:
    parse_inputs deals with expression like [[1],[2]],[1,2], in1

    Args:
        s: input string
    
    Returns:
        a list of tensorflow array
    """
    s = fix_format(s)
    res = []
    start_pos = 0
    start_copy = 0
    while True:
      tmp_index = s.find(",",start_pos)
      if tmp_index == -1:
        tmp_res = s[start_copy+1:].strip()
        if tmp_res[:2] == "in":
          res.append(_find_ins(tmp_res,input_dict))
        else:
          res.append(convert_to_tensor(tmp_res))
        break
      elif (s[:tmp_index].count('[') == s[:tmp_index].count(']')):
        tmp_res = s[start_copy:tmp_index].strip()
        if tmp_res[:2] == "in":
          res.append(_find_ins(tmp_res,input_dict))
        else:
          res.append(convert_to_tensor(tmp_res))
        start_pos = tmp_index + 1
        start_copy = start_pos
      else:
        start_pos = tmp_index + 1
    return res


def execute_string_operation_single(s: str, input_dict: dict):
    """
    Description:
    parse_string_operation_single deals with expression like tf.add([1,2],[3,4]), which uses only one tensorflow operation

    Args:
        s: input string
    
    Returns:
        a tensor, value of the expression
    """
    tmp_index = s.find('(')
    if tmp_index == -1:
        raise ValueError("The input string is not a complete expression")
    else:
        cur_operation = s[:tmp_index]
        try:
            return get_tf_function(cur_operation)(*parse_inputs(s[tmp_index+1:-1], input_dict))
        except:
            print("ERROR in expression: ",s)
            exit()


def tf2str(ins: tf.Tensor):

    return '['+str(ins.numpy())[1:-1].strip().replace(' ',',')+']'


def execute_full_operation(s:str, input_dict:dict):
    tmp_index = s.find(")")
    if tmp_index == -1:
        return s
    else:
        start_point = s.rfind("tf.",0,tmp_index)
        tmp_small = tf2str(execute_string_operation_single(s[start_point:tmp_index+1],input_dict))
        return execute_full_operation(s[:start_point] + tmp_small + s[tmp_index+1:],input_dict)


# input_dict = {"input_t":[tf.constant([1,4])]}
# print(execute_string_operation_single("tf.add([1, 2], in1)",input_dict))
# print(execute_full_operation("tf.add(tf.add(in1,[2,3]),[3,4])",input_dict))
# # print(execute_full_operation("tf.add(tf.add(in1,[2,3]),[3,3,4])",input_dict))
