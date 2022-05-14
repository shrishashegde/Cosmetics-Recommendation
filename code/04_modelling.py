import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
cosm_2 = pd.read_csv('data/cosmetic_p.csv')


option_1 = cosm_2.Label.unique().tolist()
option_2 = cosm_2.columns[6:].tolist()


def my_recommender(op_1, op_2):
    df = cosm_2[cosm_2['Label'] == op_1][cosm_2[op_2] == 1]
    df = df.reset_index()


    ingredient_idx = {}
    corpus = []
    idx = 0

    for i in range(len(df)):
        ingreds = df['ingredients'][i]
        ingreds = ingreds.lower()
        tokens = ingreds.split(', ')
        corpus.append(tokens)
        for ingredient in tokens:
            if ingredient not in ingredient_idx:
                ingredient_idx[ingredient] = idx
                idx += 1

  
    M = len(df)      
    N = len(ingredient_idx) 

    A = np.zeros(shape = (M, N))

def encoder(tokens):
        x = np.zeros(N)
        for t in tokens:
            idx = ingredient_idx[t]
            x[idx] = 1
        return x

    i = 0
    for tokens in corpus:
        A[i, :] = encoder(tokens)
        i += 1


    model = TSNE(n_components = 2, learning_rate = 200)
    tsne_features = model.fit_transform(A)


    df['X'] = tsne_features[:, 0]
    df['Y'] = tsne_features[:, 1]

    return df