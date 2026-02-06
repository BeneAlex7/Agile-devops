# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies into a temporary location
# Using --no-cache-dir to keep the image small (though it matters less in builder endpoint)
# Installing to /install for easy copying
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-alpine

WORKDIR /app

# Create a non-root user
RUN adduser -D myuser

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY app/ app/

# Switch to non-root user
USER myuser

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app/main.py"]
