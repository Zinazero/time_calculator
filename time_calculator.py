def add_time(start, duration, day=False):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    if day:
        day = day.lower()
        if day in weekdays:
            day_index = weekdays.index(day)


    start_split = start.split(" ")
    qualifier = start_split[1]
    if qualifier not in ["AM", "PM"]:
        return "Error: AM or PM is required."
    
    start_time_split = start_split[0].split(":")
    start_hour = int(start_time_split[0])
    start_minute = int(start_time_split[1])
    duration_split = duration.split(":")
    duration_hour = int(duration_split[0])
    duration_minute = int(duration_split[1])

    day_tracker = 0
    hour_tracker = start_hour
    for i in range(duration_hour):
        hour_tracker += 1
        
        if hour_tracker == 12:
            if qualifier == "AM":
                qualifier = "PM"
            elif qualifier == "PM":
                qualifier = "AM"
                day_tracker += 1
        if hour_tracker == 13:
            hour_tracker = 1

    minute_tracker = start_minute
    for i in range(duration_minute):
        minute_tracker += 1
        
        if minute_tracker == 60:
            minute_tracker = 0
            hour_tracker += 1
            if hour_tracker == 12:
                if qualifier == "AM":
                    qualifier = "PM"
                elif qualifier == "PM":
                    qualifier = "AM"
                    day_tracker += 1
            if hour_tracker == 13:
                hour_tracker = 1
    if day_tracker == 0:
        days_later = ""
    elif day_tracker == 1:
        days_later = " (next day)"
    else:
        days_later = f" ({day_tracker} days later)"

    if day:
        for i in range(day_tracker):
            day_index += 1

            if day_index > 6:
                day_index = 0

        day_of_week = f", {weekdays[day_index].capitalize()}"
    else:
        day_of_week = ""


    new_time = f"{hour_tracker}:{str(minute_tracker).zfill(2)} {qualifier}{day_of_week}{days_later}"

    return new_time

print(add_time("11:59 PM", "24:05"))