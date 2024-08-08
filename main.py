import os
from icalendar import Calendar

def merge_ics_files(directory):
    merged_calendar = Calendar()
    for filename in os.listdir(directory):
        if filename.endswith(".ics"):
            with open(os.path.join(directory, filename), 'rb') as f:
                calendar = Calendar.from_ical(f.read())
                for component in calendar.walk():
                    if component.name == "VEVENT":
                        merged_calendar.add_component(component)
    with open(os.path.join(directory, 'combined.ics'), 'wb') as f:
        f.write(merged_calendar.to_ical())

if __name__ == "__main__":
    merge_ics_files(r"D:\Temp")  # Using raw string
    # or
    # merge_ics_files("D:\\Temp")  # Using double backslashes
