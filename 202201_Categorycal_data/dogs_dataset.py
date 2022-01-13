import pandas as pd
import os
link = "D:/One Drive Hino\OneDrive - Hino Motors VietNam/5_STUDY PROJECT/1_Datacamp Course/20220113_Working with categorical data"
print(os.getcwd())
os.chdir(link)
print(os.getcwd())
dogs = pd.read_csv("ShelterDogs.csv")
dogs.info()

#set categories
dogs["coat"] = dogs["coat"].astype("category")
dogs["coat"] = dogs["coat"].cat.set_categories(new_categories=["short", "medium", "long"])
print(dogs["coat"].value_counts(dropna=False))
