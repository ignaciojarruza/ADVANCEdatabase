import pandas as pd

#Extracting 2022-2023 Events Spreadsheet Data
event_spreadsheet = 'excel-sheets/event-lists/2022-2023 Events.xlsx'
df = pd.read_excel(event_spreadsheet)

#Parsing data
#Removing the % Attendance
df = df.drop('% Attendance', axis=1)

#Changing Committee-led to NU Internal and formatting null values
for index, value in df['Speaker/Facilitator'].items():
    if value == 'Committee-led (NU Internal)':
        df.loc[index, 'Speaker/Facilitator'] = 'NU Internal'
    if pd.isna(value):
        print(index)
        df.loc[index, 'Speaker/Facilitator'] = 'No speaker/focus group'

#Normalize table into appropriate database dataframes

print(df)
