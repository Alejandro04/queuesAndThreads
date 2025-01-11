import threading
import queue
import requests

# Define the worker function that fetches data from an API
def api_worker(q, results):
    while not q.empty():
        url = q.get()  # Get the next URL from the queue
        try:
            response = requests.get(url)
            results.append((url, response.status_code, response.text))  # Save the result
        except Exception as e:
            results.append((url, None, str(e)))  # Save the error
        finally:
            q.task_done()  # Mark the task as done

# List of API URLs to call
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
]

# Create a queue and populate it with URLs
url_queue = queue.Queue()
for url in urls:
    url_queue.put(url)

# List to store results
results = []

# Create threads
num_threads = 4  # Number of parallel threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=api_worker, args=(url_queue, results))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Output the results
for result in results:
    print(f"URL: {result[0]}, Status Code: {result[1]}, Response: {result[2][:100]}")  # Show first 100 chars
