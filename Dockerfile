## Parent image
FROM python:3.10-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying ur all contents from local to app
COPY . .

## Run setup.py
RUN pip install --no-cache-dir -e .
#above command tells docker not to use the cached dependencies, libraries, and packages from pycache/ inside src/

# Used PORTS
EXPOSE 8501
#streamlit by default runs on 8501

# Run the app 
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]
#server.address 0.0.0.0 means you can use any IP to host the app page
#when you run streamlit run app\app.py it automatically opens the streamlit page because server.headless=False by default
#but we don't want that to happen in prod servers that it tries to open streamlit page when we run the command