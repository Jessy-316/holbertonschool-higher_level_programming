import os

def generate_invitations(template: str, attendees: list):
    """Create invitations based on the template and fill in the information with the list of attendees."""

    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Ensure all keys have default values if missing
        filled_attendee = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A")
        }

        # Generate the filename
        filename = f"output_{i}.txt"
        
        # Write the processed template to the file
        try:
            with open(filename, "w") as file:
                file.write(template.format(**filled_attendee))
            print(f'Generated {filename}')
        except KeyError as e:
            print(f"Error: Missing key {str(e)} in the template for attendee {i}")
