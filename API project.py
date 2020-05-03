# 1. Collect data from the Franfurt Stock Exchange,
# for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).

# Importing the modules
import requests
import json

# Store the API key as a string - according to PEP8, constants are always named in all upper case
with open ('/.config/config.json', 'r') as f
    config = json.loads(f)
API_KEY= 'file' + config

# Calling Quandl API to pull 2017 data of the company: Carl Zeiss Meditec
url = 'https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?start_date=2017-01-01&end_date=2017-12-31?api_key='+API_KEY

# Assigning get url to variable r
r = requests.get(url)

# 2. Convert the returned JSON object into a Python dictionary.
json_data = r.json()
print('Question 2. Convert the returned JSON object into a Python dictionary.')
print('Answer:', type(json_data))

# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
opening_prices = []
for i in json_data['dataset']['data']:
    opening_prices.append(i[2])

print('Question 3. Calculate what the highest and lowest opening prices were for the stock in this period.')
print('Answer: High Opening =', max(opening_prices), ", Low Opening = ", min(opening_prices))

# 4. What was the largest change in any one day (based on High and Low price)?
change = []
for i in json_data['dataset']['data']:
    change.append(i[2] - i[3])
print('Question 4. What was the largest change in any one day (based on High and Low price)?')
print('Answer:', round(max(change), 2))

# 5. What was the largest change between any two days (based on Closing Price)?
count = len(json_data['dataset']['data'])
change_2_days = []
for i in range(count):
    if i == count - 1:
        break
    else:
        change_2_days.append(json_data['dataset']['data'][i][4] - json_data['dataset']['data'][i + 1][4])
print('Question 5. What was the largest change between any two days (based on Closing Price)?')
print('Answer:', round(max(change_2_days), 2))

# 6. What was the average daily trading volume during this year?
total_traded_volume = []
for i in json_data['dataset']['data']:
    total_traded_volume.append(i[6])
avg_traded_volume = sum(total_traded_volume) / len(total_traded_volume)
print('Question 6. What was the average daily trading volume during this year?')
print('Answer:', round(avg_traded_volume, 2))


# 7. What was the median trading volume during this year. (Note: you may need to implement your own
# function for calculating the median.)
def median_function(input_list):
    sorted_list = input_list.sort()
    n = len(input_list)
    if n % 2 == 0:
        median1 = input_list[n // 2]
        median2 = input_list[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = input_list[n // 2]
    return median


median = median_function(total_traded_volume)
print('Question 7. What was the median trading volume during this year?')
print('Answer:', median)
