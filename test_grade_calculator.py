import pytest
from grade_calculator import get_grade, calculate_average


# ─── Tests for get_grade ────────────────────────────────────────────────────

class TestGetGrade:
    def test_grade_A_plus(self):
        assert get_grade(90) == "A+"

    def test_grade_A_plus_boundary(self):
        assert get_grade(100) == "A+"

    def test_grade_A(self):
        assert get_grade(75) == "A"

    def test_grade_A_upper(self):
        assert get_grade(89) == "A"

    def test_grade_B(self):
        assert get_grade(60) == "B"

    def test_grade_B_upper(self):
        assert get_grade(74) == "B"

    def test_grade_C(self):
        assert get_grade(50) == "C"

    def test_grade_C_upper(self):
        assert get_grade(59) == "C"

    def test_grade_fail(self):
        assert get_grade(49) == "Fail"

    def test_grade_fail_zero(self):
        assert get_grade(0) == "Fail"


# ─── Tests for calculate_average ────────────────────────────────────────────

class TestCalculateAverage:
    def test_average_all_100(self):
        assert calculate_average([100, 100, 100, 100, 100]) == 100.0

    def test_average_all_zero(self):
        assert calculate_average([0, 0, 0, 0, 0]) == 0.0

    def test_average_mixed(self):
        assert calculate_average([80, 70, 90, 60, 100]) == 80.0

    def test_average_float_result(self):
        result = calculate_average([55, 65, 75, 85, 95])
        assert result == 75.0

    def test_invalid_less_than_5_subjects(self):
        with pytest.raises(ValueError):
            calculate_average([80, 90, 70])

    def test_invalid_more_than_5_subjects(self):
        with pytest.raises(ValueError):
            calculate_average([80, 90, 70, 60, 50, 40])

    def test_invalid_mark_above_100(self):
        with pytest.raises(ValueError):
            calculate_average([101, 90, 70, 60, 50])

    def test_invalid_negative_mark(self):
        with pytest.raises(ValueError):
            calculate_average([-1, 90, 70, 60, 50])


# ─── Integration-style Tests ─────────────────────────────────────────────────

class TestIntegration:
    def test_full_flow_A_plus(self):
        marks = [95, 92, 98, 90, 96]
        avg = calculate_average(marks)
        assert get_grade(avg) == "A+"

    def test_full_flow_A(self):
        marks = [80, 75, 78, 76, 82]
        avg = calculate_average(marks)
        assert get_grade(avg) == "A"

    def test_full_flow_B(self):
        marks = [65, 60, 62, 68, 70]
        avg = calculate_average(marks)
        assert get_grade(avg) == "B"

    def test_full_flow_C(self):
        marks = [50, 55, 52, 53, 51]
        avg = calculate_average(marks)
        assert get_grade(avg) == "C"

    def test_full_flow_fail(self):
        marks = [30, 40, 35, 45, 20]
        avg = calculate_average(marks)
        assert get_grade(avg) == "Fail"
