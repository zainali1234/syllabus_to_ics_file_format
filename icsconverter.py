from ics import Calendar, Event
from datetime import datetime, timedelta

def clean_text(text):
    # Try to encode and decode using utf-8 to remove unknown characters
    try:
        cleaned_text = text.encode('utf-8').decode('utf-8')
    except UnicodeDecodeError:
        cleaned_text = text.encode('utf-8', 'replace').decode('utf-8', 'replace')

    return cleaned_text

def ics_converter(text):
    lines = clean_text(text).split('\n')
    cal = Calendar()

    lines = [item for item in lines if item != '']

    print(lines)

    current_year = datetime.now().year  # Get the current year
    course_name = lines[0].strip()
    # Assume the course name is on the first line

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue

        # Check if the line contains a dash ("-")
        if '-' not in line:
            print(f"Skipping line without expected format: {line}")
            continue

        date_str, event_description = line.split('-', 1)
        date_str = date_str.strip()
        event_description = event_description.strip()

        # Append the current year to the date string
        date_str_with_year = f"{date_str}/{current_year}"
        date_object = datetime.strptime(date_str_with_year, '%m/%d/%Y')

        event = Event()
        event.name = f"{course_name}: {event_description}"
        event.begin = date_object
        event.end = date_object + timedelta(hours=1)  # Assuming events last for 1 hour

        cal.events.add(event)

    return str(cal)