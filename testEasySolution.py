from warnings import catch_warnings
import pandas as pd
from configparser import ConfigParser

config = ConfigParser()

# Read the configuration file
config.read('config.ini')

# Get the path from the configuration file
input_file = config.get('FILES', 'input_file')

output_file = config.get('FILES', 'output_file')


#Read the specific excel file from the path
data_file = pd.read_excel(input_file)


# A function that calculates the percentage from the number of passes
def get_pass_percentage(column1, column2):
    percentage = (column1 / column2) * 100
    percentage_to_2dp = round(percentage, 2)
    return percentage_to_2dp


# a function to get the ratings for each score
def get_rating(score):
   match score:
       case s if s >= 90:
           return  1
       case s if 80 <= s < 90:
           return 2
       case s if 60 <= s < 80:
           return 3
       case _ :
           return 4




# Add the new column for percentage
data_file['Pass Percentage'] = data_file.apply(lambda x: get_pass_percentage(x['Passed Tests'], x['Total Tests']),
                                               axis=1)
# A new column for the rating
data_file['Rating'] = data_file.apply(lambda row: get_rating(row['Pass Percentage']), axis=1)


# A try and except block to confirm file storage
try:
    #Export the file with the index not included
    data_file.to_excel(output_file, index=False)
    print("File saved successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# pd.set_option('display.max_columns', None)
print(data_file.head(10))
