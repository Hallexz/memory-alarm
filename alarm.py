import os
import psutil
import requests

def memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    total_memory = psutil.virtual_memory().total
    return (mem_info.rss / total_memory) * 100

def send_alert(memory_used):
    url = "http://testalert.com/alert"
    data = {"memory_used": memory_used}
    response = requests.post(url, data=data)
    return response.status_code

def main():
    memory_used = memory_usage()
    print(f"Memory used: {memory_used}%")
    if memory_used > 90:
        send_alert(memory_used)

if __name__ == "__main__":
    main()
