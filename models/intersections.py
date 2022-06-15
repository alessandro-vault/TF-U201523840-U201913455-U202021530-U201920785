

class Intersection:
    def __init__(self, identifier, street_id, street_name, origin_id, final_id,
                 origin_intersection_id, final_intersection_id, distance,
                 speed, cost_1, cost_2, origin_lat, origin_lon, final_lat,
                 final_lon):
        self.identifier = int(identifier)
        self.street_id = int(street_id)
        self.street_name = street_name
        self.origin_id = int(origin_id)
        self.final_id = int(final_id)
        self.origin_intersection_id = int(origin_intersection_id)
        self.final_intersection_id = int(final_intersection_id)
        self.distance = distance
        self.speed = speed
        self.cost_1 = cost_1
        self.cost_2 = cost_2
        self.origin_lat = origin_lat
        self.origin_lon = origin_lon
        self.final_lat = final_lat
        self.final_lon = final_lon

    def origin_coords(self):
        return self.origin_lat, self.origin_lon

    def final_coords(self):
        return self.final_lat, self.final_lon



class Intersections:
    def __init__(self):
        self.intersections = []

    def add_intersection(self, *args):
        self.intersections.append(Intersection(*args))

    def first(self):
        return self.intersections[0]

    def __len__(self):
        return len(self.intersections)
