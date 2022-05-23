# Cosmetics-Recommendation
## CMPE 255 - Term project

## Team members
* Shrisha Shridhar Hegde - shrishashegde
* Soham Chandrakant Kasar - sohamkasar19
* Sai Sri Harshini Kosuri - Harshinikosuri
* Srikanth Nimmagadda - nisrika1

We are using the data that we got by web scraping and the data from OpenML. The link for the data set in openML is https://www.openml.org/search?type=data&status=active&id=43481&sort=runs

# Introduction

A cosmetic recommendation concerning skin trouble is a complex issue. It may react badly and cause skin inflammation. Consumers usually depend on recommended products from sellers i.e., best-selling products but these days one cannot blindly do this. We know the information we need is on the back of each product, but it’s hard to interpret those ingredient lists unless you’re a chemist. So, we decided to create a cosmetic recommendation system.

![alt text](/paper/cosmetics.jpg?raw=true)


There could be some people who share a very similar taste for cosmetics. And with user-user collaborative filtering, we can recommend new products based on the ranking values of this neighboring group. However, the skin type and feature of a person is a more sensitive and ticky problem than just recommending your tonight’s movie show.  To get the reliability and stability in the recommendation, we need to focus on the real content of each product, or the ingredients of products, and get the similarities based on them. Although a hybrid approach seems to have potential in the skincare domain, it requires a data set that involves both the behavioral information of the user as well as the product information. Such data set, however, is scarce in skincare.

# Procedure

As a first step, we would like to web scrap from Sephora. To focus on the skin care items, the dataset contains six different categories — moisturizing cream, facial treatments, cleanser, facial mask, eye treatment, and sun protection. We are aiming at restricting the dataset around 1500 items. We are thinking to also include the brand, the price, the rank(rating), skin types and ingredients for each item. These are the features included in the dataset link given above, for some reason if website does not mention some of these features we are thinking to replace it with any other feature or completely remove the feature.

In the second step we would like to use content-based recommendation system which is an unsupervised learningto cluster similar items together based on the ingredients in an item. The components of the content based recommender system would include creating Document Term Matrix (DTM). Here each cosmetic product will correspond to a document, and each chemical composition will correspond to a term. This means we can think of the matrix as a “cosmetic-ingredient” matrix.

As a final step we would like to use t-SNE dimensionality reduction technique to two dimensions and create a scatter plot. Each point in this scatter plot would indicate an item. The items having similar ingredients would appear closer to each other when compared to items having different ingredients.

# Design Implementation

The proposed system offers content-based filtering depending on if the user inputs a product in the beginning. After evaluating the similarity of ingredient composition within products, the system returns 𝑘 number of recommendations for each of the 𝑛 product types.


![alt text](/paper/project_flowchart.jpg?raw=true)

## Data Collection

The data was scraped from sephora.com. This website offers beauty products from multiple brands. Among them six were extracted to focus on skincare products. These categories include moisturizing cream, facial treatments, cleanser, facial mask, eye treatment, and sun protection. Initially we scrapped the product links from the search page for each category and then information about each product is extracted from the links gathered. The data set includes information about the brand, name, price, rank, skin types, and chemical components of each product. The extraction is done using the library ‘Selenium’ that allows data mining from different websites. The data was extracted using the xpath of the element on the html page. This data set will be used specifically to evaluate the efficiency of this method after the implementation of the content-based recommender system.


## Data cleaning
Data cleaning is the process of removing the data which is incorrect, wrongly formatted, duplicate data or incomplete dats within the dataset.
When the data is combined from multiple resources there is lot of duplicate or mislabeled data in combined csv file.
It removes the data that should not be included in the dataset.
### STEPS FOR DATA CLEANING:
1. Remove duplicate and unwanted data
2. Structural errors must be corrected: you may find “N/A” and “Not Applicable” as different, but they should be analyzed as the same category.
3. Outliers must be filtered:  Irrelevant outliers must be removed.
4. Handling missing values:
- we can drop the missing values but there is a chance of loosing the information
- Missing values can be filled with the assumptions from the observations but then there a chance of loosing integrity of the data, because the values are filled from assumptions not observations.
- Can be filled with null values.
5. Validate the cleaned dataset: before using the cleaned data validate it if it make sense then proceed with the cleaned csv file.





## Content based filtering
After the ingredients are extracted and processed they are passed into the recommender system with the user’s skin type. In this cosine similarity is applied to measure the ingredient similarity between products. Basically this is applied to produce k recommendations for n different product categories to rank cosmetics that have similar properties i.e similar ingredient list with the original product.
All cosmetic items are bought into two-dimensional coordinates. These values are arranged in ascending order from most to least similar products. This process is repeated by passing different product categories to filter data. Splitting the data set into different types allows the system to recommend products across multiple categories.

Initially, the collected data are filtered by the skin type input of the user. Once the user selects a product of their choice, the system extracts its ingredients and sends it to the recommender system along with the Sephora data set. The list of all ingredients are split into tokens. Once the duplication is checked, each chemical element is given a unique index to be stored in a dictionary. Next, the document term matrix (DTM) is created between the products and corresponding ingredients for each product. An empty matrix is initialized and filled with zeros. Here, the number of rows represents the number of skincare products, and the number of columns represents the number of total ingredients. Then, onehot encoding is used to fill in the cosmetic-ingredient matrix with either 1 (present) or 0 (not present), depending on the existence of ingredients in each product. 


# Visualizations

![alt text](/paper/label_histplot.jpg?raw=true)

This plot shows the distribution of products in different categories and it seems that moisturizer has the highest number of products whereas sunscreen holds the least number. This may influence our final prediction.


![alt text](/paper/price_boxplot.jpg?raw=true)

Most of the products lie in the range of 0 to $120 but for some premium products we can see that the price exceeds $500. Usually the outliers are dropped or imputed but in this case as the model is based on ingredients we can't impute the price column.


![alt text](/paper/price_vs_rank_lineplot.jpg?raw=true)

The graph depicts that higher price of the product does not imply better rank or rating. Variability in rating of products is high from rank 2 to 3.










