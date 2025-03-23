class Query:
    def __init__(self, type, triggers, fears, message):
        self.type = type
        self.triggers = triggers
        self.fears = fears
        self.message = message
    
    def create_query(self):
        return f"I have the problem of {self.type}. My trigger points for this disorder are {self.triggers}. My fears include {self.fears}. {self.message}"
    

