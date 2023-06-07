import numpy as np
import ast
from execute import convert_to_tensor

def get_inputs(path):
    # with open('examples/1.txt') as fp:
    with open(path) as fp:
        input_info = {}
        input_info['input_t'] = []
        input_info['RQ'] = []
        while True:
            line = fp.readline()
            if line.strip() == "# input tensors":
                while True:
                    line1 = fp.readline()
                    if line1 == "\n":
                        break
                    else:
                        input_info['input_t'].append(convert_to_tensor(line1))
                        # print(input_info['input_t'])
            elif line.strip() == "# output tensors":
                # print("f")
                line1 = fp.readline()
                if line1 == "\n":
                    break
                else:
                    input_info['output_t'] = convert_to_tensor(line1)
            elif line.strip() == "# Requirement":
                # print("s")
                while True:
                    line = fp.readline()
                    if line.strip() == "":
                        break
                    else:
                        input_info['RQ'].append(line.strip())
            elif not line:
                break
        return input_info
