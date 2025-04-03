class Singleton:
    _instance = None

    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance
    
obj1 = Singleton.get_instance()
obj2 = Singleton.get_instance()

print(obj1 is obj2)