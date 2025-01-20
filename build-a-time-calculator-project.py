def add_time(start, duration, starting_day=None):
    # Days of the week for reference
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Parse start time
    start_parts = start.split()
    start_time = start_parts[0]
    period = start_parts[1]  # AM or PM
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM':
        start_hour += 12
    
    # Calculate total minutes and hours
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    total_minutes %= 60
    
    # Calculate the final time in 24-hour format
    final_hour = total_hours % 24
    final_days = total_hours // 24
    
    # Convert back to 12-hour format
    final_period = 'AM' if final_hour < 12 else 'PM'
    final_hour = final_hour % 12
    if final_hour == 0:
        final_hour = 12
    
    # Determine the day of the week
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        final_day_index = (starting_day_index + final_days) % 7
        final_day = days_of_week[final_day_index]
    else:
        final_day = None
    
    # Format the result
    result = f"{final_hour}:{total_minutes:02d} {final_period}"
    
    if final_day:
        result += f", {final_day}"
    
    if final_days == 1:
        result += " (next day)"
    elif final_days > 1:
        result += f" ({final_days} days later)"
    
    return result


# Example Function Calls
print(add_time("3:00 PM", "3:10"))  # Returns: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday"))  # Returns: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"))  # Returns: 12:03 PM
print(add_time("10:10 PM", "3:30"))  # Returns: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday"))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))  # Returns: 7:42 AM (9 days later)
