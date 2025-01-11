import threading
import queue
import requests
import json
from typing import List, Tuple, Union, Dict

ResultType = Tuple[str, int, Union[Dict[str, Union[int, str]], str]]


# Define the worker function that fetches data from an API
def api_worker(q: queue.Queue, results: List[ResultType]):
    while not q.empty():
        url = q.get()  # Get the next URL from the queue
        try:
            response = requests.get(url)
            data = response.json()
            formatted_data = {
                "userId": data["userId"],
                "id": data["id"],
                "title": data["title"],
                "body": data["body"],
            }
            results.append(
                (url, response.status_code, formatted_data)
            )  # Save the result
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
results: List[ResultType] = []

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

formatted_results = []
for result in results:
    data_or_error = result[2]

    if isinstance(data_or_error, dict):
        formatted_results.append(
            {"url": result[0], "status_code": result[1], "data": data_or_error}
        )
    else:
        formatted_results.append(
            {"url": result[0], "status_code": result[1], "error": data_or_error}
        )

print(json.dumps(formatted_results, indent=2))
