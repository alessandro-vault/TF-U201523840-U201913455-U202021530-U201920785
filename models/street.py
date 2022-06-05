class Street:
    def __init__(self, _id, name, intersection_count):
        self._id = _id
        self.name = name
        self.intersection_count = intersection_count

    def __repr__(self):
        return f"<Street: @id={self._id} @name={self.name} @intersection_count={self.intersection_count}>"