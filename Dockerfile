FROM python:3.11.2
WORKDIR /work_review_notifications
COPY requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY main.py
CMD ["python3", "main.py"]
