# imports
import os
import csv
import sys

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import numpy as np

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
class BioGPTEmbedder(object):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/biogpt")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/biogpt")

    def calculate(self, text_inputs):
        X = np.zeros((len(text_inputs), 1024), dtype=np.float32)
        for i, text in enumerate(text_inputs):
            encoded_input = self.tokenizer(text, return_tensors="pt")
            with torch.no_grad():
                hidden_states = self.model.base_model(**encoded_input).last_hidden_state
            mean_encoding = torch.mean(hidden_states, dim=1)
            mean_encoding_np = mean_encoding.numpy()
            X[i, :] = mean_encoding_np
        return X

# read text from .csv file, assuming one column with header
with open(input_file, "r") as f:
    next(f)
    text_list = []
    for l in f:
        text_list += [l.rstrip("\n")]

# run model
model = BioGPTEmbedder()
X = model.calculate(text_list)

# write output in a .csv file
columns = ["f-{0}".format(i) for i in range(X.shape[1])]
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(columns)  # header
    for i in range(X.shape[0]):
        writer.writerow(list(X[i,:]))
