from main import add, subtract, multiply


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(1, 2) == 3

    def test_add_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_add_mixed_signs(self):
        assert add(-1, 2) == 1
        assert add(1, -2) == -1

    def test_add_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5


class TestSubtract:
    def test_subtract_positive_result(self):
        assert subtract(5, 2) == 3

    def test_subtract_negative_result(self):
        assert subtract(1, 2) == -1

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6