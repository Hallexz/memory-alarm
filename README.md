### Memory Usage Alert
This is a Python script that monitors the memory usage of the current process and sends an alert if the memory usage exceeds a certain threshold. The script uses the psutil library to get the memory usage information and the requests library to send an HTTP POST request to a specified URL with the memory usage data.

## Requirements
- Python 3.10
- psutil library
- requests library

## Usage

Install the required libraries by running ``` pip install -r requirements.txt. ```
Run the script with ``` python alarm.py. ```

#### Or:

Dockerfile
The provided Dockerfile sets up a Python 3.10 environment, copies the current directory into the container's /app directory, installs the required dependencies from requirements.txt, and runs the alarm.py script when the container starts.

To build the Docker image, run:

```
docker build -t memory-alert .
```
To run the Docker container, use:

```
docker run --rm memory-alert
```
