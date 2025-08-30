from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutRound2:
    def test_new_item_e_basic(self):
        # single E, no offer
        assert CheckoutSolution().checkout("E") == 40

    def test_free_b_with_two_es(self):
        # 2E gives one B free, so only pay for Es
        assert CheckoutSolution().checkout("EEB") == 80

    def test_multi_offers_on_a(self):
        # 5A should cost 200 (better deal than 3A+2A=230)
        assert CheckoutSolution().checkout("AAAAA") == 200

    def test_mix_of_offers(self):
        # 2E -> pay 80, 1B free, plus C=20
        assert CheckoutSolution().checkout("EECB") == 100
