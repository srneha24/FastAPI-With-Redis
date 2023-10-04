FROM python:3.8-slim

WORKDIR /app

# Copy only the necessary files
COPY ./requirements.txt /app/requirements.txt
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
