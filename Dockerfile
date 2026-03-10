FROM python:3.11-slim

WORKDIR /app

RUN pip install sentence-transformers numpy

COPY . .

CMD ["python", "ml/sentence_similarity.py"]