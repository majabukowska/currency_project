
# Currency project

## Overview
This application provides a simple web interface to interact with the National Bank of Poland's API to fetch and display exchange rate data for a specified currency and date. The application is built using Flask, a lightweight WSGI web application framework in Python.

## Features
- Fetch the average exchange rate for a specific date.
- Display maximum and minimum average exchange rates over a given period.
- Show the major differences between the buy and ask rate for recent days.

## Installation

### Prerequisites
- Python 3.9+
- Flask
- Requests

### Setup
1. Clone this repository to your local machine using:
   ```
   git clone [repository-url]
   ```
2. Navigate to the repository directory:
   ```
   cd [repository-directory]
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
To run the application locally, execute:
```
python app.py
```
Alternatively, to run it in a Docker container, ensure you have Docker installed and run:
```
docker build -t exchange-rate-app .
docker run -p 80:80 exchange-rate-app
```

## Testing
To execute tests, run:
```
python -m unittest
```
