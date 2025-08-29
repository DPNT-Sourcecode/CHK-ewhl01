
class SumSolution:
    
    def compute(self, x, y):
        """
        Adds two integers between 0 and 100 (inclusive)

        param x: first integer (0 <= x <= 100)
        param y: second integer (0 <= y <= 100)
        return: sum of x and y
        """
        if not (0 <= x <= 100):
            raise ValueError("Parameter 'x' must be between 0 and 100")
        if not (0 <= y <= 100):
            raise ValueError("Parameter 'y' must be between 0 and 100")
        return x + y
