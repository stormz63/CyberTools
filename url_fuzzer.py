import requests

wordlist = [
    "admin", "login", "dashboard", "config", "user", "profile", "private", "test"
]

def fuzz_url(base_url):
    for word in wordlist:
        url = base_url + word
        
        try:
            response = requests.get(url)

            print(f"URL: {url} | Status Code: {response.status_code}")

            if response.status_code == 200:
                print(f"Found accessible URL: {url}")

        except requests.RequestException as e:
            print(f"Error with {url}: {e}")

if __name__ == "__main__":
    base_url = input("Enter the base URL of the site to fuzz (e.g., https://example.com/): ")
    
    if not base_url.endswith('/'):
        base_url += '/'
        
    fuzz_url(base_url)
