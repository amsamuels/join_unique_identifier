import glob
import time

start_time = time.time()
data = {}
# delimiter used in the csv file
delimiter = ","
# get all the files in the directory
all_files = glob.glob("csv_live/*.csv")
# sort the files in the directory

for new_all_files in all_files:
    with open(new_all_files, "r", encoding="utf-8") as file:
        lines = file.readlines()
        line_count = len(lines)
        line_index0 = 0
        line_end = line_count - 1
        while line_index0 < line_end:
            current_line = lines[line_index0].strip().split(delimiter)
            col_id = current_line[0]
            if col_id in data:
                existing_values = data[col_id]
                merged_values = existing_values + current_line[1:]
                data[col_id] = merged_values
            else:
                data[col_id] = current_line[1:]

            line_index0 += 1

# Name of the output file
output_file = "combined_large_file.csv"
# open the output file in write mode and store in a variable
with open(output_file, "w", encoding="utf-8") as file:
    # Write the header line

    # iterates over the items in the dictionary
    for unique_id, record in data.items():
        # write the key and values in the dictionary to the output file
        line = [unique_id] + record
        # write the line to the output file
        file.write(delimiter.join(line) + "\n")

end_time = time.time()
elapsed_time = end_time - start_time

# Print the elapsed time
print("Elapsed time: ", elapsed_time, "seconds")
