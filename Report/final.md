Abstract- Consumer interest in cosmetics has risen globally in recent years, with a focus on skincare. Consumers have previously relied on best-seller products or 
in-store counter recommendations. However, because everyone's skin is different, these are ineffective ways for determining whether a product and a person are compatible.
The goal of this proposal is to create a skincare product recommendation system based on the user's skin type and the product's ingredient composition. 
Product chemical components are identified and products with similar constituent compositions are found using content-based filtering.

# INTRODUCTION

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


#### (B) Outlier Detection




