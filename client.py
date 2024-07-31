import requests
import time

def long_polling_client():
    url = 'http://localhost:8080/long-poll'
    start_time = time.time()
    
    try:
        with requests.get(url, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    print(f"Received: {line.decode('utf-8')}")
                if time.time() - start_time > 900:  # 15 minutes
                    break
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    long_polling_client()
