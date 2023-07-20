from rapidfuzz import fuzz
from tests.my_vcr import generate_vcr

from lyrics_client.classes.clients.musixmatch_lyrics_client import MusixmatchLyricsClient
from lyrics_client.classes.fetch_lyrics_command import FetchLyricsCommand


my_vcr = generate_vcr("test_musixmatch_client")

@my_vcr.use_cassette
def test_headers_initialized():
    client = MusixmatchLyricsClient()

    assert client.headers is not None


@my_vcr.use_cassette
def test_client_name_is_azlyrics():
    client = MusixmatchLyricsClient()

    assert client.client_name == "musixmatch"


@my_vcr.use_cassette
def test_search_songs():
    client = MusixmatchLyricsClient()
    command = FetchLyricsCommand("in the end", "linkin park", ["musixmatch"])

    search_results = client.search_songs(command)

    assert search_results is not None
    assert 'In the End - Linkin Park' in search_results


@my_vcr.use_cassette
def test_fetch_lyrics():
    URL = 'https://www.musixmatch.com/lyrics/LINKIN-PARK/In-the-End-1'
    EXPECTED_LYRICS = "[Verse 1: Mike Shinoda, Chester Bennington, Both]\nIt starts with one\nOne thing, I don't know why\nIt doesn't even matter how hard you try\nKeep that in mind, I designed this rhyme\nTo explain in due time, all I know\nTime is a valuable thing\nWatch it fly by as the pendulum swings\nWatch it count down to the end of the day\nThe clock ticks life away, it's so unreal\nDidn't look out below\nWatch the time go right out the window\nTryin' to hold on, d-didn't even know\nI wasted it all just to watch you go\n\n[Pre-Chorus: Mike Shinoda]\nI kept everything inside\nAnd even though I tried, it all fell apart\nWhat it meant to me will eventually be\nA memory of a time when I tried so hard\n\n[Chorus: Chester Bennington]\nI tried so hard and got so far\nBut in the end, it doesn't even matter\nI had to fall to lose it all\nBut in the end, it doesn't even matter\n\n[Verse 2: Mike Shinoda, Both]\nOne thing, I don't know why\nIt doesn't even matter how hard you try\nKeep that in mind, I designed this rhyme\nTo remind myself how I tried so hard\nIn spite of the way you were mockin' me\nActin' like I was part of your property\nRemembering all the times you fought with me\nI'm surprised it got so far\nThings aren't the way they were before\nYou wouldn't even recognize me anymore\nNot that you knew me back then\nBut it all comes back to me in the end\n\n[Pre-Chorus: Mike Shinoda]\nYou kept everything inside\nAnd even though I tried, it all fell apart\nWhat it meant to me will eventually be\nA memory of a time when I tried so hard\n\n[Chorus: Chester Bennington]\nI tried so hard and got so far\nBut in the end, it doesn't even matter\nI had to fall to lose it all\nBut in the end, it doesn't even matter\n\n[Bridge: Chester Bennington]\nI've put my trust in you\nPushed as far as I can go\nFor all this, there's only one thing you should know\nI've put my trust in you\nPushed as far as I can go\nFor all this, there's only one thing you should know\n\n[Chorus: Chester Bennington]\nI tried so hard and got so far\nBut in the end, it doesn't even matter\nI had to fall to lose it all\nBut in the end, it doesn't even matter"

    client = MusixmatchLyricsClient()
    lyrics = client.fetch_lyrics(URL)

    assert lyrics is not None
    assert fuzz.ratio(EXPECTED_LYRICS, lyrics) > 80


@my_vcr.use_cassette
def test_get_lyrics():
    EXPECTED_LYRICS = "[Verse 1: Mike Shinoda, Chester Bennington, Both]\nIt starts with one\nOne thing, I don't know why\nIt doesn't even matter how hard you try\nKeep that in mind, I designed this rhyme\nTo explain in due time, all I know\nTime is a valuable thing\nWatch it fly by as the pendulum swings\nWatch it count down to the end of the day\nThe clock ticks life away, it's so unreal\nDidn't look out below\nWatch the time go right out the window\nTryin' to hold on, d-didn't even know\nI wasted it all just to watch you go\n\n[Pre-Chorus: Mike Shinoda]\nI kept everything inside\nAnd even though I tried, it all fell apart\nWhat it meant to me will eventually be\nA memory of a time when I tried so hard\n\n[Chorus: Chester Bennington]\nI tried so hard and got so far\nBut in the end, it doesn't even matter\nI had to fall to lose it all\nBut in the end, it doesn't even matter\n\n[Verse 2: Mike Shinoda, Both]\nOne thing, I don't know why\nIt doesn't even matter how hard you try\nKeep that in mind, I designed this rhyme\nTo remind myself how I tried so hard\nIn spite of the way you were mockin' me\nActin' like I was part of your property\nRemembering all the times you fought with me\nI'm surprised it got so far\nThings aren't the way they were before\nYou wouldn't even recognize me anymore\nNot that you knew me back then\nBut it all comes back to me in the end\n\n[Pre-Chorus: Mike Shinoda]\nYou kept everything inside\nAnd even though I tried, it all fell apart\nWhat it meant to me will eventually be\nA memory of a time when I tried so hard\n\n[Chorus: Chester Bennington]\nI tried so hard and got so far\nBut in the end, it doesn't even matter\nI had to fall to lose it all\nBut in the end, it doesn't even matter\n\n[Bridge: Chester Bennington]\nI've put my trust in you\nPushed as far as I can go\nFor all this, there's only one thing you should know\nI've put my trust in you\nPushed as far as I can go\nFor all this, there's only one thing you should know\n\n[Chorus: Chester Bennington]\nI tried so hard and got so far\nBut in the end, it doesn't even matter\nI had to fall to lose it all\nBut in the end, it doesn't even matter"

    client = MusixmatchLyricsClient()
    command = FetchLyricsCommand("in the end", "linkin park", ["musixmatch"])

    result = client.get_lyrics(command)

    assert result is not None
    assert result.client == "musixmatch"
    assert result.song_title == "in the end"
    assert result.song_artists == "linkin park"
    assert result.lyrics is not None
    assert fuzz.ratio(EXPECTED_LYRICS, result.lyrics) > 80
    assert result.exception is None
