# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
#RUN pip install --upgrade pip
#RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8503 available to the world outside this container
EXPOSE 8503

# Run streamlit when the container launches
CMD ["streamlit", "run", "association_rule_assignment.py"]
