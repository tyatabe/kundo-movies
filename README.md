# kundo-movies
Solution to coding challenge from Kundo

# Running the application with Docker
1. Copy `api/settings.toml` to `api/.secrets.toml`
```shell
cp api/settings.toml api/.secrets.toml
```
and fill in the secret values.
2. Run the following command to build and run the application.
``` shell
docker-compose up --build
```
3. The search web app will be available at `http://localhost:8000/search`.
4. The API will be available at `http://0.0.0.0:4000/v1/search`.
