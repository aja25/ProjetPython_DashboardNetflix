import os
import pandas as pd
import numpy as np 

# Recuperation du dataset sur kaggle 

def download_data_set():
    print("Downloading data set ...")
    print("Hello world")
    kaggle_data={"username":"ajanannavendran","key":"07e60dd137cceb2063b1bdba04190dd6"}
    os.environ['KAGGLE_USERNAME'] = kaggle_data["username"]
    os.environ['KAGGLE_KEY'] = kaggle_data["key"]
    import kaggle
    kaggle.api.dataset_download_files('shivamb/netflix-shows', path='./data', unzip=True)
    if os.path.exists("data/netflix-shows.zip"):
        os.remove("data/netflix-shows.zip")

#Import de la data
def read_csv():
    df = pd.read_csv('data/netflix_titles.csv',
                     names=["show_id","type","title","director","cast","country","date_added","release_year","rating","duration","listed_in","description"],
                     dtype={"type": str, "listes_in": str},
                     )
    print("Read .csv done.")
    return df



# Filling missing values
def clean_data(data):
    print("Cleaning the dataset")
    #data['date_added'] = pd.to_datetime(data['date_added']).dt.year
    data['director'].replace(np.nan, 'No Director',inplace=True)
    data= data.dropna(subset=['country'])
    #data['cast'].replace(np.nan, 'No Cast',inplace=True)
    data.isnull().sum()
    #print(data['rating'])
    #data['rating'] = data['rating'].replace({'74 min': np.nan, '84 min': np.nan, '66 min': np.nan, 'G': 'TV-G'})
    data['rating'].unique()
    data['type'].value_counts()
    return data



def main(): 
    download_data_set()
    df=read_csv()
    data = clean_data(df)
    #print(df.head())

    return data

if __name__ == "__main__":
    main()