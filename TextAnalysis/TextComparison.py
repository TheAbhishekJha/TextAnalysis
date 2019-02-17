from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu

import json

hypothesis = "A laptop is a computer designed for portability. Laptops are usually less than 3 inches thick, weigh less than 5 pounds and can be powered by a battery. As such laptops are designed for low power consumption and are most often used when space is limited, such as on an airplane."
user= "A laptop computer, sometimes called a notebook computer by manufacturers, is a battery- or AC-powered personal computer generally smaller than a briefcase that can easily be transported and conveniently used in temporary spaces such as on airplanes, in libraries, temporary offices, and at meetings."

rouge = Rouge()
scores = rouge.get_scores(hypothesis, user)
print(scores)

# dictionary = str(scores)
# print(dictionary)
#dictionary =  json.loads(scores)
reference = [hypothesis.split()]
candidate = user.split()
print(reference)
score = sentence_bleu(reference, candidate)
print("BLEU Score:"+str(score))

print(hypothesis.split())