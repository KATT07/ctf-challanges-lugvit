FROM python:slim

# Copy all challenge relate files to /root
WORKDIR /root
COPY . /root

# Make gen_flag executable
RUN chmod +x /root/gen_flag
RUN pip install flask ua-parser
RUN echo "error flag not set">/root/flag.txt

EXPOSE 5000
CMD ["python", "/root/app.py"]
