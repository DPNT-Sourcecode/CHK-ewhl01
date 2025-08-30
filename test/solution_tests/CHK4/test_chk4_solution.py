from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutRound4:
    def test_basic_new_items(self):
        # single new items
        assert CheckoutSolution().checkout("G") == 20
        assert CheckoutSolution().checkout("H") == 10
        assert CheckoutSolution().checkout("I") == 35
        assert CheckoutSolution().checkout("J") == 60
        assert CheckoutSolution().checkout("K") == 80
        assert CheckoutSolution().checkout("L") == 90
        assert CheckoutSolution().checkout("M") == 15
        assert CheckoutSolution().checkout("N") == 40
        assert CheckoutSolution().checkout("O") == 10
        assert CheckoutSolution().checkout("P") == 50
        assert CheckoutSolution().checkout("Q") == 30
        assert CheckoutSolution().checkout("R") == 50
        assert CheckoutSolution().checkout("S") == 30
        assert CheckoutSolution().checkout("T") == 20
        assert CheckoutSolution().checkout("U") == 40
        assert CheckoutSolution().checkout("V") == 50
        assert CheckoutSolution().checkout("W") == 20
        assert CheckoutSolution().checkout("X") == 90
        assert CheckoutSolution().checkout("Y") == 10
        assert CheckoutSolution().checkout("Z") == 50

    def test_offer_on_h(self):
        # 5H = 45 (offer)
        assert CheckoutSolution().checkout("H"*5) == 45

        # 10H = 80 (offer)
        assert CheckoutSolution().checkout("H"*10) == 80


    def test_offer_on_k(self):
        # 2K = 150
        assert CheckoutSolution().checkout("KK") == 150

    def test_offer_on_v(self):
        # 3V = 130
        assert CheckoutSolution().checkout("VVV") == 130

    def test_cross_offer_n_and_m(self):
        # 3N gives 1M free
        assert CheckoutSolution().checkout("NNNM") == 120

    def test_self_offer_u(self):
        # 4U -> pay for 3 = 120
        assert CheckoutSolution().checkout("UUUU") == 120
