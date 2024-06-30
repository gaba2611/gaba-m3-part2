def main():
    # Input current time in hours (24-hour format)
    current_time = int(input("Enter the current time (0-23): "))
    
    # Input hours to wait for the alarm
    wait_hours = int(input("Enter the number of hours to wait: "))
    
    # Calculate the alarm time
    alarm_time = (current_time + wait_hours) % 24
    
    # Print the result
    print(f"When the alarm goes off in {wait_hours} hours, it will be {alarm_time} (24-hour clock).")

if __name__ == "__main__":
    main()