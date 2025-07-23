# Import geopandas and pandas
import geopandas as gpd
import pandas as pd

# Read the shapefile of India [give the  file path for the big data .shp file]
india = gpd.read_file(r"D:\23_07_25\India_district\IND_adm3.shp")
print(india)
# Read the csv file of district names [give the file path for the csv file]
districts = pd.read_csv(r"D:\23_07_25\csv_files\Rajasthan.csv")

# Convert the district names to a list
district_list = districts.iloc[:,0].tolist()
print(district_list)
dist_list = [i.split(' District')[0] for  i in district_list]
print(dist_list)


# Filter the India shapefile by the district names
india_districts = india[india["NAME_2"].isin(dist_list)]
print(india_districts)


# union of the features by NAME_2

india_districts = india_districts.dissolve(by="NAME_2")


# # Save the filtered shapefile as a new file
india_districts.to_file(r"D:\23_07_25\raj.shp")

