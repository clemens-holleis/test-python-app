FROM python
COPY app.py /app.py
RUN pip install flask
# CMD tail -f /dev/null
CMD python /app.py