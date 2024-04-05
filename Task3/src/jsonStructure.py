import json 

class News:
    def __init__(self, date, title, link, underHeader):
        self.date = date
        self.title = title
        self.link = link
        self.underHeader = underHeader

class NewsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, News):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)