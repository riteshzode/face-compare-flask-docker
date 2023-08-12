# Face Comparison Flask Project

This is a Flask-based project that allows you to compare images using face recognition.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.7 or later
- Docker (if you intend to use Docker for deployment)

### Installation

1. Create a virtual environment:

   ```python -m venv venv```

   
   Activate the virtual environment:

   ```source venv/bin/activate```


2. Install the required packages using the provided requirements.txt file:

   ```pip install -r requirements.txt```



3. Complete the model installation:

    Run the following command to ensure that the required model or assets are properly installed:
    
       ```python compare_images.py```

## Running the Application

  ### Start the Flask app:
  
  ```bash
  python app.py
  ```

Open a web browser and navigate to http://localhost:5000 to access the application.

## Docker
  A Docker image for this project is available on Docker Hub at ```riteshzode/face-compare-flask ```. To run the application using Docker:


### Pull the Docker image:
  
  Copy code
  ```docker pull riteshzode/face-compare-flask```

### Run a Docker container:

  Copy code
  ```docker run -p 5000:5000 riteshzode/face-compare-flask```

Open a web browser and navigate to http://localhost:5000 to access the application.

### Repository Link - https://hub.docker.com/repository/docker/riteshzode/face-compare-flask/general
