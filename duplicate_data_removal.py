from more_itertools import unique_everseen

with open('DETAILS.csv', 'r') as f, open('New_Details.csv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))
