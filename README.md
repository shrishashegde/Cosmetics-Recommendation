![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

# Cosmetics-Recommendation
## CMPE 255 - Term project

## Team members
* Shrisha Shridhar Hegde - shrishashegde
* Soham Chandrakant Kasar - sohamkasar19
* Sai Sri Harshini Kosuri - Harshinikosuri
* Srikanth Nimmagadda - nisrika1

We are using the data that we got by web scraping and the data from OpenML. The link for the data set in openML is https://www.openml.org/search?type=data&status=active&id=43481&sort=runs

# Folder structure

```shell
Cosmetics-Recommendation/
├── code
│   ├── 01_Scrapping.py
│   ├── 02_Preprocessing.py
│   ├── 03_Data_analysis.ipynb
│   ├── 04_Modelling.py
│   └── 05_Visualisation.ipynb
├── data
│   ├── cosmetic.csv
│   ├── 255 Presentation.pptx
│   ├── cosmetic_TSNE.csv
│   └── cosmetic_preprocess.csv
├── paper
│   ├── Images
│   ├── final.md
│   └── report.pdf
├── license   
├── readme.md
└── requirements.txt
```
# Installation

Installation of below packages required before running the project

* `pip install -r requirements.txt`
  
# Steps to run the project

1. Create a folder in local for Above Git Repo and open in termianl to execute below commands-

    `$ git clone https://github.com/rohit-chandra/Customer_Churn_Analysis.git`

2. In the root folder run `python code/01_Scrapping.py`
3. In the root folder run `python code/02_Preprocessing.py`
4. In the root folder run `python code/04_Modelling.py`
5. Navigate to code folder and run 03_Data_analysis.ipynb in jupyter notebook
6. Navigate to code folder and run 05_Visualisation.ipynb in jupyter notebook

The complete report can be found in [final.md](paper/final.md)
