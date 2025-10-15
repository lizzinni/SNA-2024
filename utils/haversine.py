import math
import numpy


def haversine(lat1, lon1, lat2, lon2):
    """
    Вычисляет расстояние между двумя точками на Земле
    по их широте и долготе с использованием формулы хаверсина.
    """

    # Радиус Земли в километрах
    R = 6371.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # print(lat1_rad, lon1_rad, lat2_rad, lon2_rad)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Формула хаверсина
    # a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    a = numpy.sin(dlat / 2) ** 2 + numpy.cos(lat1_rad) * numpy.cos(lat2_rad) * numpy.sin(dlon / 2) ** 2
    c = 2 * numpy.arcsin(numpy.sqrt(a))

    distance = R * c
    return distance


lat_moscow, lon_moscow = 55.7558, 37.6173
lat_spb, lon_spb = 59.9311, 30.3609

distance = haversine(lat_moscow, lon_moscow, lat_spb, lon_spb)
print(f"Расстояние между Москвой и Санкт-Петербургом: {distance:.8f} км")
