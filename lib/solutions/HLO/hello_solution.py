
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        """
        Returns a greeting message for the given friend_name.

        :param friend_name: Name to greet
        :return: Greeting string
        """
        if not isinstance(friend_name, str):
            raise ValueError("Parameter 'friend_name' must be a string")
        if not friend_name.strip():
            raise ValueError("Parameter 'friend_name' cannot be empty")
        
        return f"Hello, {friend_name}!"