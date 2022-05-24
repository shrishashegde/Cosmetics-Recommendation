# Abstract

Consumer interest in cosmetics has risen globally in recent years, with a focus on skincare. Consumers have previously relied on best-seller products or 
in-store counter recommendations. However, because everyone's skin is different, these are ineffective ways for determining whether a product and a person are compatible.
The goal of this proposal is to create a skincare product recommendation system based on the user's skin type and the product's ingredient composition. 
Product chemical components are identified and products with similar constituent compositions are found using content-based filtering.

# I. INTRODUCTION

With an annual increase in sales, skincare has surpassed makeup as the "fastest-growing category internationally". According to Trefis, a financial research and analysis 
business, skincare product sales in the United States increased by 13% in 2018, whereas makeup sales only increased by 1% . Trefis also expects the worldwide skincare 
market to reach $180 billion in the next five years, up more than 30% from where it is now. Customers' desire for natural beauty, as well as men's rising interest in 
skincare products, are driving this expansion. Anti-aging products are also being added by companies in order to keep women as their key customers as they age.

More customers began visiting the cosmetics counter for product recommendations, necessitating the need for improved technologies. This method, however, is frequently 
ineffectual and time-consuming. The overwhelming amount of information available on the internet has also made it difficult for consumers to make informed decisions. 
The quantity of product information and feedback is seen as beneficial. However, it prohibits consumers from selecting appropriate information and making decisions based 
on their requirements. As a result of this difficulties, there is a pressing demand for customized solutions that can make data access easier.

Researchers have proposed different recommender systems to resolve the information overloading problem and facilitate the selection process. The two most adopted methods 
are collaborative filtering and content-based filtering. Recently, a hybrid approach that combines the two techniques was introduced to maximize the benefits of both 
methods while covering their weaknesses.

There could be some people who share a very similar taste for cosmetics. And with user-user collaborative filtering, we can recommend new products based on the ranking 
values of this neighboring group. However, the skin type and feature of a person is a more sensitive and ticky problem than just recommending your tonight’s movie show.
To get the reliability and stability in the recommendation, we need to focus on the real content of each product, or the ingredients of products, and get the similarities based on them. Although a hybrid approach seems to have potential in the skincare domain, it requires a data set that involves both the behavioral information of the user as well as the product information. Such data set, however, is scarce in skincare.


## A.	DataSet

The data was scraped from sephora.com. This website offers beauty products from multiple brands. Among them six were extracted to focus on skincare products. These categories include moisturizing cream, facial treatments, cleanser, facial mask, eye treatment, and sun protection. Initially we scrapped the product links from the search page for each category and then information about each product is extracted from the links gathered. The data set includes information about the brand, name, price, rank, skin types, and chemical components of each product. The extraction is done using the library ‘Selenium’ that allows data mining from different websites. The data was extracted using the xpath of the element on the html page. This data set will be used specifically to evaluate the efficiency of this method after the implementation of the content-based recommender system.

## B.	Exploratory Data Analysis

### 1.	Data Preprocessing 

Data preprocessing is a data mining technique which is used to transform the raw data in a useful and efficient format. 

#### Steps Involved in Data Preprocessing:
#### (A) Data Cleaning

The raw data may contain a variety of meaningless and missing items. To deal with this, data cleaning is used. It requires coping with data that is absent or noisy.

1.Remove duplicate and unwanted data: Removed unwanted columns like URLs from the dataset.

2.Structural errors must be corrected: Structural error columns Label, ingredients, skin_type, price, and rating were fixed.

3.Handling missing values: We decided to handle the missing data on the bases of columns in which the data is missing. In columns like ingredients, we have dropped the row. And in columns like Skin_type, we replaced it with mode.

### 2.Feature Scaling
This step is conducted to convert the data into a format that can be used in the mining process. In order to use the skin type data, we apply one-hot encoding on that column.

### 3.Data Visualizations

Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

![alt text](/paper/Images/Label_analyisis.png?raw=true)
Fig 1: Distribution of products

Observation: Fig 1 shows the distribution of products in different categories and it seems that moisturizer has the highest number of products whereas sunscreen holds the least number. This may influence our final prediction.

![alt text](/paper/Images/Label_analyisis.png?raw=true)
Fig 2: Price distribution

Observation: In Fig 2 Most of the products lie in the range of 0 to $120 but for some premium products we can see that the price exceeds $500. Usually, the outliers are dropped or imputed but in this case, as the model is based on ingredients we can't impute the price column.

![alt text](/paper/Images/price_analysis.png?raw=true)
Fig 3: Rank Vs Price

Observation: In Fig 3 the graph depicts that the higher price of the product does not imply a better rank or rating. Variability in the rating of products is high from rank 2 to 3.

![alt text](/paper/Images/combination_skintype.png?raw=true)
![alt text](/paper/Images/sensitive_skintype.png?raw=true)
![alt text](/paper/Images/dry_skintype.png?raw=true)
![alt text](/paper/Images/mature_skintype.png?raw=true)
![alt text](/paper/Images/normal_skintype.png?raw=true)
![alt text](/paper/Images/oil_skintype.png?raw=true)

Fig 4: Product distribution based on Skintype

Observation: In fig 4 shows the distribution of products for each skin type. we can observe that there are negligible amount of products for Mature and Sensitive skin types.

![alt text](/paper/Images/mask.png?raw=true)
![alt text](/paper/Images/cleanse.png?raw=true)

Fig 5: wordclouds and classification

Observation: Fig 5 depicts that cleanser mainly contains Sodium, Lauryl, Acid, Water, and Ferment as their main ingredients.And Mask mainly contains Extract, Butylene, Glycol, and Water.

### 4.Ingredient Extraction

Initially, the collected data are filtered based on the user's skin type input. When a user selects a product, the system extracts its ingredients and sends them, along with the Sephora data set, to the recommender system. The list of all ingredients is extracted from the data set's ingredients column and divided into tokens. After the duplication has been checked, each chemical element is assigned a unique index that will be stored in a dictionary.

The document term matrix (DTM) is then created between the products and their corresponding ingredients. An empty matrix is created and then filled with zeros. The number of rows here represents the number of skincare products, while the number of columns represents the total number of ingredients. Then, depending on the presence of ingredients in each product, one-hot encoding is used to fill in the cosmetic-ingredient matrix with either 1 (present) or 0 (not present).


### 5.Dimensionality  Reduction

Dealing with very high-dimensional data is a common issue for data scientists nowadays (lots of features). Most algorithms for classification and prediction that work well with low-dimensional datasets don't work as well with many features, a problem known as the curse of dimensionality. To address this, we can reduce the number of dimensions through feature selection or feature extraction, typically by handpicking the most relevant features or using Principal Component Analysis (PCA) prior to feeding the data into our preferred model. Even though PCA is excellent in most cases, it is still a linear model that may be insufficient for some datasets. So, we have used t-SNE to reduce the dimensionality of the dataset.

t-Distributed Stochastic Neighbor Embedding (t-SNE) is a very popular and state-of-the-art dimensionality reduction technique that is usually used to map high to 2 or 3 dimensions in order to visualize it. It does so by computing affinities between points and trying to maintain these affinities in the new, low-dimensional space.

Using t-SNE on cosmetic-ingredient matrix we have reduced the dimensionality of the cosmetic-ingredient matrix from 452 to 2.

# II. METHODS

## 1. Content-based Filtering: 

The chemicals, together with the user's skin type, are submitted into the recommender system after they have been extracted and processed. This method compares the similarity of item constituent composition using cosine similarity. It's used to rank cosmetics with similar qualities to the original product by generating  recommendations for different product categories.



Using the resulting matrix, all cosmetic elements are vectorized into two-dimensional coordinates using t-SNE. The cosine similarity equation is used to calculate the distances between various locations using these coordinates. Finally, these values are ranked from most similar to least similar in ascending order. The method is repeated to filter the data by adding more product categories. The system can recommend products from a variety of categories by categorizing the data.




## 2. TF-IDF Filtering:

There is also a different technique that can be used to recommend skincare products based on the product entered. The top recommendations can be identified by calculating the TF-IDF values. The values are derived using the below equations.


𝑛𝑝: the number of unique ingredients included in product 𝑝 in
beauty effect group 𝑋
𝑚: the number of products in beauty effect group 𝑋
𝛼𝑝,𝑖: the rank of ingredient 𝑖 listed in product 𝑝



𝑁: the number of products in the data set
𝑝𝑓 (𝑖): the number of products including ingredient 𝑖


The similarity of the products represented as TF-IDF vectors is computed using the linear kernel. The products that include such ingredients are then filtered. Finally, the top recommendations are returned to the user. 


# III. COMPARISONS

The data that was gathered using web scraping consisted of information of ingredients and product type, no information was available of users or customers of the product. So quantifying of recommender systems is not possible this time. However we have manually compared the ingredients of the input product with the recommendations generated and found quite a lot of similarities and found that the TF IDF method of recommendation  was slightly better.

There are surveys usually conducted to test this kind of data [1]. In this paper the user liking is compared with the recommendations and it was found that the TF IDF method was slightly better than Content Based recommendation system.

# IV. CONCLUSION AND RESULTS

![alt text](/paper/Images/bokeh%20image.png?raw=true)

This report talks about the implementation of Content-Based recommendations and TF IDF-based recommendations. The bokeh plot in figure 6 shows the plot face_treatment with normal skin type. Each data point in the plot indicates the item and items with similar ingredients appear closer and if we hover over an item tooltip shows the name, brand, cost, and rating. By this, we can see what items are similar.
![alt text](/paper/Images/content_based_filter_result.png?raw=true)

In figure 7 we see the results of the content-based recommendation system. The input is “Peat Miracle Revital Cream”  top 5 items were chosen. The first one is the exact same because the cosine similarity to itself is 1.
![alt text](/paper/Images/TF_IDF_result.png?raw=true)

In figure 8 we see the results for the TF IDF recommendation system. The ingredients of recommended items were manually compared with the item selected and it was found that TF IDF was slightly better.

# V. LIMITATIONS AND FUTURE RESEARCH

Lack of access to customer information or any survey-based user liking was the main challenge. If this data were available then we can quantify the recommendation systems that are implemented. Once the user data is available we can also implement collaborative filtering and compare the recommendation among all the three recommendation systems.












