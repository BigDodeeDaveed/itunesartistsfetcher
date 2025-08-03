import requests
import sys

# loops through the json file so we can take what we want from it
while True:

    artist = input("Enter the artist's name: ")

    if artist.strip().capitalize() == "Exit":

        sys.exit("Terminating window.")

# takes all of the info that the itunes api provides
    response = requests.get(f"https://itunes.apple.com/search?term={artist}&media=music&entity=song&limit=10")

# converts it into a json file so we can take specific things from it
    data = response.json()

    if data and "results" in data and len(data["results"]) > 0:
        for result in data["results"]:
            track_name = result.get("trackName")

            print(f"{track_name}")

            
    else:
        print("No results found.")
        