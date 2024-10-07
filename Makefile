install:
    pip install -r requirements.txt

test:
    pytest test_main.py

docker-build:
    docker build -t booksdb-app .

docker-run:
    docker run -it booksdb-app

