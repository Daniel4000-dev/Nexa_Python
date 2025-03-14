# def count_errors(filename):
#     with open(filename, "r") as file:
#         content = file.read()
#         error_count = content.count("ERROR")
#         print(f"Found {error_count} occurrences of 'ERROR' in {filename}")
    
# if __name__ == "__main__":
#     # Specify your sample log file name
#     count_errors("sample.log")

def count_errors_filtered(filename, date_filter=None, severity_filter="ERROR"):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            if severity_filter in line:
                if date_filter:
                    # Check if the date string is in the log line
                    if date_filter in line:
                        count += 1
                else:
                    count += 1
    print(f"Found {count} occurrences of '{severity_filter}' in {filename}" + (f" on {date_filter}" if date_filter else ""))

if __name__ == "__main__":
    import sys
    # Accept filename and optional date filter from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "sample.log"
    date_filter = sys.argv[2] if len(sys.argv) > 2 else None
    count_errors_filtered(filename, date_filter)
