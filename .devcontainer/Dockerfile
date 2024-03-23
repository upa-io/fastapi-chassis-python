FROM mcr.microsoft.com/devcontainers/python:3.12

# Install JDK 21 (replace '21' with the actual version you want)
RUN apt-get update && apt-get install -y openjdk-21-jdk

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*