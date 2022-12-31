## Sprite Creator
Edit only `sprite_from_folder.py`

1. Fork & clone
2. Create a directory `Sprites/` & `cd` into it
3. For each spritesheet you make, you'll make a folder inside of that folder. Say you want to make a sheet called `cats`
4. Create a directory called `cats` inside of `Sprites` and put all your images inside of it
5. Inside of `sprites_from_folder.py` set `SPRITE_NAME=cats` and `IMAGES_ACROSS=something to make it approximately square`. You may also have to set `IMAGE_WIDTH` and `IMAGE_HEIGHT`. It's recommended to keep `IMAGE_GAP` at 2, but you can adjust that if you want.
6. If you want, you can adjust the text as well, currently it's configured to create some Lua. Remember to escape special characters.
