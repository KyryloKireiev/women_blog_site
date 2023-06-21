# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /women_blog_site

# Copy the requirements file and install dependencies
COPY requirements.txt /women_blog_site/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /women_blog_site/

# Expose the port that the Django development server will be listening on
EXPOSE 8000

# Run the Django development server
CMD ["python", "coolsite/manage.py", "runserver", "0.0.0.0:8000"]