## Installation

First, install the required packages:

```
pip install flask requests
```
## Edit gemini_proxy.py!!!

API key ect...

## Start the Proxy

Start the script (for example: `python gemini_proxy.py`), which will make the API available at `http://127.0.0.1:3000/v1/chat/completions`.

## In-Game Commands

Set up the correct configuration in the game using the following commands:

```
/creaturechat url set "http://127.0.0.1:3000/v1/chat/completions"
/creaturechat model set "gemini-1.5-flash"  # or the model name you selected
/creaturechat timeout set 0
```

## Telepítés

Először telepítsd a szükséges csomagokat:

```
pip install flask requests
```

## Szerkezd a gemini_proxy.py-t!!!

API kulcs stb...

## A proxy futtatása

Indítsd el a scriptet (például `python gemini_proxy.py`), amely elérhetővé teszi az API-t a `http://127.0.0.1:3000/v1/chat/completions` címen.

## Parancsok a játékban

A játékban állítsd be a megfelelő beállításokat a következő parancsokkal:

```
/creaturechat url set "http://127.0.0.1:3000/v1/chat/completions"
/creaturechat model set "gemini-1.5-flash"  # vagy az általad választott modell neve
/creaturechat timeout set 0
```
