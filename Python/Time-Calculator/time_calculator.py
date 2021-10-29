def add_time(start, duration, day=None):
    start_time = str(start)[:-2].strip()
    meridian = str(start)[-2:].strip().upper()

    start_time_hours = int(start_time.split(':')[0])
    start_time_mins = int(start_time.split(':')[1])

    start_time_hours = start_time_hours + 12 if meridian == "PM" else start_time_hours + 0

    number_of_hours = int(str(duration).split(':')[0])
    number_of_mins = int(str(duration).split(':')[1])

    total_hours = start_time_hours + number_of_hours
    total_mins = start_time_mins + number_of_mins

    days_later = 0
    days_later_output = ""
    if days_later == 1:
        days_later_output = "(next day)"
    elif days_later > 1:
        days_later_output = f"({days_later} days later)"

    if total_hours > 24:
        total_hours %= 24
        days_later = total_hours // 24

    if total_hours == 0:
        total_hours = 12
        meridian_output = "AM"
    elif total_hours >= 12:
        meridian_output = "PM"
        total_hours -= 12 if total_hours > 12 else 0
    else:
        meridian_output = "AM"

    if total_mins >= 60:
        total_mins -= 60
        total_hours += 1

    if total_mins < 10:
        total_mins = "0" + str(total_mins)
    
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = str(day).capitalize()
    final_new_day = ""
    if day in days_of_the_week:
        new_day = days_of_the_week.index(day)
        new_day += total_hours // 24
        final_new_day = f", {days_of_the_week[new_day % 7]}"

    new_time = f"{total_hours}:{total_mins} {meridian_output}{final_new_day} {days_later_output}"
    return new_time
