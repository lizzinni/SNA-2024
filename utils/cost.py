import pandas as pd
from geopy.distance import geodesic

reviews = pd.read_csv("reviews.csv")
items = pd.read_csv("items.csv")


def cost(detail_id_1, detail_id_2):
    """
    Рассчитывает время перемещения между двумя точками на основе расстояния между ними.
    """
    poi_1 = items[items['detail_id'] == detail_id_1]
    poi_2 = items[items['detail_id'] == detail_id_2]

    if poi_1.empty or poi_2.empty:
        return float('inf')

    coord_1 = (poi_1.iloc[0]['latitude'], poi_1.iloc[0]['longitude'])
    coord_2 = (poi_2.iloc[0]['latitude'], poi_2.iloc[0]['longitude'])
    distance = geodesic(coord_1, coord_2).kilometers
    travel_time = distance / 30 * 60

    return travel_time
