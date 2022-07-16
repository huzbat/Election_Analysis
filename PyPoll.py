# Import the datetime class from the datetime module.
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)
# import csv
# dir(csv)

# add dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)









    # # Write some data to the file.
    # txt_file.write("Counties in the Election\n--------------")

    # # Write three counties to the file.
    # txt_file.write("\nArapahoe\nDenver\nJefferson")