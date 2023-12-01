```python
def calculate_convex_hull(points):
    """
        Calculates the convex hull of a given set of 2D points.
        Input:
            points: List of tuples [(x1, y1), (x2, y2), ..., (xn, yn)].
        Output:
            List of tuples representing the vertices of the convex hull, ordered along its perimeter.
    """
    sorted_points = sort_points_by_angle(points, calculate_centroid(points))
    hull = [sorted_points[0], sorted_points[1]]
    for i in range(2, len(sorted_points)):
        while len(hull) >= 2 and (hull[-1][1] - hull[-2][1]) * (sorted_points[i][0] - hull[-2][0]) - (hull[-1][0] - hull[-2][0]) * (sorted_points[i][1] - hull[-2][1]) <= 0:
            hull.pop()
        hull.append(sorted_points[i])
    return hull
```