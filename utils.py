import json
from datetime import datetime, date, time

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%m/%d/%Y %H:%M:%S")
        elif isinstance(o, date):
            return o.strftime("%m/%d/%Y")
        return json.JSONEncoder.default(self, o)




