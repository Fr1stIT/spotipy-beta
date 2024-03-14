import lyricsgenius as genius
from test import genius_api_key

genius = genius.Genius(genius_api_key)


def extract_lines(text, num_lines):
    lines = text.split("\n")
    kuplet1_lines = []
    kuplet1_found = False

    for line in lines:
        if "Куплет 1" in line or "Verse 1" in line:
            kuplet1_found = True
            continue
        if kuplet1_found and len(kuplet1_lines) < num_lines:
            kuplet1_lines.append(line)
        if len(kuplet1_lines) == num_lines:
            break

    return kuplet1_lines



def join_strings(array):
    result = ''
    temp_result = ''
    for string in array:
        if len(temp_result) + len(string) >= 90:
            break
        else:
            temp_result = result + ' ' + string
        print(len(temp_result))
        result = temp_result
    return result





def get_string(artist: str, song: str):
    # Поиск песни
    songIN = genius.search_song(song, artist)

    try:
        # Получение текста песни
        lyrics = songIN.lyrics
        kuplet1_lines = extract_lines(lyrics, 4)
        print("Куплет 1:", kuplet1_lines)
        kuplet1_lines.insert(0, f'{song}-{artist} |')
        res = join_strings(kuplet1_lines)
        print(res)
        return res
    except:
        return None


