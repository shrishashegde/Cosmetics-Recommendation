import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import math  


def clean_data(df):
    df.loc[df['Label'] == "moisturizing-cream-oils-mists", 'Label'] = "moisturizer"
    df.loc[df['Label'] == "facial-treatments", 'Label'] = "face_treatment"
    df.loc[df['Label'] == "face-mask", 'Label'] = "face_mask"
    df.loc[df['Label'] == "eye-treatment-dark-circle-treatment", 'Label'] = "eye_treatment"
    df.loc[df['Label'] == "sunscreen-sun-protection", 'Label'] = "sunscreen"
    df.drop(columns=['URL'], inplace=True)


def preprocess_ingredients(df):
    df.dropna(subset=['ingredients'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    processed_ingredient = [t.split('\r\n\r\n') for t in df['ingredients']]
    pattern = ['\r\n', '-\w+:', 'Please', 'No Info', 'This product', 'Visit']

    for i in range(len(df)):
        num = len(processed_ingredient[i])
        for j in range(num):
            if all(x not in processed_ingredient[i][j] for x in pattern):
                df['ingredients'][i] = processed_ingredient[i][j]
    return df


def skin_type_preprocessing(data):
    data['skin_type'].fillna(data.mode()['skin_type'][0], inplace=True)
    data.isnull().sum()
    data['skin_type'].unique()
    data['skin_type'] = data['skin_type'].str.replace('and', ',')
    data['skin_type'] = data['skin_type'].str.replace(' ', '')
    data['skin_type'] = data['skin_type'].str.replace(',,', ',')
    data['skin_type'] = data['skin_type'].str.replace('Oily', 'Oil')
    jp = data['skin_type'].str.split(':', n=1, expand=True)
    data['skin_type'] = jp[1]
    data['skin_type'].replace('', data.mode()['skin_type'][0], inplace=True)
    data['skin_type'] = data['skin_type'].str.replace('.', '')
    data.skin_type = data.skin_type.str.split(',')
    mlb = MultiLabelBinarizer(sparse_output=True)
    data = data.join(pd.DataFrame.sparse.from_spmatrix(mlb.fit_transform(data.pop('skin_type')), index=data.index, columns=mlb.classes_))
    return data


def preprocess_price(data):
    data['price'].fillna('$0', inplace=True)
    for idx, row in data.iterrows():
        curr = str(data.loc[idx, 'price'])
        if ' ' in curr:
            data.loc[idx, 'price'] = int(math.ceil(float(curr.split(' ')[0][1:])))
        else:
            data.loc[idx, 'price'] = int(math.ceil(float(curr[1:])))
    return data


def preprocess_rank(data):
    data.dropna(subset=['rank'], inplace=True)
    for idx, row in data.iterrows():
        curr = str(data.loc[idx, 'rank'])
        data.loc[idx, 'rank'] = float(curr.split(' ')[0])
    return data    


if __name__ == '__main__':
    df = pd.read_csv('data/cosmetic.csv', na_values={'NA', '#NAME?'})
    clean_data(df)
    df = preprocess_ingredients(df)
    df = skin_type_preprocessing(df)
    df = preprocess_price(df)
    df = preprocess_rank(df)
    df.to_csv('data/cosmetic_preprocess.csv', index=False)
