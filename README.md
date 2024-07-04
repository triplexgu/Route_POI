# A postbox on your way to campus

## Requirements
- Task 1: Create a function `selectRoutesWithPOI()` that takes a GDF of routes (multipolylines as given by `getRoutes()` and a GDF of POIs (points as given by `getPOIs()`) and returns the selection of routes that have a POI close to the road (within a given euclidean distance (default=10m)). Apply your function to the case of John and find out which routes have a postbox close to it within 10 meters from the road. Assign the resulting GDF of potential routes to a variable called `routesWithPOI`.

- Task 2: For the GDF `routesWithPOI` add an attribute `routelength` and calculate the length of these routes for this column in meters. Create a few lines of code that select the best route for John; it should have a postbox within 10m and be the shortest possible. Assign this one best solution to a variable `bestRoute`. Find out which postbox is actually close to the route of `bestRoute` and assign this one postbox to a variable `poiOnRoute`.

- Task 3: Create a nice-looking folium map that shows both the best route for John and the postbox that he will pass-by. Save the plot as `bestRouteForJohn.html` in your output folder. During all three tasks, pay attention to the documentation and structure of your Python scripts.

## Extra (only attempt if you finished and tested the above without errors)
Calculate the detour (meters) John is cycling to pass by a postbox compared to the shortest route regardless a postbox. Assign this distance to a variable `detourForJohn`.
