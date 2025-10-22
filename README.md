# VulnSight

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

## Getting Started

To get started with VulnSight, follow these steps:

### Prerequisites

- Python 3.x
- Node.js and npm

### Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/your-username/vulnsight.git
   ```

2. **Install backend dependencies:**
   ```
   pip install -r backend/requirements.txt
   ```

3. **Install frontend dependencies:**
   ```
   npm install --prefix frontend
   ```

### Running the Scanner

1. **Start the backend server:**
   ```
   python backend/app.py
   ```

2. **Start the frontend development server:**
   ```
   npm start --prefix frontend
   ```

The application will be available at `http://localhost:3000`.

## How to Use

1. **Enter the URL** of the web application you want to scan.
2. **Click the "Scan" button** to start the scanning process.
3. **View the results** in the dashboard below.

## Future Development

This project is a work in progress. Future development will focus on:

-   **Implementing AI/ML capabilities** for more intelligent vulnerability detection and prioritization.
-   **Expanding the range of vulnerabilities** that can be detected.
-   **Improving the reporting and dashboard** with more detailed information and visualizations.
-   **Adding authentication and user management** to support multiple users and scans.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.
