
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        """
        Work out the checkout price for a string of SKUs.
        Returns -1 if the input is not valid.
        """
        # quick check input is a string
        if not isinstance(skus, str):
            return -1

        # normal prices
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
        }

        # deals on some items
        offers = {
            "A": (3, 130),  # 3 As for 130
            "B": (2, 45),   # 2 Bs for 45
        }

        # count up each item
        counts = {}
        for ch in skus:
            if ch not in prices:
                return -1
            counts[ch] = counts.get(ch, 0) + 1

        # work out total with offers
        total = 0
        for item, count in counts.items():
            if item in offers:
                offer_qty, offer_price = offers[item]
                total += (count // offer_qty) * offer_price
                total += (count % offer_qty) * prices[item]
            else:
                total += count * prices[item]

        return total

