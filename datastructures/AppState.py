class AppState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}  # Your application state data
            cls._instance.observers = []
        return cls._instance
    
    def set_data(self, key, value):
        self.data[key] = value
        self.notify_observers()

    def get_data(self, key):
        return self.data.get(key)

    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()