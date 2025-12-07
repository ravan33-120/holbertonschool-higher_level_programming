# task_00_intro.py

import os

def generate_invitations(template, attendees):
    # -------------------------------------------------
    # 1. Input type checks
    # -------------------------------------------------
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return
    
    # -------------------------------------------------
    # 2. Empty template check
    # -------------------------------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # -------------------------------------------------
    # 3. Empty attendees list
    # -------------------------------------------------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    # -------------------------------------------------
    # 4. Process each attendee
    # -------------------------------------------------
    for index, person in enumerate(attendees, start=1):

        # Replace missing keys → N/A
        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        # Replace placeholders in template
        output_text = template.replace("{name}", name)
        output_text = output_text.replace("{event_title}", event_title)
        output_text = output_text.replace("{event_date}", event_date)
        output_text = output_text.replace("{event_location}", event_location)

        # Output file name
        file_name = f"output_{index}.txt"

        try:
            with open(file_name, "w") as f:
                f.write(output_text)
        except Exception as e:
            print(f"Error writing file {file_name}: {e}")
            continue

