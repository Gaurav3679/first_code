# Import geopandas and pandas
import geopandas as gpd
import pandas as pd

# Read the shapefile of India
india = gpd.read_file(r"give the  file path for the big data .shp file")

# Read the csv file of district names
districts = pd.read_csv(r"give the file path for the csv file")

# Convert the district names to a list
district_list = districts.iloc[:,0].tolist()
print(district_list)

# Filter the India shapefile by the district names
india_districts = india[india["NAME_2"].isin(district_list)]
print(india_districts)


# union of the features by NAME_2

india_districts = india_districts.dissolve(by="NAME_2")


# # Save the filtered shapefile as a new file
india_districts.to_file(r"provide the output file path")

