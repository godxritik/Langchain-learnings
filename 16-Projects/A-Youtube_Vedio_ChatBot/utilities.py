from urllib.parse import urlparse, parse_qs

# Method to extract Video id from Video url
def extract_video_id(url: str) -> str | None:
    try:
        parsed = urlparse(url)

        # Short URL: https://youtu.be/VIDEO_ID
        if parsed.netloc in ("youtu.be", "www.youtu.be"):
            return parsed.path.lstrip("/")

        # Standard URL: https://www.youtube.com/watch?v=VIDEO_ID
        query_params = parse_qs(parsed.query)
        if "v" in query_params:
            return query_params["v"][0]

        # Embed URL: https://www.youtube.com/embed/VIDEO_ID
        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/")[2]

        # Shorts URL: https://www.youtube.com/shorts/VIDEO_ID
        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/")[2]

    except Exception:
        return None

    return None

def format_documents(documents):
    return "\n\n".join([doc.page_content for doc in documents])
