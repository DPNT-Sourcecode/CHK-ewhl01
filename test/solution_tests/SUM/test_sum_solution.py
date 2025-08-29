from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_sum_with_zero(self):
        assert SumSolution().compute(0, 10) == 10

