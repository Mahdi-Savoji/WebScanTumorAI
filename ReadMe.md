# Brain Tumor Detection Web Service

## Introduction
This repository is home to a Brain Tumor Detection application that can discern between four states in brain scans:
- Normal
- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor

The application uses a Flask backend for serving the machine learning model and a Vue.js frontend for a user-friendly web interface.

## Getting Started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed the latest version of [Node.js](https://nodejs.org/).
- You have a Windows/Linux/Mac machine capable of running Node and Python.
- You have installed Python 3.6 or higher.

### Installation

#### Frontend Setup

To get the frontend up and running, follow these steps:

1. Navigate to the `frontend` directory from your terminal.
2. Install `serve` npm package globally using the following command:
    ```
    npm install -g serve
    ```
3. To start the frontend application, run:
    ```
    serve -s dist
    ```

#### Backend Setup

For the backend setup, you'll be taking the following steps:

1. Change directory to the `backend` folder:
    ```bash
    cd Flask
    ```
2. (Optional) Set up and activate a Python virtual environment.
3. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Download the [trained model](https://drive.google.com/file/d/13Ny-GL51Il_JluJ1btWggX2YE9lCSbxn/view?usp=sharing) and place it in the `Flask` directory.

5. Start the Flask backend server by running:
    ```bash
    python back.py
    ```

Make sure you have both the frontend and backend servers running to ensure the application functions correctly.

## Usage
After setting up both the frontend and backend:
- Open your web browser and navigate to the URL provided by the `serve` command.
- Upload a brain scan image through the web interface.
- The application will classify the state of the brain as Normal, Glioma Tumor, Meningioma Tumor, or Pituitary Tumor.


## Demonstration
Below is an animated GIF that shows a test run of the Brain Tumor Detection Web Service in action:

![Brain Tumor Detection GIF](Output.gif)


## Contributing
We welcome contributions! If you have suggestions or issues, please open a ticket in the [issues](<GitHub-Issues-Link>) section of this repository.

## Contact
If you want to contact me, please reach out through [GitHub](<GitHub-Profile-Link>).