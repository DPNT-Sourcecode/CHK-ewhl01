from solutions.HLO.hello_solution import HelloSolution

class TestHello:
    def test_basic_hello(self):
        assert HelloSolution().hello("World") == "Hello World"

    def test_hello_with_name(self):
        assert HelloSolution().hello("Alice") == "Hello Alice"

    def test_hello_with_spaces(self):
        assert HelloSolution().hello(" Bob ") == "Hello  Bob "
    
    def test_empty_name(self):
        try:
            HelloSolution().hello("")
            assert False, "Expected ValueError for empty name"
        except ValueError:
            assert True

    def test_non_string_input(self):
        try:
            HelloSolution().hello(123)
            assert False, "Expected ValueError for non-string input"
        except ValueError:
            assert True
