"""
# Geoscripting
# Exercise 9
# Route with Postbox
# Stater
# Group: able panther of judgment
# 24/10/2022
"""
# Load required packages and our functions file
import os
import folium
import matplotlib.pyplot as plt
import functions_exc9 as funcs

# Create data and output folders
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists('output'):
    os.makedirs('output')

# Get data for this exercise
routesGDF = funcs.getRoutes()
postBoxesGDF = funcs.getPOIs()

# Plot them for a first visual inspection
routeslayer = routesGDF.plot()
postBoxesGDF.plot(ax=routeslayer, color='red')
plt.show()

# Task 1
# Assign GDF of potential routes to a variable called routesWithPOI

routesWithPOI=funcs.selectRoutesWithPOI(routesGDF, postBoxesGDF)

# Perform an intersection routes
routesWithPOI.plot(color="orange")
print(routesWithPOI)

# Task 2
# Add an attribute routelength to routesWithPOI
# ref1: https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.length.html
routeLength= routesWithPOI['geometry'].length

# Using 'routelength' as the column name
# and equating it to the list
routesWithPOI['routelength']=routeLength


# Check if there are solutions, if more than 1 select shortest route option
# ref2: https://sparkbyexamples.com/pandas/get-first-row-of-pandas-dataframe/
if all(list(routesWithPOI.isna())) == False:
    bestRoute= routesWithPOI.sort_values(by='routelength').iloc[:1].to_crs(4326)

# Select POI that is on the best route
import geopandas as gpd

closestpoint = gpd.sjoin_nearest(bestRoute, postBoxesGDF)
poiOnRoute = postBoxesGDF[postBoxesGDF.POInr == list(closestpoint['POInr'])[0]]


# Task 3
# Plot best route option on folium map
# Initialize the map
campusMap = folium.Map([51.98527485, 5.66370505205543], zoom_start=15)

# Add the POI
folium.GeoJson(poiOnRoute, style_function=lambda x: {"fillColor": "#ff0000"}).add_to(campusMap)

# Add the bestroute
folium.GeoJson(bestRoute).add_to(campusMap)

# Add layer control
folium.LayerControl().add_to(campusMap)

# Save (you can now open the generated .html file from the output directory)
campusMap.save('output/campusMap.html')

# Extra
# Calculate the detour (meters) John is cycling to pass by a postbox compared to the shortest route regardless a postbox
bestLength = bestRoute['routelength']
minLength = routesGDF['geometry'].length
detourForJohn = bestLength.min()  - minLength.min()
print('The detour is %.2f metres.'%detourForJohn)


