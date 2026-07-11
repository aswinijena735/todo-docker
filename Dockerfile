FROM python:3
COPY todo.py .
CMD ["python3", "todo.py"]
