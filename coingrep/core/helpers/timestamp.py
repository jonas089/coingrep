from datetime import datetime

def unix_to_human(unix):
    return datetime.utcfromtimestamp(unix).strftime('%d-%m-%Y')

def human_to_unix(human):
    return human.utcfromtimestamp(unix_timestamp)