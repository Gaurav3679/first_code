# Import geopandas and pandas
import geopandas as gpd
import pandas as pd

# Read the shapefile of India
india = gpd.read_file("D:\Aritra_work\India_Adm\IND_adm3.shp")

# Read the csv file of district names
districts = pd.read_csv("D:\Aritra_work\Bauxite\Orissa\docs.csv")

# Convert the district names to a list
district_list = districts.iloc[:,0].tolist()
print(district_list)

# Filter the India shapefile by the district names
india_districts = india[india["NAME_2"].isin(district_list)]
print(india_districts)

# # Save the filtered shapefile as a new file
india_districts.to_file("D:\Aritra_work\Bauxite\Orissa\dist.shp")
