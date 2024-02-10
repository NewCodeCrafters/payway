FROM python:3.10-alpine

LABEL maintainer="oldnewdev2014@gmail.com, bekay.asa@icloud.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev supervisor

WORKDIR /app

# Install any needed packages specified in requirements.in
COPY requirements.in /app/

# Copy the current directory contents into the container at /app
COPY . /app/

# Create and activate virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install project dependencies
RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r requirements.in

# Create an unprivileged user
RUN adduser --disabled-password --no-create-home djangouser

# Switch to the unprivileged user
USER djangouser

# # Command to run when the container starts
# CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
