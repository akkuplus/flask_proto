"""
Request some jokes.
"""

import requests


class Loader(object):
    """Load jokes from remote source"""

    def __init__(self, url: str = "https://icanhazdadjoke.com/"):
        print(f"Starting Loader.")
        self._random_joke_collection = []
        self.url = url

    def request_data(self, number_of_jokes: int = 1):
        """Request a number of jokes from remote api"""
        try:
            headers = {"Accept": "text/plain"}
            self._random_joke_collection = []  # always clear list

            for idx in range(number_of_jokes):
                # curl -H "Accept: text/plain" https://icanhazdadjoke.com/
                resp = requests.get(self.url, headers=headers)

                if resp.status_code == 200:
                    joke_test = resp.text
                    joke_test.replace("\n", " ")
                    self._random_joke_collection.append(joke_test)

        except Exception as ex:
            msg = f"Error requesting data from {self.url}, see {ex}."
            print(msg)

    def number_jokes(self):
        """ Joint number and the corresponding joke."""
        numbered_joke = []
        for idx in range(len(self._random_joke_collection)):
            numbered_joke.append(f"{str(idx + 1)}. {self._random_joke_collection[idx]}.")

        self._random_joke_collection = numbered_joke

    def show_all_jokes(self):
        """Print all collected jokes to command prompt"""
        for item in self._random_joke_collection:
            print(f"{item}")

    def get_all_jokes(self) -> list:
        """Return all jokes as list"""
        return self._random_joke_collection

    def run(self):
        self.request_data(5)
        self.number_jokes()
        self.show_all_jokes()


if __name__ == "__main__":
    loader = Loader()
    loader.run()
