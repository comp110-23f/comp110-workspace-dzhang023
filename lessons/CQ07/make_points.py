"""Docstring."""

from lessons.CQ07.point import Point


point_a: Point = Point(5.0, 7.0)
point_a.scale_by(2)
print(point_a.x, point_a.y)
point_b: Point = point_a.scale(3)
print(point_b.x, point_b.y)