FROM python:3.10-alpine

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy application code
COPY bfs_script.py .
COPY data_loader.py .
COPY countries_api.py .
COPY main.py .
COPY countries_graph.json .

EXPOSE 8080

CMD ["python", "main.py"]
