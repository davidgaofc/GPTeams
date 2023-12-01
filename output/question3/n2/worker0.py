```python
import math

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

def calculate_convex_hull(points):
    """
        Calculates the convex hull of a given set of 2D points.
        Input:
            points: List of tuples [(x1, y1), (x2, y2), ..., (xn, yn)].
        Output:
            List of tuples representing the vertices of the convex hull, ordered along its perimeter.
    """
    hull = []
    if len(points) < 3:
        return hull
    
    sorted_points = sorted(points)
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    
    hull.append(sorted_points[0])
    hull.append(sorted_points[1])
    
    for i in range(2, len(sorted_points)):
        hull.append(sorted_points[i])
        while len(hull) > 2 and cross_product(hull[-3], hull[-2], hull[-1]) <= 0:
            hull.pop(-2)
    
    return hull
```