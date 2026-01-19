# Use a slim Python image
FROM python:3.13-slim

WORKDIR /app

# --- STEP 1: Install Core ---
COPY cco-core /app/cco-core

# Enter the core folder and install it
WORKDIR /app/cco-core
RUN pip install --no-cache-dir .

# --- STEP 2: Install Service ---
WORKDIR /app

# Copy the service folder
COPY cco-service /app/cco-service

# Enter the service folder and install it
WORKDIR /app/cco-service
# Now when this runs, it will find cco-core is already installed!
RUN pip install --no-cache-dir .

# 4. Run the server
# Host 0.0.0.0 is required for Docker networking
CMD ["uvicorn", "cco_service.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
