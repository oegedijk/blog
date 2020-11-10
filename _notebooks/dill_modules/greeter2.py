def greeting1():
    return "Booyaa!"


def greeting2():
    return "Howdy!"


class Greeter:
    def __init__(self, greetings):
        self.greetings = greetings
        
    def greet(self):
        for greet in self.greetings:
            print(greet())
     
    @classmethod
    def dillable(cls, greetings):
        import __main__
        for greeting in greetings:
            cls._mainify(greeting)
        cls._mainify(cls)
        cls = getattr(__main__, cls.__name__)
        greetings = [getattr(__main__, greeting.__name__) for greeting in greetings]
        return cls(greetings)
    
    @staticmethod
    def _mainify(obj):
        """If obj is not defined in __main__ then redefine it in 
        main so that dill will serialize the definition along with the object"""
        if obj.__module__ != "__main__":
            import __main__
            import inspect
            s = inspect.getsource(obj)
            co = compile(s, '<string>', 'exec')
            exec(co, __main__.__dict__)