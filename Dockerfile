FROM python:3.11-slim-bookworm
LABEL authors="htsago"

WORKDIR /app

# Security: update apt and install only necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        && rm -rf /var/lib/apt/lists/* \
        && useradd --create-home appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Security: run as non-root user
USER appuser

# Expose the port
EXPOSE 8888

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
