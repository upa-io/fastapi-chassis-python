FROM mcr.microsoft.com/devcontainers/python:3.12


RUN apt-get update && apt-get install -y temurin-21-jdk

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*