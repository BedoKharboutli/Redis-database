'''import redis
import random


def get_quote():
    r = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)
    quotes = r.srandmember("quotes")

    return quotes


if __name__ == "__main__":
    print(get_quote())'''
