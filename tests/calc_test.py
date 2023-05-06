import pytest
from app.calculator import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 4, 3) == 7

    def test_subtracting_success(self):
        assert self.calc.subtraction(self, 11, 6) == 5

    def test_multiply_success(self):
        assert self.calc.multiply(self, 4, 5) == 20

    def test_division_success(self):
        assert self.calc.division(self, 64, 8) == 8
