import requests
import redis
import json
import random

# Anslut till Redis-databasen
redis_db = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)


# Funktion för att hämta citat från webbkälla och lagra dem i Redis-databasen
def lagra_citat():
    url = "https://dummyjson.com/quotes"
    response = requests.get(url)
    citat_data = json.loads(response.text)
    citat_list = citat_data["quotes"]
    for citat in citat_list:
        redis_db.rpush("citat", citat["quote"] + " ##by author : " + citat["author"])


# Funktion för att hämta ett slumpmässigt citat från Redis-databasen
def slumpmassigt_citat():
    antal_citat = redis_db.llen("citat")
    slumpmässigt_index = random.randint(0, antal_citat)
    citat = redis_db.lindex("citat", slumpmässigt_index)
    return citat


def main():
    while True:
        print("1. Get a random quote")
        print("2. Save quotes to database")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Hämta ett slumpmässigt citat och visa det
            print("----->", slumpmassigt_citat(), "<-----")

        elif choice == "2":
            # Lagra citat i Redis-databasen
            lagra_citat()
            print("Quotes saved to database!")

        elif choice == "3":
            break

        else:
            print("Invalid number, choose between 1 - 2")


if __name__ == "__main__":
    main()
