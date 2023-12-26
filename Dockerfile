FROM python:slim

# Copy all challenge relate files to /root
WORKDIR /root
COPY . /root

# Make gen_flag executable
RUN chmod +x /root/gen_flag
RUN sudo cp enigma_settings.png /app/ 

# Copy all files which user can access to /app
WORKDIR /app

EXPOSE 8080
CMD ["python", "-m", "http.server", "8080"]
