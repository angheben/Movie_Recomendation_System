import pandas as pd

spreadsheet = pd.read_excel('teste.xlsx', sheet_name='teste')
print(pd.DataFrame(spreadsheet))
"""
with open(file='movie_list.csv', encoding='UTF-8', mode='r') as file:
"""
