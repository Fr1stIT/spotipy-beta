from test import api_hash, api_id, CLIENT_ID, CLIENT_SECRET, user
import spotipy
import spotipy.util as util
from pyrogram import Client, filters
import time
import threading
import requests
import asyncio
from whydoyoutry import get_string

api_id = api_id
api_hash = api_hash
app = Client("my_account2", api_id=api_id, api_hash=api_hash)

CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET

user = user # имя пользователя
username = user
scope = "user-read-currently-playing"
redirect_uri = "http://localhost:8888/callback"


async def main():
    boolean = False
    bo = True
    last_song = 'testds'
    nothing_song = True
    global currentsong

    await app.start()  # Start the Pyrogram client

    try:
        while True:
            # try:
                token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)

                sp = spotipy.Spotify(auth=token)
                currentsong = sp.currently_playing()

                if currentsong == None:
                    bo = False
                    anw = ("Сорри, что-то я засолил. Так очевидно что никто и не спорит.")  # if no to play
                    print(anw)
                    if nothing_song == True:

                        await app.update_profile(first_name="Frist", bio=anw)
                        nothing_song = False
                else:
                    boolean = True
                    bo = True
                if bo == True:
                    if currentsong['item']['name'] == last_song:
                        boolean = False



                if bo == True:
                    last_song = currentsong['item']['name']
                    nothing_song = True

                else:
                    last_song = ''

                await asyncio.sleep(30)
            #Коментарий



                if boolean == True:
                        song_name = currentsong['item']['name']
                        song_artist = currentsong['item']['artists'][0]['name']
                        anw = get_string(song_artist, song_name)
                        # url = currentsong["item"]["album"]["images"][0]["url"]
                        # r = requests.get(url)
                        # with open(f'./img/{song_name}-{song_artist}.jpg', 'wb') as f:
                        #     f.write(r.content)  # Retrieve HTTP meta-data
                        print(anw)
                        await app.update_profile(first_name="Frist", bio=anw)
                        # print(anw) #debug
                        # await app.set_profile_photo(photo=f'./img/{song_name}-{song_artist}.jpg')
                        #
                        # # Get the photos to be deleted
                        # photos = []
                        # # Use async for to iterate over the asynchronous generator
                        # async for p in app.get_chat_photos("me"):
                        #     photos.append(p)
                        #
                        # # Delete the rest of the photos
                        # await app.delete_profile_photos([p.file_id for p in photos[1:]])

                else:
                        print('Играет та же песня, обновление не будет просходить') #if we havethis song in bio
    except asyncio.CancelledError:
        pass
    finally:
        # Stop the Pyrogram client when done
        await app.stop()


@app.on_message(filters.command('song', prefixes='.') & filters.me)
async def song(_, message):
    global currentsong
    song_name1 = currentsong['item']['name']

    song_artist1 = currentsong['item']['artists'][0]['name']
    anw1 = ("Послушай со мной {} | {}".format(song_name1, song_artist1))  #command .song
    await message.edit(text=anw1)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
