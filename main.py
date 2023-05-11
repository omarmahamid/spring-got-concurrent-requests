import time
import requests
from concurrent.futures import ThreadPoolExecutor

concurrent_requests = 100

target_url = 'http://localhost:8080/fetcher'


def send_request(url):
    try:
        response = requests.get(url)

        print(f'Response received: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')


start_time = time.time()

with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
    for _ in range(concurrent_requests):
        executor.submit(send_request, target_url)

total_time = time.time() - start_time

requests_per_second = concurrent_requests / total_time

print(f'Total time: {total_time}')

print(f'Requests per second: {requests_per_second}')
