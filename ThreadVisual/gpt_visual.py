import matplotlib.pyplot as plt

# Example conversation threads
conversation_threads = [
    {'sender': 'You', 'message': 'Hello', 'timestamp': '2023-04-09 10:00:00'},
    {'sender': 'ChatGPT', 'message': 'Hi there!', 'timestamp': '2023-04-09 10:01:00'},
    {'sender': 'You', 'message': 'How are you?', 'timestamp': '2023-04-09 10:02:00'},
    {'sender': 'ChatGPT', 'message': 'I am doing well, thank you!', 'timestamp': '2023-04-09 10:03:00'},
    # Add more conversation threads as needed
]

# Extract sender, message, and timestamp from conversation threads
senders = [thread['sender'] for thread in conversation_threads]
messages = [thread['message'] for thread in conversation_threads]
timestamps = [thread['timestamp'] for thread in conversation_threads]

# Convert timestamps to datetime objects
# Note: This assumes that the timestamps are in a consistent format, e.g., 'YYYY-MM-DD HH:MM:SS'
timestamps = [datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') for timestamp in timestamps]

# Create a timeline plot
plt.figure(figsize=(10, 6))
plt.plot(timestamps, senders, 'o-')
plt.yticks(['You', 'ChatGPT'])  # Set y-axis ticks to sender names
plt.xlabel('Time')
plt.ylabel('Sender')
plt.title('ChatGPT Conversation Timeline')
plt.grid(True)
plt.show()
