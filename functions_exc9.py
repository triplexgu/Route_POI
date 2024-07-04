""""
# Geoscripting
# Exercise 9
# Route with Postbox
# Stater - functions
# Group: able panther of judgment
# 24/10/2022
"""


def getPOIs(placename='Wageningen, Netherlands', poi='postbox'):
    """Function that extracts OSM geometries. For OSM tags available see
    https://wiki.openstreetmap.org/wiki/Map_Features"""
    import osmnx as ox

    # Acquire POIs (mailboxes) from osm
    if poi == 'postbox':
        tags = {'amenity': 'post_box'}
    else:
        tags = {'amenity': True}
    gdf = ox.geometries.geometries_from_place(placename, tags)
    gdf = ox.project_gdf(gdf)  # reproject to local UTM zone

    # Add POI labels
    gdf['POInr'] = range(1, len(gdf) + 1)
    gdf['POInr'] = 'POI_' + gdf['POInr'].astype(str)

    return gdf


def routeToWKT(oxroute, graph):
    """ Function that takes a OSMNX graph and route calculated over it.
    Function converts the route (represented as list of nodes) to a
    multilinestring in WKT format"""
    import osmnx as ox
    from shapely.geometry import MultiLineString

    route_pairwise = zip(oxroute[:-1], oxroute[1:])

    # Get the edges and sort index for performance (to prevent warning)
    edges = ox.graph_to_gdfs(G=graph, nodes=False).sort_index()
    lines = [edges.loc[uv, 'geometry'].iloc[0] for uv in route_pairwise]
    geom = MultiLineString(lines).wkt

    return geom


def routesToGDF(oxroutes, graph):
    """Function to load WKT formatted routes (multilinestring) into
    GeoDataFrame, projected to local UTM zone.
    Function converts one or more routes, based on number of elements in input
    variable OXroutes"""
    import osmnx as ox
    import pandas as pd
    import geopandas as gpd
    from shapely import wkt

    wktroutes = [routeToWKT(oxroute, graph) for oxroute in oxroutes]
    df = pd.DataFrame.from_dict(dict(enumerate(wktroutes)).items())
    df['geometry'] = df[1].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs='epsg:4326')
    gdf = ox.project_gdf(gdf)  # reproject to local UTM zone

    return gdf


def getRoutes(placename='Wageningen, Netherlands',
              source='Bosrandweg 1, Wageningen, Netherlands',
              target='Droevendaalsesteeg 3, Wageningen, Netherlands',
              routecount=10, travelmode='drive'):
    """Function that takes a city of interest, start and end address.
    Extracts network graph for the city and calculates number of shortest
    routes from start to end address.
    Returns GDF with shortest routes in local UTM zone."""
    import osmnx as ox

    g = ox.graph.graph_from_place(placename, network_type=travelmode)
    sourcenode = ox.nearest_nodes(g, ox.geocoder.geocode(source)[1],
                                  ox.geocoder.geocode(source)[0])
    targetnode = ox.nearest_nodes(g, ox.geocoder.geocode(target)[1],
                                  ox.geocoder.geocode(target)[0])
    shortestroutes = list(ox.k_shortest_paths(k=routecount, G=g,
                                              orig=sourcenode,
                                              dest=targetnode, weight='length'))

    return routesToGDF(shortestroutes, g)

''' Task 1 '''
# Select the routes with points´
def selectRoutesWithPOI(routes,boxes):
    # Add the package
    import geopandas as gpd
    
    # Create buffer zones and select the intersect routes
    BoxesbufferGDF = gpd.GeoDataFrame(boxes, geometry=boxes.buffer(distance=10))
    InterRoutes = gpd.overlay(routes, BoxesbufferGDF , how="intersection")
    
    return routes.iloc[list(InterRoutes[0])]