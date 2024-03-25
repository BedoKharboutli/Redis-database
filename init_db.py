"""import redis
import requests


def init_db():
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    response = requests.get("https://dummyjson.com/quotes")
    quotes = response.json()
    for q in quotes:
        r.sadd("qoutes", q)


if __name__ == "__main__":
    init_db()"""
