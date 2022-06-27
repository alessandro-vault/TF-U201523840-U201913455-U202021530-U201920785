import random


class Intersection:
    def __init__(
        self,
        identifier,
        street_id,
        street_name,
        origin_id,
        final_id,
        origin_intersection_id,
        final_intersection_id,
        distance,
        speed,
        cost_1,
        cost_2,
        origin_lat,
        origin_lon,
        final_lat,
        final_lon,
    ):
        self.identifier = int(identifier)
        self.street_id = int(street_id)
        self.street_name = street_name
        self.start_id = int(origin_id)
        self.end_id = int(final_id)
        self.start_intersection_id = int(origin_intersection_id)
        self.end_intersection_id = int(final_intersection_id)
        self.distance = distance
        self.speed = speed
        self.cost_1 = cost_1
        self.cost_2 = cost_2
        self.start_coords = float(origin_lat), float(origin_lon)
        self.end_coords = float(final_lat), float(final_lon)

    def __repr__(self):
        return f"<Intersection {self.identifier}: {self.start_coords} -> {self.end_coords}>"


class Intersections:
    def __init__(self):
        self.intersections = []

    def add_intersection(self, *args):
        self.intersections.append(Intersection(*args))

    # ! QUERY
    def first(self):
        return self.intersections[0]

    def find(self, identifier):
        for intersection in self.intersections:
            if intersection.identifier == identifier:
                return intersection

    def start_coords(self):
        return set([x.start_coords for x in self.intersections])

    def find_by(self, street):
        result = []
        for intersection in self.intersections:
            if intersection.street_id == street.identifier:
                result.append(intersection)
        return random.sample(result, 1)[0]
    # ? FUNCTIONS
    def __iter__(self):
        return iter(self.intersections)

    def __len__(self):
        return len(self.intersections)

    def __repr__(self):
        return f"<Intersections @count={len(self)}>"
