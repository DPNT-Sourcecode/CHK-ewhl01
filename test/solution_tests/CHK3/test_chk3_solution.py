from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutRound3:
    def test_single_f(self):
        # one F = 10
        assert CheckoutSolution().checkout("F") == 10

    def test_three_fs_offer(self):
        # 3 Fs cost 20 (pay for 2 only)
        assert CheckoutSolution().checkout("FFF") == 20

    def test_mixed_fs(self):
        # 4 Fs -> 20 (for first 3) + 10 = 30
        assert CheckoutSolution().checkout("FFFF") == 30

    def test_combined_with_other_items(self):
        # 2E -> 80, free B removed, plus 3F -> 20
        # total = 100
        assert CheckoutSolution().checkout("EEBFFF") == 100
