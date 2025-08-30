
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
            "E": 40,
        }

        # deals on some items
        # for multi-price offers we put them in a list, biggest deal first

        offers = {
            "A": [(5, 200), (3, 130)], # 5 for 200, 3 for 130
            "B": [(2, 45)],   # 2 Bs for 45
        }

        # count up each item
        counts = {}
        for ch in skus:
            if ch not in prices:
                return -1
            counts[ch] = counts.get(ch, 0) + 1

        # work out total with offers
        total = 0

        # handle B freebies from Es
        if "E" in counts and counts["E"] >= 2:
            free_bs = counts["E"] // 2
            if "B" in counts:
                counts["B"] = max(0, counts["B"] - free_bs)

        # apply offers
        for item, count in counts.items():
            if item in offers:
                for qty, offer_price in offers[item]:
                    num_offers = count // qty
                    total += num_offers * offer_price
                    count %= qty
                total += count * prices[item]
            else:
                total += count * prices[item]

        return total
