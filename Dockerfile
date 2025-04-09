FROM python:3.13-slim

WORKDIR /app

COPY ../app /app
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]