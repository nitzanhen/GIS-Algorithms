from math import radians, sin, cos, sqrt, asin

R = 6371  # Km; this is Earth's radius.


def spherical_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    """
    Calculates the great circle distance given the latitudes and longitudes of two points.

    TODO refactor to lat-lon class of some sort, maybe extract conversion of coords to radians outside.
    """
    # Phi is the angle corresponding to latitude in spherical coordinated, and lambda is the angle corresponding to longitude.
    phi1 = radians(lat1)
    lambda1 = radians(lon1)
    phi2 = radians(lat2)
    lambda2 = radians(lon2)

    dphi = phi2 - phi1
    dlambda = lambda2 - lambda1

    # Use the Haversine formula
    alpha = sin(dphi / 2) ** 2 + cos(phi1)*cos(phi2)*sin(dlambda / 2) ** 2
    c = 2 * asin(min(1, sqrt(alpha)))
    d = c * R

    return d


if __name__ == "__main__":
    lat1, lon1 = 31.9261858427916, 34.86515937464347  # Somewhere in Ramla
    lat2, lon2 = 32.00533180757691, 34.94436605385349  # Somewhere in Shoham
    distance = spherical_distance(lat1, lon1, lat2, lon2)
    google_distance = 11.62

    print(f"{lat1, lon1}, {lat2, lon2}")
    print(
        f"The distance according to this calculation is {round(distance, 3)} km.")
    print(f"According to Google it's {google_distance} km.")
    print(f"The difference is {round(abs(google_distance - distance), 3)}km")

    lat1, lon1 = 31.78173391903297, 34.88138701166011
    lat2, lon2 = 31.62600339993675, 34.96417016358551
    distance = spherical_distance(lat1, lon1, lat2, lon2)
    google_distance = 18.83

    print(f"{lat1, lon1}, {lat2, lon2}")
    print(
        f"The distance according to this calculation is {round(distance, 3)} km.")
    print(f"According to Google it's {google_distance} km.")
    print(f"The difference is {round(abs(google_distance - distance), 3)}km")

    lat1, lon1 = 31.759668533315963, 35.15400909714414
    lat2, lon2 = 31.75784599297399, 35.151055433123986
    distance = spherical_distance(lat1, lon1, lat2, lon2)
    google_distance = 0.34412

    print(f"{lat1, lon1}, {lat2, lon2}")
    print(
        f"The distance according to this calculation is {round(distance, 3)} km.")
    print(f"According to Google it's {google_distance} km.")
    print(f"The difference is {round(abs(google_distance - distance), 3)}km")
