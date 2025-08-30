from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutRound5:
    def test_updated_prices(self):
        # updated items
        assert CheckoutSolution().checkout("K") == 70
        assert CheckoutSolution().checkout("X") == 17
        assert CheckoutSolution().checkout("Z") == 21

    def test_updated_offer_k(self):
        # new deal: 2K = 120
        assert CheckoutSolution().checkout("KK") == 120

    def test_group_offer_basic(self):
        # 3 group items -> 45
        assert CheckoutSolution().checkout("STZ") == 45

    def test_group_offer_picks_highest(self):
        # take priciest 3 first: Z(21)+S(20)+Y(20)=61, group=45 + X(17) left
        assert CheckoutSolution().checkout("XYZS") == 62

    def test_mixed_basket(self):
        # 3A=130, plus STZ=45, total=175
        assert CheckoutSolution().checkout("AAASTZ") == 175

    def test_invalid_input(self):
        assert CheckoutSolution().checkout("1A") == -1
        assert CheckoutSolution().checkout(123) == -1
