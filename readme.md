   # CSV Reader

   Short description of your application.

   ## Prerequisites

   - Docker installed on your local machine.

   ## Getting Started

   These instructions will help you get your Serverless application up and running inside a Docker container.

   1. **Clone the Repository**

      ```bash
      git clone https://github.com/omermaksutii/csvreader-python.git
      ```

   2. **Navigate to the Project Directory**

      ```bash
      cd csvreader-python
      ```

   3. **Build the Docker Image**

      Build the Docker image using the provided Dockerfile. This will create a Docker image containing your Serverless application and its dependencies.

      ```bash
      docker build -t csv-reader-app .
      ```

   4. **Run the Docker Container**

      Run a Docker container based on the image you built. This will start your Serverless application.

      ```bash
      docker run -p 3000:3000 csv-reader-app
      ```

      The `-p` flag maps the container's port to your host's port. Adjust the ports as needed.

   5. **Access Your Application**

      Your Serverless application should now be accessible at `http://localhost:3000`. You can make API requests to the specified endpoints as needed.

      ### Uploading CSV File:

      ```bash
      curl -X POST \
        -H "Content-Type: application/json" \
        -d '{
          "csv_url": "https://vincentarelbundock.github.io/Rdatasets/csv/AER/Affairs.csv",
          "topic": "your_topic"
        }' \
        http://localhost:3000/api/v1/uploadcsv
      ```

      ### Getting CSV Contents:

      ```bash
      curl -X GET \
        "http://localhost:3000/api/v1/listcsv?topic=your_topic"
      ```

      ### Getting CSV Header:

      ```bash
      curl -X GET \
        "http://localhost:3000/api/v1/getcsvheader?filename=your_filename.csv"
      ```

   ## Stopping and Cleaning Up

   To stop and remove the Docker container, use the following commands:

   ```bash
   # List running containers
   docker ps

   # Stop the container (replace CONTAINER_ID with the actual container ID)
   docker stop CONTAINER_ID

   # Remove the container (replace CONTAINER_ID with the actual container ID)
   docker rm CONTAINER_ID
