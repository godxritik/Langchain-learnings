import requests
from bs4 import BeautifulSoup


def decode_secret_message(doc_url):
    # Download document
    response = requests.get(doc_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    rows = []

    # Find all table rows
    for tr in soup.find_all("tr"):
        cols = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]

        if len(cols) != 3:
            continue

        try:
            x = int(cols[0])
            char = cols[1]
            y = int(cols[2])
            rows.append((x, y, char))
        except ValueError:
            continue

    if not rows:
        print("No coordinate data found.")
        return

    # Determine grid dimensions
    max_x = max(x for x, _, _ in rows)
    max_y = max(y for _, y, _ in rows)

    # Create grid filled with spaces
    grid = [
        [" " for _ in range(max_x + 1)]
        for _ in range(max_y + 1)
    ]

    # Place characters
    for x, y, char in rows:
        grid[y][x] = char

    # Print grid
    for row in grid:
        print("".join(row))


decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")