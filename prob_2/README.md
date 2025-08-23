# Django Currency Converter

This is a web application built with Django for converting between world currencies and viewing historical exchange rate data.

The application is intended for users who need to perform currency conversions or review recent exchange rate trends.

## Features

This project includes the following features:

* **Real-Time Conversion:** Fetches current exchange rates from an external API to perform conversions.
* **Comprehensive Currency Support:** Populates selection menus with a list of available world currencies.
* **Historical Data Charting:** Displays a 30-day historical line chart for the selected currency pair after a conversion is made.

## Technology Stack

The application is built with the following technologies:

* **Backend:** Python, Django
* **Frontend:** HTML, JavaScript, Tailwind CSS
* **Charting:** Chart.js
* **APIs:**
    * [ExchangeRate-API](https://www.exchangerate-api.com/) provides the real-time conversion data.
    * [Frankfurter.app](https://www.frankfurter.app/) provides the historical data for the charts.
* **Environment:** `python-dotenv` is used for managing the API key.

## Local Setup and Installation

To run this project locally, follow the steps below.

1.  **Clone the repository:**
    Download the source code to your local machine.
    ```
    git clone <your-repository-url>
    cd <project-folder>
    ```

2.  **Create and activate a virtual environment:**
    This isolates the project's dependencies.
    ```
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    This command reads the `requirements.txt` file and installs the necessary packages.
    ```
    pip install -r requirements.txt
    ```

4.  **Create the `.env` file:**
    Create a file named `.env` in the root project directory and add your API key.
    ```
    API_KEY=YOUR_API_KEY_HERE
    ```
    *A free API key can be obtained from [exchangerate-api.com](https://www.exchangerate-api.com/).*

5.  **Apply database migrations:**
    This command initializes the Django database.
    ```
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```
    python manage.py runserver
    ```

The application will then be available at `http://127.0.0.1:8000/`.