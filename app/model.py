"""
Request
"""

import requests

class Loader(object):
    """Load jokes from remote source"""

    def __init__(self, url: str = "https://icanhazdadjoke.com/"):
        print(f"Starting Loader.")
        self.random_joke_collection = []
        self.url = url

    def _request_data(self, number_of_jokes: int = 1):
        """Request a number of jokes from remote api"""
        try:
            import requests
            headers = {"Accept": "text/plain"}
            #self.random_joke_collection = []

            for idx in range(number_of_jokes):
                # curl -H "Accept: text/plain" https://icanhazdadjoke.com/
                resp = requests.get(self.url, headers=headers)

                if resp.status_code == 200:
                    self.random_joke_collection.append(resp.text)

        except Exception as ex:
            msg = f"Error requesting data from {Loader.url}, see {ex}."
            print(msg)

    def show_all_jokes(self):
        """Print all colected jokes to command prompt"""
        for item in self.random_joke_collection:
            print(f"{item}")

    def get_all_jokes(self) -> list:
        """Return all jokes as list"""
        return self.random_joke_collection

    def run(self):
        self._request_data(5)
        self.show_all_jokes()


if __name__ == "__main__":

    loader = Loader()
    loader.run()
