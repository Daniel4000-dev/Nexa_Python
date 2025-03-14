import psutil;
import time;

log_file = "system_usage.log"

with open(log_file, "a") as logfile:
    try:
        while True:
            # Get CPU usage
            cpu_usage = psutil.cpu_times_percent(interval=1) # interval=1 makes the function wait 1 second to get a proper measurement
            # Get memory usage percentage
            memory_usage = psutil.virtual_memory().percent
            
            # Format the output
            output = f"CPU Usage: {cpu_usage}% Memory Usage: {memory_usage}%"
            print(output)
            logfile.write(output + "\n")
            
            # Wait for 4 seconds so that the overall loop runs roughly every 5 seconds
            time.sleep(4)
    except KeyboardInterrupt:
        print("Monitoring stopped.")