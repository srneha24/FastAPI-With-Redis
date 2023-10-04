FROM python:3.8-slim

WORKDIR /app

# Copy only the necessary files
COPY ./requirements.txt /app/requirements.txt
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start Celery worker and beat in the background using a shell script
COPY ./start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
