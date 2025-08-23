# Django Weather Application

## Description

This is a Django-based web application that allows users to check the current weather for a specified city. It utilizes the OpenWeatherMap API to fetch real-time weather data. The user interface includes an autocomplete feature to help users select from a predefined list of cities.

---

## Features

* Fetches and displays current weather data for a given city.
* Autocomplete search functionality for city names.
* Displays temperature in both Celsius and Kelvin.
* Shows additional weather details including humidity and wind speed.
* Handles API errors and invalid city name inputs gracefully.

---

## Setup and Installation

To run this project locally, follow these steps:

1.  **Prerequisites**
    * Python 3.x
    * pip

2.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name/prob_1
    ```

3.  **Create and activate a virtual environment**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

4.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file by running `pip freeze > requirements.txt` in your activated environment.)*

5.  **Set up environment variables**
    * Create a file named `.env` in the root project directory (`prob_1`).
    * Add your OpenWeatherMap API key to the `.env` file as follows:
        ```
        API_KEY=your_actual_api_key_here
        ```

6.  **Run database migrations**
    ```bash
    python manage.py migrate
    ```

7.  **Start the development server**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

## Dependencies

* Django
* requests
* python-decouple