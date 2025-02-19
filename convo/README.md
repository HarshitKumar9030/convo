# README.md

# Smart Conversation Generator

This project is a web application that generates conversation starters using AI. It leverages the Google Generative AI API to create engaging questions based on user-defined parameters such as relationship duration, tone, complexity, and interests.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [License](#license)

## Features

- Generate customizable conversation starters.
- User-friendly interface with adjustable parameters.
- Download generated questions as a text file.
- View history of generated questions.

## Technologies Used

- Flask: A lightweight WSGI web application framework.
- python-dotenv: For loading environment variables from a `.env` file.
- google-generativeai: To interact with the Google Generative AI API.
- Tailwind CSS and DaisyUI: For styling the frontend.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd convo
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory and add your environment variables:
   ```
   GEMINI_API_KEY=<your_api_key>
   FLASK_SECRET_KEY=<your_secret_key>
   ```

## Running the Application

To run the application locally, use the following command:
```
flask run
```
The application will be accessible at `http://127.0.0.1:5000`.

## Deployment

To deploy the application on Digital Ocean App Platform, follow these steps:

1. Ensure you have a Digital Ocean account and have set up the App Platform.
2. Create a new app and connect your repository.
3. The platform will automatically detect the `app.yaml` file for configuration.
4. Set the necessary environment variables in the App Settings.
5. Deploy the app.

## License

This project is licensed under the MIT License. See the LICENSE file for details.