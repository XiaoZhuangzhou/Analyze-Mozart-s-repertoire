"""Class blah"""
class Item(object):
    """Class to represent an item"""

    def __init__(self, name, date, genre, key, orchestration, description):
        """Init"""
        self.name = name
        self.date = date
        self.genre = genre
        self.key = key
        self.orchestration = orchestration
        self.description = description

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_genre(self):
        return self.genre

    def get_key(self):
        return self.key

    def get_orchestration(self):
        return self.orchestration

    def get_description(self):
        return self.description

    def __str__(self):
        return '{0}, {1}, {2}, {3}, {4}, {5}'.format(self.name, self.date, self.genre, self.key, self.orchestration, self.description)