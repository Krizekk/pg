import sys
import requests


def download_url_and_get_all_hrefs(url):
   
    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        
        html = response.content.decode("utf-8", errors="ignore")

        
        parts = html.split('href="')
        for part in parts[1:]:
            link = part.split('"')[0]
            hrefs.append(link)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)
        print(links)
    except IndexError:
        print(
            "Chyba: Nebyla zadána URL adresa. Spusť skript ve tvaru: python sixth.py <url>"
        )
    except Exception as e:
        print(f"Program skoncil chybou: {e}")