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