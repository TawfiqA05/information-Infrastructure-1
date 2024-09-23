# Load the dataset from a CSV file
file_path = 'us_countries_covid19_daily.csv'  # Ensure this file is in the same directory or provide the correct path

# Initialize dictionaries to store total deaths and counts per month
monthly_deaths = {}
monthly_counts = {}

# Open the CSV file and process it
with open(file_path, mode='r') as file:
    # Read the header
    header = file.readline().strip().split(',')
    
    # Find the indices of the 'date' and 'deaths' columns
    date_idx = header.index('date')
    deaths_idx = header.index('deaths')
    
    for line in file:
        row = line.strip().split(',')
        date_str = row[date_idx]
        deaths_str = row[deaths_idx]
        
        # Skip rows with missing death data
        if deaths_str == '':
            continue
        
        deaths = float(deaths_str)

        # Extract year and month from the date string
        year_month = date_str[:7]

        # Accumulate deaths and counts for each month
        if year_month not in monthly_deaths:
            monthly_deaths[year_month] = 0
            monthly_counts[year_month] = 0
        
        monthly_deaths[year_month] += deaths
        monthly_counts[year_month] += 1

# Calculate the average deaths for each month
average_deaths = {}
for year_month in monthly_deaths:
    average_deaths[year_month] = monthly_deaths[year_month] / monthly_counts[year_month]

# Print the results
for year_month, avg_deaths in average_deaths.items():
    print(f"{year_month}: Average Deaths = {avg_deaths:.2f}")