import requests
import typing
import numpy as np
import sqlite3

import imagehash as imh
from PIL import Image

def is_valid_token(token: str):
    """
    Check if a token is valid
    Pretty sure i'll remove this later
    """
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def get_hashes(img: Image) -> typing.List[str]:
    """
    You can get the hashes of an image by passing the image as a PIL Image object, or by passing the image url,

    Returns a list of hashes, which can be used to compare images.
    Returns 4 types of hashes:

    - phash: Perceptual hash
    - difference-hash: Difference hash
    - wavelet-hash: Wavelet hash
    - average-hash: Average hash

    phash is the one I recommend.
    https://content-blockchain.org/research/testing-different-image-hash-functions/
    """

    img = Image.open(requests.get(img, stream=True).raw)
    arr = np.array(img)
    arr[arr[:, :, 3] == 0] = 0
    img = Image.fromarray(arr).convert('RGB')    
    return [imh.phash(img), imh.dhash(img), imh.whash(img), imh.average_hash(img)]

def recognize_pokemon(image: Image, _type_: str="base") -> str:
    """
    Search for a pokemon in the database with given hash
    """
    if _type_ not in ("base", "cjk"):
        _type_ = "base"

    database = sqlite3.connect("database.db")
    cursor = database.cursor()
    hashes = get_hashes(image)

    if _type_ == "base":
        query = f"""
        SELECT name FROM pokemontable
        WHERE hash = '{hashes[0]}'
        """
        cursor.execute(query)
        pokemon = cursor.fetchone()
        if pokemon is None:
            raise Exception("Pokémon not found in database")
        else:
            return pokemon[0]
            
    elif _type_ == "cjk":
        query = f"""
        SELECT bname FROM pokemontable
        WHERE hash = '{hashes[0]}'
        """
        cursor.execute(query)
        pokemon = cursor.fetchone()
        if pokemon is None:
            raise Exception("Pokémon not found in database")
        else:
            return pokemon[0]