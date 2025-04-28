# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Flask (or other required packages)
RUN pip install flask mysql-connector-python


# Expose the Flask default port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
