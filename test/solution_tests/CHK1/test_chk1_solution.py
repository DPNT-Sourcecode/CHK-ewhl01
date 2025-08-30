from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_single_items(self):
        # price of each item on its own
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15

    def test_multiple_items_no_offer(self):
        # mix of items, no special deal
        assert CheckoutSolution().checkout("ABCD") == 115  # 50+30+20+15

    def test_special_offer_applied(self):
        # deal kicks in
        assert CheckoutSolution().checkout("AAA") == 130  # 3 As for 130
        assert CheckoutSolution().checkout("BB") == 45    # 2 Bs for 45

    def test_illegal_input(self):
        # bad input should give -1
        assert CheckoutSolution().checkout("AX") == -1
        assert CheckoutSolution().checkout(123) == -1
