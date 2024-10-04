# Title: Time Addition Function
# This script defines a function to add a duration to a starting time, 
# returning the new time in a standard format. It can also take an optional
# starting day of the week and correctly handle transitions between AM and PM,
# as well as wrap around the week.

def add_time(start, duration, starting_day=''):
    # Split start time into hours, minutes, and period (AM/PM)
    time, period = start.split()  # Split the time and period (AM/PM)
    start_hour, start_minute = map(int, time.split(':'))  # Convert to integers

    # Split duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))  # Convert to integers

    # Convert start time to 24-hour format for easier calculations
    if period == 'PM' and start_hour != 12:  # Convert PM hours
        start_hour += 12  # Add 12 to convert to 24-hour format
    elif period == 'AM' and start_hour == 12:  # Convert 12 AM to 0 hours
        start_hour = 0  # Midnight in 24-hour format

    # Calculate total minutes from start time and duration
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate new hour and minute from total minutes
    new_hour = (total_minutes // 60) % 24  # Get new hour (wrap around for 24 hours)
    new_minute = total_minutes % 60  # Get remaining minutes

    # Determine AM/PM for the new time
    if new_hour < 12:  # Before noon
        new_period = 'AM'
        display_hour = 12 if new_hour == 0 else new_hour  # Display hour (12 for midnight)
    else:  # After noon
        new_period = 'PM'
        display_hour = new_hour - 12 if new_hour > 12 else 12  # Convert back to 12-hour format

    # Calculate the number of days passed during the addition
    days_passed = total_minutes // 1440  # 1440 minutes in a day (24 * 60)

    # Handle the starting day input
    new_day = ''  # Initialize new day as empty string
    if starting_day:  # If a starting day is provided
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # List of days
        starting_day_index = days_of_week.index(starting_day.title())  # Get index of starting day
        new_day = days_of_week[(starting_day_index + days_passed) % len(days_of_week)]  # Calculate new day

    # Construct output string based on how many days passed
    if days_passed > 0:  # If at least one day passed
        if days_passed == 1:  # If only one day passed
            days_passed_str = ' (next day)'  # Special case for next day
        else:
            days_passed_str = f' ({days_passed} days later)'  # More than one day
    else:
        days_passed_str = ''  # No days passed

    # Construct final new time string with proper formatting
    if new_day:  # If there's a new day
        new_time = f"{display_hour}:{str(new_minute).zfill(2)} {new_period}, {new_day}{days_passed_str}"
    else:  # No new day
        new_time = f"{display_hour}:{str(new_minute).zfill(2)} {new_period}{days_passed_str}"

    return new_time  # Return the final formatted time string

# Example usage of the function
print(add_time('11:43 AM', '00:20'))              # Expected output: '12:03 PM'
print(add_time('10:10 PM', '3:30', 'Monday'))     # Expected output: '1:40 AM, Tuesday'
print(add_time('3:30 PM', '2:12', 'Monday'))      # Expected output: '5:42 PM, Monday'