#! /usr/bin/env python3

import getpodcast
from datetime import date
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

opt = getpodcast.options(
    date_from=date.today().strftime("%Y-%m-%d"),
    root_dir='./podcast')

podcasts = {
    "Abertura": "https://omny.fm/shows/abertura-de-mercado/playlists/podcast.rss",
    "BTG": "https://anchor.fm/s/488b72a0/podcast/rss",
    "Agora": "https://feeds.soundcloud.com/users/soundcloud:users:574251438/sounds.rss",
    "Suno": "https://feeds.soundcloud.com/users/soundcloud:users:323314005/sounds.rss",
    "5Fatos": "https://omny.fm/shows/5-fatos/playlists/podcast.rss",
    "FT News Briefing": "https://rss.acast.com/ftnewsbriefing"
}

getpodcast.getpodcast(podcasts, opt)
