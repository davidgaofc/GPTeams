```python

import math
import matplotlib.pyplot as plt

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

def calculate_convex_hull(points):
    """
        Calculates the convex hull of a given set of 2D points.
        Input:
            points: List of tuples [(x1, y1), (x2, y2), ..., (xn, yn)].
        Output:
            List of tuples representing the vertices of the convex hull, ordered along its perimeter.
    """
    hull = []

    # Sort points in increasing order of x coordinate
    points = sorted(points, key=lambda x: x[0])

    # Find the lower hull
    for point in points:
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    # Find the upper hull
    upper_hull = []
    for point in reversed(points):
        while len(upper_hull) >= 2 and ccw(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)

    # Remove the first and last points of the upper_hull to avoid duplicates
    upper_hull = upper_hull[1:-1]

    # Combine the lower hull and upper hull to form the convex hull
    convex_hull = hull + upper_hull

    return convex_hull

def ccw(p1, p2, p3):
    """
        Determines if three points are in counter-clockwise order.
        Input:
            p1, p2, p3: Tuples representing 2D points (x, y).
        Output:
            Positive value if points are in counter-clockwise order, negative if in clockwise order,
            and 0 if they are collinear.
    """
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

```