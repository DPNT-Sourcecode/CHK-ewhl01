
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        """
        Return a greeting message to the world!
        """        

        if not isinstance(friend_name, str):
            raise ValueError("Parameter 'friend_name' must be a string")
        if not friend_name.strip():
            raise ValueError("Parameter 'friend_name' cannot be empty")
        
        
        return "Hello, World!"