import pandas as pd
import numpy as np
from sklearn.manifold import TSNE


df_cosmetic = pd.read_csv('data/cosmetic_preprocess.csv')
# Not enough data for skin type Mature and Sensitive to fit t_SNE so dropping
df_cosmetic.drop(columns=['Mature', 'Sensitive'], inplace=True)

option_1 = df_cosmetic.Label.unique().tolist()
option_2 = df_cosmetic.columns[6:].tolist()


def generate_tokens(label, skin_type):
    df = df_cosmetic[df_cosmetic['Label'] == label][df_cosmetic[skin_type] == 1]
    df = df.reset_index(drop=True)

    # embedding each ingredients
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

    df_len = len(df)
    ingredient_len = len(ingredient_idx)
    document_term_matrix = np.zeros(shape = (df_len, ingredient_len))
    if df_len <= 1 or ingredient_len <= 1:
        return

    t_sne(corpus, ingredient_idx, document_term_matrix, ingredient_len, df)

    return df


def oh_encoder(tokens, ingredient_idx, ingredient_len):
    x = np.zeros(ingredient_len)
    for t in tokens:
        idx = ingredient_idx[t]
        x[idx] = 1
    return x


def t_sne(corpus, ingredient_idx, document_term_matrix, ingredient_len, df):
    i = 0
    for tokens in corpus:
        document_term_matrix[i, :] = oh_encoder(tokens, ingredient_idx, ingredient_len)
        i += 1

    model = TSNE(n_components=2, learning_rate=200)
    tsne_features = model.fit_transform(document_term_matrix)

    df['X'] = tsne_features[:, 0]
    df['Y'] = tsne_features[:, 1]


if __name__ == '__main__':
    df_all = pd.DataFrame()
    for op_1 in option_1:
        for op_2 in option_2:
            temp = generate_tokens(op_1, op_2)
            if temp is not None:
                temp['Label'] = op_1 + '_' + op_2
                df_all = pd.concat([df_all, temp])
            else:
                print('{}_{} was not added because of lack of data available'.format(op_1, op_2))
    df_all.reset_index(drop=True, inplace=True)
    df_all.to_csv('data/cosmetic_TSNE.csv', encoding='utf-8-sig', index=False)
