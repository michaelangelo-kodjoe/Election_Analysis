from asyncore import write
import csv
import os
import csv
# #Assign Variable for the file to load the path
file_to_load = os.path.join('resources','election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)
    #print each row in the csv file
    # for row in file_reader:
    #     print(row)
