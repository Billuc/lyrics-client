from taipan_di import DependencyCollection

from lyrics_client.interfaces import BaseLyricsClient
from lyrics_client.classes.clients import GeniusLyricsClient

def add_lyrics_client(services: DependencyCollection) -> DependencyCollection:
    services.register_pipeline(BaseLyricsClient)\
        .add(GeniusLyricsClient)\
        .register()
    
    return services