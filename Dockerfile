FROM python:3.11.2
WORKDIR /work_review_notifications
COPY requirements.txt /work_review_notifications
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY main.py /work_review_notifications
CMD ["python3", "main.py"]
