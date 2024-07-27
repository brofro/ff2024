from bs4 import BeautifulSoup

from utils import get_html


def scrape_adp_data(season):
    adp_data = []
    for pos in ["qb", "rb", "wr", "te"]:
        target_url = f"https://fantasydata.com/nfl/ppr-adp/{pos}?season={season}"
        html_content = get_html(target_url)

        if html_content:
            print(
                f"Successfully scraped {len(html_content)} characters from {target_url}"
            )
        else:
            print(f"Failed to scrape {target_url}")

        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table with class 'stats'
        table = soup.find("table", class_="stats")

        # Find all rows in the table body
        rows = table.find("tbody").find_all("tr")

        for row in rows:
            # Extract the required data from each row
            columns = row.find_all("td")

            # Create a dictionary for each row
            player_data = {
                "RK": columns[0].text.strip(),
                "NAME": columns[1].text.strip(),
                "POS": columns[5].text.strip(),
                "RANK": columns[6].text.strip(),
                "ADP": columns[7].text.strip(),
            }

            adp_data.append(player_data)

    return adp_data
