import gspread
import time
gc = gspread.service_account('secret.json')
spreadsheet = gc.open('PythonApp')
# Get Sheet based on index
# worksheet1 = spreadsheet.get_worksheet(0)
# Get sheet based on name
worksheet1 = spreadsheet.worksheet('List 1')
# Data from Sheet 1
data = worksheet1.get_all_records()
columns = worksheet1.col_values(4)
row_five = worksheet1.get_values('A5:F5')
# Getting just  a cell
oneitem = worksheet1.acell('A5').value
# Search for value
# search_value = worksheet1.find('10')
# search_all_values = worksheet1.findall('1')
# for value in search_all_values:
#     print(value.row, value.col)
# print(search_all_values)


# updateing cell
worksheet1.update('D2', 55)


# Tracking changes
worksheet2 = spreadsheet.worksheet('Two')
value1 = worksheet1.acell('F25').value
print('Change value now')
time.sleep(5)
value2 = worksheet2.acell('F25').value
if value1 != value2:
    worksheet2.update('A1', 'Changed')
