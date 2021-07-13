# cURL & Python Foundations Dockerfile
FROM python:3.9-slim-buster

LABEL \
    maintainer='Tim Hull <tim.hull@wwt.com>' \
    version='1.2'

# Set environment variables
ENV MERAKI_TOKEN="6bec40cf957de430a6f1f2baa056b99a4fac9ea0" \
    DNAC_USER="devnetuser" \
    DNAC_PW="Cisco123!"

# Update repositories and install curl
RUN apt-get update && \
    apt-get -y install curl

# Create '/code' directory
RUN mkdir /code

# Set the working directory to '/code'
WORKDIR /code

# Copy requirements files to Image
COPY requirements/ requirements/

# Install Python packages
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements/requirements.txt

# Copy sample files files to Image
COPY sample-files/ sample-files/

# Start the bash shell at container startup
CMD ["/bin/sh"]
