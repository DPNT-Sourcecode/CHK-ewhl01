from solutions.HLO.hello_solution import HelloSolution

class TestHello:
    
    def test_hello_craftsman(self):
        assert HelloSolution().hello("Craftsman") == "Hello, World!"

    def test_hello_mr_x(self):
        assert HelloSolution().hello("Mr. X") == "Hello, World!"

    def test_empty_name_raises(self):
        try:
            HelloSolution().hello("")
            assert False, "Expected ValueError for empty name"
        except ValueError:
            assert True

    def test_whitespace_name_raises(self):
        try:
            HelloSolution().hello("   ")
            assert False, "Expected ValueError for whitespace-only name"
        except ValueError:
            assert True

    def test_non_string_input_raises(self):
        try:
            HelloSolution().hello(123)
            assert False, "Expected ValueError for non-string input"
        except ValueError:
            assert True

