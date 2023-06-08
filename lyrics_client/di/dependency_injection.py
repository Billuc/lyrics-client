from taipan_di import DependencyCollection

from lyrics_client.interfaces import BaseLyricsClient

def add_lyrics_client(services: DependencyCollection) -> DependencyCollection:
    services.register_pipeline(BaseLyricsClient).register()
    
    return services