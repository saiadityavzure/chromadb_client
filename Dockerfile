FROM python:latest
WORKDIR /app
COPY requirements_chroma.txt /app/
RUN pip install -r requirements_chroma.txt
COPY . /app/
CMD ["python", "chroma_client.py"]