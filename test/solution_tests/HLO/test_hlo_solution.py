from solutions.HLO.hello_solution import HelloSolution

class TestHello:
    def test_basic_hello(self):
        assert HelloSolution().hello("World") == "Hello World"

    def test_hello_with_name(self):
        assert HelloSolution().hello("Alice") == "Hello Alice"

    def test_hello_with_spaces(self):
        assert HelloSolution().hello(" Bob ") == "Hello  Bob "