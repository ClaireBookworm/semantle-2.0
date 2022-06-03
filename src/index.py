from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch
import random
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("distilroberta-base")
model = AutoModelForMaskedLM.from_pretrained("distilroberta-base")

def dailyword():


    commonwords = open("/google-10000-english-usa-no-swears-medium.txt").read().split("\n")
    todaysword = commonwords[random.randint(0, len(commonwords))]
    reference = tokenizer(todaysword)
    return reference

# take in input here, compare to reference

def returnSimilarity(input, reference):
    input = torch.tensor(input)
    reference = torch.tensor(reference)
    model.eval()
    with torch.no_grad():
        output = model(input, masked_lm_labels=reference)
        loss, prediction_scores = output
    return prediction_scores

# similarity = np.dot(reference, tokenizer(tempInput))

