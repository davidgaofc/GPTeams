import math
import matplotlib.pyplot as plt
import random

def create_points(num_points):
    return [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_points)]

def calculate_distances(points):
    distances = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            distances[(i, j)] = dist
    return distances

def find_closest_points(points, distances):
    closest_pair = min(distances, key=distances.get)
    return points[closest_pair[0]], points[closest_pair[1]]

def draw_points(points, hull=None):
    plt.scatter(*zip(*points))
    if hull:
        for i in range(len(hull)):
            plt.plot(*zip(*hull[i:i+2]), color='red')
        plt.plot(*zip(*[hull[-1], hull[0]]), color='red')  # Closing the hull
    plt.show()

def calculate_centroid(points):
    x_mean = sum(point[0] for point in points) / len(points)
    y_mean = sum(point[1] for point in points) / len(points)
    return x_mean, y_mean

def sort_points_by_angle(points, centroid):
    def angle_from_centroid(point):
        return math.atan2(point[1] - centroid[1], point[0] - centroid[0])
    return sorted(points, key=angle_from_centroid)

def calculate_area_of_polygon(points):
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def is_point_inside_polygon(point, polygon):
    crossings = 0
    x, y = point
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            crossings += 1
    return crossings % 2 != 0

# TODO: Implement calculate_convex_hull function
def calculate_convex_hull(points):
    """
        Calculates the convex hull of a given set of 2D points.
        Input:
            points: List of tuples [(x1, y1), (x2, y2), ..., (xn, yn)].
        Output:
            List of tuples representing the vertices of the convex hull, ordered along its perimeter.
    """
    n = len(points)
    if n <= 3:
        return points

    def orientation(p, q, r):
        """
        Finds the orientation of three points.
        Output:
            0: Collinear
            1: Clockwise
            2: Counterclockwise
        """
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    hull = []

    # Find the leftmost point
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i

    p = l
    q = (p + 1) % n

    while True:
        hull.append(points[p])
        o = orientation(points[p], points[q], points[i])

        if o == 2:
            q = i

        p = q
        q = (q + 1) % n

        if p == l:
            break

    return hull