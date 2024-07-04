# Exercise 9: A postbox on your way to campus

## Your task
John is leaving his home and heading to campus for an early morning lecture. He is in a hurry and actually a bit late. While walking through the hallway to the front door he sees a letter that really needs to be posted today. As John is not used to send handwritten letters anymore, he has no clue where there is a postbox on his way to the Wageningen campus. 

Your task of today is to help out John. Find out what the shortest route is to the Wageningen Campus that has a postbox close to the road.


## Details
A starter and some functions are already given for this exercise. See also the explanation and description of the given functions in the file `functions_exc9.py`.

Use the conda environment `vector` you created during the tutorial.

Work with a project structure, and use the `main.py` module that imports functions from `functions_exc9.py`. These functions are already given for this exercise:
- `getRoutes()` => This function calculates a number of shortest routes from start point to end point. Use default values and it provides you a GeoDataFrame (GDF) with the ten shortest route options for John. 
- `getPOIs()` => This function extracts Points Of Interest from OSM. With default values it will provide you the postboxes within Wageningen Municipality as a GeoDataFrame (GDF).


## Requirements
- Task 1: Create a function `selectRoutesWithPOI()` that takes a GDF of routes (multipolylines as given by `getRoutes()` and a GDF of POIs (points as given by `getPOIs()`) and returns the selection of routes that have a POI close to the road (within a given euclidean distance (default=10m)). Apply your function to the case of John and find out which routes have a postbox close to it within 10 meters from the road. Assign the resulting GDF of potential routes to a variable called `routesWithPOI`.

- Task 2: For the GDF `routesWithPOI` add an attribute `routelength` and calculate the length of these routes for this column in meters. Create a few lines of code that select the best route for John; it should have a postbox within 10m and be the shortest possible. Assign this one best solution to a variable `bestRoute`. Find out which postbox is actually close to the route of `bestRoute` and assign this one postbox to a variable `poiOnRoute`.

- Task 3: Create a nice-looking folium map that shows both the best route for John and the postbox that he will pass-by. Save the plot as `bestRouteForJohn.html` in your output folder. During all three tasks, pay attention to the documentation and structure of your Python scripts.


## Hints
- If you need some help how to make functions or how to import modules, have a look at the code in the Python refresher and the references mentioned there at the end. 
- For Task 3, you might want to get inspired by https://anitagraser.com/2019/10/31/interactive-plots-for-geopandas-geodataframe-of-linestrings/.


## Extra (only attempt if you finished and tested the above without errors)
Calculate the detour (meters) John is cycling to pass by a postbox compared to the shortest route regardless a postbox. Assign this distance to a variable `detourForJohn`.
