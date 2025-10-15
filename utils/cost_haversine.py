import math
import numpy as np
import pandas as pd
from haversine import haversine

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

    lat1, lon1 = poi_1.iloc[0]['latitude'], poi_1.iloc[0]['longitude']
    lat2, lon2 = poi_2.iloc[0]['latitude'], poi_2.iloc[0]['longitude']
    distance = haversine(lat1, lon1, lat2, lon2)
    travel_time = distance / 30 * 60  # если скорость = 30 км/ч

    return travel_time
