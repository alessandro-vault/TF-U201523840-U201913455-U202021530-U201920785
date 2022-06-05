

class Intersection:
    def __init__(self, identifier, street_id, street_name, origin_id, final_id,
                 origin_intersection_id, final_intersection_id, distance,
                 speed, cost_1, cost_2, origin_lat, origin_lon, final_lat,
                 final_lon):
        identifier = int(identifier)
        street_id = int(street_id)
        street_name = street_name
        origin_id = int(origin_id)
        final_id = int(final_id)
        origin_intersection_id = int(origin_intersection_id)
        final_intersection_id = int(final_intersection_id)
        distance = distance
        speed = speed
        cost_1 = cost_1
        cost_2 = cost_2
        origin_lat = origin_lat
        origin_lon = origin_lon
        final_lat = final_lat
        final_lon = final_lon

    def __len__(self):
        return len(self.intersections)


class Intersections:
    def __init__(self):
        self.intersections = []

    def add_intersection(self, *args):
        self.intersections.append(Intersection(*args))

    def first(self):
        return self.intersections[0]

    def __len__(self):
        return len(self.intersections)
