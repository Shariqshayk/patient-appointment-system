# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.16-slim

EXPOSE 5001

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /patient-appointment-system

# Install pip requirements
COPY requirements.txt /patient-appointment-system

# Install required library libmysqlclient (and build-essential for building mysqlclient python extension)
RUN set -eux && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*


RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt


COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "app.py"]
