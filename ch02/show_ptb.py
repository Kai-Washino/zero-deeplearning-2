import sys
sys.path.append('..')
from dataset import ptb
import numpy as np
from common.util import preprocess, create_co_matrix, cos_similarity, ppmi

corpus, word_to_id, id_to_word = ptb.load_data('train')

print(len(corpus))
print(corpus[:30])
print(id_to_word[0])
print(word_to_id['car'])