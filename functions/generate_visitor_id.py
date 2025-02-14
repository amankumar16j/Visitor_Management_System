from datetime import datetime

def generate_visitor_id(user_name):
    user_name = user_name[:2].upper()  # First two letters of the username (uppercase)
    current_time = datetime.now()
    
    date_part=f"{current_time.day:02d}"
    minute_part = f"{current_time.minute:02d}"  # First two digits of the current date
    second_part = f"{current_time.second:02d}"  # First two digits of the current minute
    
    user_id = user_name +date_part + minute_part + second_part
    return user_id
