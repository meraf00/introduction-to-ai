def load_romania_coords(filename):
    city_coords = {}

    with open(filename) as file:
        for line in file.readlines()[1:]:
            city, lat, long = line.split("    ")
            lat = float(lat)
            long = float(long)

            city_coords[city] = [lat, long]

    return city_coords


print(load_romania_coords("clean\Romania\RomaniaCoords.txt"))
