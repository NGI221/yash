from collections import deque

# Initialize queue
event_queue = deque()

def add_event(event):
    event_queue.append(event)
    print(f"Event '{event}' added.")

def process_event():
    if event_queue:
        event = event_queue.popleft()
        print(f"Processed event: {event}")
    else:
        print("No events to process.")

def display_events():
    if event_queue:
        print("Pending events:", list(event_queue))
    else:
        print("No pending events.")

def cancel_event(event):
    if event in event_queue:
        event_queue.remove(event)
        print(f"Event '{event}' canceled.")
    else:
        print("Event not found or already processed.")

# Example usage
while True:
    print("\n1. Add Event\n2. Process Event\n3. Display Events\n4. Cancel Event\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_event(input("Enter event name: "))
    elif choice == '2':
        process_event()
    elif choice == '3':
        display_events()
    elif choice == '4':
        cancel_event(input("Enter event name to cancel: "))
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")