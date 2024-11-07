import pandas as pd
from geopy.distance import geodesic

reviews = pd.read_csv("reviews.csv")
items = pd.read_csv("items.csv")


def score(detail_id):
    """
    Рассчитывает средний рейтинг для указанной точки интереса (POI).
    """
    poi_reviews = reviews[reviews['detail_id'] == detail_id]
    if len(poi_reviews) == 0:
        return 0
    return poi_reviews['mark'].mean()