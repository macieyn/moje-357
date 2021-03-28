# https://stackoverflow.com/questions/41022893/monitoring-icy-stream-metadata-title-python

import re
import requests
import sys
import logging
import traceback
from requests.exceptions import ConnectionError
import time

from io import BytesIO


def icy_monitor(stream_url, callback=None):

    r = requests.get(stream_url, headers={'Icy-MetaData': '1'}, stream=True)
    if r.encoding is None:
        r.encoding = 'utf-8'

    byte_counter = 0
    meta_counter = 0
    metadata_buffer = BytesIO()

    metadata_size = int(r.headers['icy-metaint']) + 255

    data_is_meta = False


    for byte in r.iter_content(1):

        byte_counter += 1

        if (byte_counter <= 2048):
            pass

        if (byte_counter > 2048):
            if (meta_counter == 0):
                meta_counter += 1

            elif (meta_counter <= int(metadata_size + 1)):

                metadata_buffer.write(byte)
                meta_counter += 1
            else:
                data_is_meta = True

        if (byte_counter > 2048 + metadata_size):
            byte_counter = 0

        if data_is_meta:

            metadata_buffer.seek(0)

            meta = metadata_buffer.read().rstrip(b'\0')

            m = re.search(br"StreamTitle='([^']*)';", bytes(meta))
            if m:
                stream_title = m.group(1).decode(r.encoding, errors='replace')
                title_groups = re.search(r"(.*)\s-\stext=\"(.*)\"", stream_title)
                author = title_groups.group(1)
                title = title_groups.group(2)

                if callback:
                    callback(author, title)

            byte_counter = 0
            meta_counter = 0
            metadata_buffer = BytesIO()

            data_is_meta = False


def print_title(author, title):
    print('Title: {} - {}'.format(author, title))


def post_song(artist, track):
    print('Title: {} - {}'.format(artist, track))
    tries = 5
    while tries:
        try:
            repsonse = requests.post('http://127.0.0.1:5000/api/track/', json={'q': f'{artist} {track}'})
            break
        except ConnectionError:
            logging.error(f'Request failed for "{artist} - {track}". Try: {tries}')
            tries -= 1
            time.sleep(10)



if __name__ == '__main__':
    stream_url = 'https://n13a-eu.rcs.revma.com/an1ugyygzk8uv?rj-ttl=5&rj-tok=AAABeHhJIacAZ6M8eJFwkxiumQ'
    icy_monitor(stream_url, callback=post_song)