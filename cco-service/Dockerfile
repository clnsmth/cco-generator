# Use a slim Python image
FROM python:3.13-slim

WORKDIR /app

# 1. Copy and install the CORE library first (for better layer caching)
# We copy the entire folder because it's a local dependency
COPY cco-core /app/cco-core

# 2. Copy the SERVICE definition
COPY cco-service/pyproject.toml /app/cco-service/
COPY cco-service/src /app/cco-service/src

# 3. Install dependencies
# We install the service, which automatically pulls in the core from the path
WORKDIR /app/cco-service
RUN pip install --no-cache-dir .

# 4. Run the server
# Host 0.0.0.0 is required for Docker networking
CMD ["uvicorn", "cco_service.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
