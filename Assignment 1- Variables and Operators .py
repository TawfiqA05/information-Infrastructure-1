# Initialize variables to store the earliest and latest dates
earliest_date = None
latest_date = None

# Open the CSV file and read its contents
with open('us_counties_covid19_daily.csv', 'r') as file:
    # Skip the header line
    next(file)
    
    for line in file:
        # Extract the date from the current line
        current_date_str = line.split(',')[0]
        
        # Convert the date string to a tuple of integers (year, month, day)
        year, month, day = map(int, current_date_str.split('-'))
        current_date = (year, month, day)
        
        # Update the earliest and latest dates
        if earliest_date is None or current_date < earliest_date:
            earliest_date = current_date
        if latest_date is None or current_date > latest_date:
            latest_date = current_date

# Format the dates as strings for output
earliest_date_str = f"{earliest_date[0]:04d}-{earliest_date[1]:02d}-{earliest_date[2]:02d}"
latest_date_str = f"{latest_date[0]:04d}-{latest_date[1]:02d}-{latest_date[2]:02d}"

# Print the date range
print(f"Date range: {earliest_date_str} to {latest_date_str}")