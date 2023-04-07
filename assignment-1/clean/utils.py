from graph import UndirectedGraph


def load_coords(filename):
    city_coords = {}

    with open(filename) as file:
        for line in file.readlines()[1:]:
            city, lat, long = line.split("    ")
            lat = float(lat)
            long = float(long)

            city_coords[city] = [lat, long]

    return city_coords


def load_city_graph(filename, distance_unit="miles"):
    graph = UndirectedGraph()

    with open(filename) as file:
        for line in file.readlines()[1:]:
            city_1, city_2, distance = line.split("    ")

            distance = int(distance)

            if distance_unit == "km":
                distance *= 1.60934

            graph.add_edge(city_1, city_2, distance)

    return graph


# print(load_city_graph("clean/RomaniaData/RomaniaRoadDistance.txt"))
# print(load_city_graph("clean/RomaniaData/RomaniaRoadDistance.txt", "km"))
