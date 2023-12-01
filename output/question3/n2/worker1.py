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
    # Sort points by x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Define helper functions

    def orientation(p, q, r):
        """
        Returns the orientation of three points (p, q, r).
        :return:
            0 if p, q, r are collinear,
            1 if clockwise,
            2 if counterclockwise.
        """
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        elif val > 0:
            return 1  # Clockwise
        else:
            return 2  # Counterclockwise

    # Initialize an empty stack
    stack = []

    # Add first three points to the stack
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])
    stack.append(sorted_points[2])

    # Process remaining points
    for i in range(3, len(sorted_points)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()

        stack.append(sorted_points[i])

    return stack
```