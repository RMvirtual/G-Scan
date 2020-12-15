class Date(object):
    """A class representing a year or month with short and
    full displays."""
    
    def __init__(self, full, short):
        self.full = full
        self.short = short

    def __str__(self):
        return str(self.full)