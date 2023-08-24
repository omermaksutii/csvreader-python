FROM node:14

WORKDIR /app

COPY . /app/

# Install Serverless Framework globally
RUN npm install -g serverless

# Install any necessary dependencies
RUN npm install

# Expose any necessary ports (if applicable)
EXPOSE 3000

CMD ["serverless", "deploy"]
