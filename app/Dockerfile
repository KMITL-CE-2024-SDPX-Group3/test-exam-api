# Build Stage
FROM python:3.10-slim AS build
WORKDIR /exam-api

# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Final Stage
FROM python:3.10-slim
COPY --from=build /install /usr/local

ENV FLASK_APP=exam_app.py
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /exam-api
COPY . .

CMD ["flask", "run"]