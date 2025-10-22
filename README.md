# VulnSight

**Plan and code handcrafted by Gautham balaji.**

VulnSight is a web vulnerability scanner designed to help you identify and address security weaknesses in your web applications. It provides a foundation for building a comprehensive security testing tool.

## Features

- **Automated Vulnerability Scanning:** Scan any web application for common security vulnerabilities.
- **Web Crawler:** Discovers links on a page to scan multiple pages of a website.
- **Dashboard:** View scan results in a user-friendly interface.
- **Actionable Insights:** Get detailed reports with clear explanations.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** React, Axios
- **Vulnerability Scanner:** Requests, BeautifulSoup

## Project Structure

The project is organized into two main directories:

- `backend/`: Contains the Flask application that powers the vulnerability scanner.
- `frontend/`: Contains the React application that provides the user interface.

## Getting Started: How to Execute This Code

To get started with VulnSight, follow these steps in order:

### Prerequisites

- **Python 3.x:** Make sure Python is installed on your system.
- **Node.js and npm:** Make sure Node.js and the npm package manager are installed.

### Step 1: Installation

First, you need to set up the project and install all the necessary dependencies for both the frontend and backend.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/vulnsight.git
    cd vulnsight
    ```

2.  **Install backend dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Install frontend dependencies:**
    ```bash
    npm install --prefix frontend
    ```

### Step 2: Running the Scanner

Once the installation is complete, you need to start both the backend and frontend servers.

1.  **Start the backend server:**
    Open a new terminal and run the following command:
    ```bash
    python backend/app.py
    ```
    This will start the Flask server on `http://127.0.0.1:5000`. Keep this terminal running.

2.  **Start the frontend development server:**
    Open a **second** terminal and run the following command:
    ```bash
    npm start --prefix frontend
    ```
    This will start the React development server and automatically open the application in your web browser at `http://localhost:3000`.

### Step 3: How to Use the Application

1.  Navigate to `http://localhost:3000` in your browser.
2.  **Enter the URL** of the web application you want to scan into the input field.
3.  **Click the "Scan" button** to begin the scanning process.
4.  **View the results** in the dashboard as they appear.

## Future Development

This project is a work in progress. Future development will focus on:

-   **Implementing AI/ML capabilities** for more intelligent vulnerability detection and prioritization.
-   **Expanding the range of vulnerabilities** that can be detected.
-   **Improving the reporting and dashboard** with more detailed information and visualizations.
-   **Adding authentication and user management** to support multiple users and scans.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
