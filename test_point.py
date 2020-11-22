# -*- coding: utf-8 -*-
from point import Point


def test_should_check_constructor_without_z():
    # given
    point_a = Point('A', 1, 1)

    # when
    # then
    assert point_a.name == 'A'
    assert point_a.x == 1
    assert point_a.y == 1
    assert point_a.z == 0


def test_should_check_constructor_with_z():
    # given
    point_a = Point('A', 1, 1, 1)

    # when
    # then
    assert point_a.name == 'A'
    assert point_a.x == 1
    assert point_a.y == 1
    assert point_a.z == 1


def test_should_check_print_method():
    # given
    point_a = Point('A', 1, 1, 1)

    # when
    # then
    assert point_a.__str__() == 'Point(nr="A", x=1, y=1, z=1)'


def test_should_check_get_length():
    # given
    begin_point = Point('P1245', 0, 0)
    end_point = Point('P12', 3, 4)
    end_point_3d = Point('P12', 3, 4, 1)

    # when
    # then
    assert begin_point.get_length(begin_point) == 0
    assert begin_point.get_length(end_point) == 5
    assert end_point.get_length(begin_point) == 5

    assert begin_point.get_length(begin_point, _3d=True) == 0
    assert begin_point.get_length(end_point_3d, _3d=True) == (9 + 16 + 1) ** 0.5
    assert end_point_3d.get_length(begin_point, _3d=True) == (9 + 16 + 1) ** 0.5


def test_should_check_get_azimuth():
    # given
    begin_point = Point('P1245', 0, 0)
    end_point_0 = Point('P0', 1, 0)
    end_point_50 = Point('P50', 1, 1)
    end_point_100 = Point('P100', 0, 1)
    end_point_150 = Point('P150', -1, 1)
    end_point_200 = Point('P200', -1, 0)
    end_point_250 = Point('P250', -1, -1)
    end_point_300 = Point('P300', 0, -1)
    end_point_350 = Point('P350', 1, -1)

    # when
    # then
    assert begin_point.get_azimuth(end_point_0) == 0
    assert begin_point.get_azimuth(end_point_50) == 50
    assert begin_point.get_azimuth(end_point_100) == 100
    assert begin_point.get_azimuth(end_point_150) == 150
    assert begin_point.get_azimuth(end_point_200) == 200
    assert begin_point.get_azimuth(end_point_250) == 250
    assert begin_point.get_azimuth(end_point_300) == 300
    assert begin_point.get_azimuth(end_point_350) == 350


def test_should_check_get_angle():
    # given
    central_point = Point('P1245', 0, 0)
    end_point_0 = Point('P0', 1, 0)
    end_point_50 = Point('P50', 1, 1)
    end_point_100 = Point('P100', 0, 1)
    end_point_150 = Point('P150', -1, 1)
    end_point_200 = Point('P200', -1, 0)
    end_point_250 = Point('P250', -1, -1)
    end_point_300 = Point('P300', 0, -1)
    end_point_350 = Point('P350', 1, -1)

    # when
    # then
    assert central_point.get_angle(end_point_0, end_point_0) == 0
    assert central_point.get_angle(end_point_0, end_point_50) == 50
    assert central_point.get_angle(end_point_0, end_point_100) == 100
    assert central_point.get_angle(end_point_0, end_point_150) == 150
    assert central_point.get_angle(end_point_0, end_point_200) == 200
    assert central_point.get_angle(end_point_0, end_point_250) == 250
    assert central_point.get_angle(end_point_0, end_point_300) == 300
    assert central_point.get_angle(end_point_0, end_point_350) == 350

    assert central_point.get_angle(end_point_50, end_point_50) == 0
    assert central_point.get_angle(end_point_50, end_point_100) == 50
    assert central_point.get_angle(end_point_50, end_point_150) == 100
    assert central_point.get_angle(end_point_50, end_point_200) == 150
    assert central_point.get_angle(end_point_50, end_point_250) == 200
    assert central_point.get_angle(end_point_50, end_point_300) == 250
    assert central_point.get_angle(end_point_50, end_point_350) == 300
    assert central_point.get_angle(end_point_50, end_point_0) == 350

    assert central_point.get_angle(end_point_100, end_point_100) == 0
    assert central_point.get_angle(end_point_100, end_point_150) == 50
    assert central_point.get_angle(end_point_100, end_point_200) == 100
    assert central_point.get_angle(end_point_100, end_point_250) == 150
    assert central_point.get_angle(end_point_100, end_point_300) == 200
    assert central_point.get_angle(end_point_100, end_point_350) == 250
    assert central_point.get_angle(end_point_100, end_point_0) == 300
    assert central_point.get_angle(end_point_100, end_point_50) == 350

def test_should_check_get_dlugosc():
    # given
    begin_point = Point("P1", 14, 12)
    end_point = Point("P2", 20, 20)

    # when
    # then
    assert begin_point.get_length(end_point) == 10
    assert end_point.get_length(begin_point) == 10
    assert end_point.get_length(end_point) == 0

def test_should_check_get_azymut():
    # given
    begin_point = Point("P0", 14, 16)
    end_point = Point("P3", 10, 20)

    # when
    # then
    assert begin_point.get_azimuth(end_point) == 150

def test_should_check_get_kat():
    # given
    central_point = Point('P1', 14, 16)
    end_point = Point('P3', 10, 20)
    end_point_1 = Point('P4', 20, 10)

    # when
    # then
    assert central_point.get_angle(end_point, end_point_1) == 200







