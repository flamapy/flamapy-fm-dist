# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /flamapy-api

# Install any needed packages specified in requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
# In case of wish the dev server use CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
