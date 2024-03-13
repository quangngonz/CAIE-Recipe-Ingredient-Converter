from datetime import datetime

class Event:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time

class EventScheduler:
    def __init__(self):
        self.events = []

    def add_event(self, title, date, time):
        event = Event(title, date, time)
        self.events.append(event)
        print("Event added successfully.")

    def edit_event(self, index, title, date, time):
        if index >= 0 and index < len(self.events):
            self.events[index].title = title
            self.events[index].date = date
            self.events[index].time = time
            print("Event edited successfully.")
        else:
            print("Invalid event index.")

    def delete_event(self, index):
        if index >= 0 and index < len(self.events):
            del self.events[index]
            print("Event deleted successfully.")
        else:
            print("Invalid event index.")

    def view_events(self):
        if len(self.events) == 0:
            print("No events scheduled.")
        else:
            sorted_events = sorted(self.events, key=lambda x: datetime.strptime(x.date + ' ' + x.time, '%Y-%m-%d %H:%M'))
            print("Events sorted by date:")
            for index, event in enumerate(sorted_events):
                print(f"{index + 1}. {event.title} - {event.date} {event.time}")

# Main program
scheduler = EventScheduler()

# Adding events
scheduler.add_event("Meeting", "2024-03-15", "15:00")
scheduler.add_event("Birthday Party", "2024-04-20", "18:30")

# Viewing events
scheduler.view_events()

# Editing an event
scheduler.edit_event(1, "Birthday Party", "2024-04-20", "19:00")

# Viewing events after editing
scheduler.view_events()

# Deleting an event
scheduler.delete_event(0)

# Viewing events after deleting
scheduler.view_events()
