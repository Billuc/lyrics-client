from taipan_di import DependencyCollection

from lyrics_client.classes import FetchLyricsCommand, FetchLyricsResult
from lyrics_client.di import add_lyrics_client
from lyrics_client.interfaces import BaseLyricsClient


class LyricsClient:
    def __init__(self):
        services = DependencyCollection()
        add_lyrics_client(services)

        self._clients = services.build().resolve(BaseLyricsClient)

    def get_lyrics(self, request: FetchLyricsCommand) -> FetchLyricsResult:
        return self._clients.exec(request)
