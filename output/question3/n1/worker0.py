```python
import math

def calculate_convex_hull(points):
    """
        Calculates the convex hull of a given set of 2D points.
        Input:
            points: List of tuples [(x1, y1), (x2, y2), ..., (xn, yn)].
        Output:
            List of tuples representing the vertices of the convex hull, ordered along its perimeter.
    """
    def orientation(p, q, r):
        """
            Helper function to calculate the orientation of three points.
            Returns:
                0 if three points are collinear
                1 if they are clockwise
                2 if they are counterclockwise
        """
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def get_next_point(points, p):
        """
            Helper function to get the next point on the convex hull.
        """
        q = (p[0], p[1])
        while True:
            next_point = (points[0][0], points[0][1])
            for i in range(1, len(points)):
                if (orientation(p, next_point, points[i]) == 2 or
                        (orientation(p, next_point, points[i]) == 0 and
                         calculate_distance(p, points[i]) > calculate_distance(p, next_point))):
                    next_point = (points[i][0], points[i][1])
            return next_point

    def calculate_distance(p1, p2):
        """
            Helper function to calculate the Euclidean distance between two points.
        """
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    # Sort the points lexicographically (by x-coordinate, then by y-coordinate)
    points = sorted(points, key=lambda x: (x[0], x[1]))

    # Initialize an empty stack to store the convex hull
    hull = []

    # Find the leftmost point and add it to the hull
    leftmost_point = points[0]
    hull.append(leftmost_point)

    # Start from the leftmost point and keep adding the next point of the convex hull until we reach the starting point again
    p = leftmost_point
    while True:
        q = get_next_point(points, p)
        if q == leftmost_point:
            break
        hull.append(q)
        p = q

    return hull
```