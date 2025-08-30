
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
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 80,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 30,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 90,
            "Y": 10,
            "Z": 50,

        }

        # deals on some items
        # for multi-price offers we put them in a list, biggest deal first

        offers = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "H": [(10, 80), (5, 45)],
            "K": [(2, 150)],
            "P": [(5, 200)],
            "Q": [(3, 80)],
            "V": [(3, 130), (2, 90)],
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


        # 3N -> 1M free
        if "N" in counts and counts["N"] >= 3:
            free_ms = counts["N"] // 3
            if "M" in counts:
                counts["M"] = max(0, counts["M"] - free_ms)

        # F deal: buy 2F, get 1F free (so pay for only 2 of every 3), only works if at least 3 Fs, but if less than 3, still pay for 2
        if "F" in counts:
            groups_of_three = counts["F"] // 3
            remainder = counts["F"] % 3
            total += groups_of_three * 2 * prices["F"]
            counts["F"] = remainder

        # 3R -> 1Q free
        if "R" in counts and counts["R"] >= 3:
            free_qs = counts["R"] // 3
            if "Q" in counts:
                counts["Q"] = max(0, counts["Q"] - free_qs)

        # U: 3U get 1U free => for every 4U pay for 3
        if "U" in counts:
            groups = counts["U"] // 4
            remainder = counts["U"] % 4
            total += groups * 3 * prices["U"]
            counts["U"] = remainder

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

