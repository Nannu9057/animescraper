
# Stealth Scraper Agent (AnimeSugeTV.to)

## Target:
- [animesugetv.to](https://animesugetv.to)

## Features:
- Scrapes iframe streaming links from anime episode pages.
- Exposes a FastAPI endpoint to retrieve those links.

## Setup Instructions

1. Install dependencies:
```
pip install -r requirements.txt
playwright install
```

2. Run the API server:
```
uvicorn main:app --reload
```

3. Example usage:
```
GET /get-link/?url=https://animesugetv.to/anime/jujutsu-kaisen-episode-1
```

## Notes:
- This gets the iframe embed URL, not direct .m3u8 stream.
- May require headful mode or proxy if blocked.
