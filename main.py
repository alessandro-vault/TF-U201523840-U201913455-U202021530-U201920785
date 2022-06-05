from helper.load_data import load
from models.database import Database

data = Database()
load(data)

print(len(data.streets))
print(len(data.intersections))
