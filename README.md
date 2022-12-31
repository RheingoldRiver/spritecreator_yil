## Sprite Creator
Edit only `sprite_from_folder.py`, please don't touch `sprite_creator.py`, or if you do & you break stuff don't ask me for help fixing it

Requirement: PIL, no idea what Python version but I wrote it in Python 3.8

This spritesheet creator only supports icons that are all of the same size. It will generate a sheet for you with a uniform gap between images and output some text telling you where you find all of the images. You COULD edit the output with regex, or you could fork the generator and edit the codegen to create what you want in the first place (I think that would be easier).

1. Fork & clone
2. Create a directory `Sprites/` & `cd` into it
3. For each spritesheet you make, you'll make a folder inside of `Sprites`. Say you want to make a sheet called `cats`
4. Create a directory called `cats` inside of `Sprites` and put all your images inside of it
5. Inside of `sprites_from_folder.py` set `SPRITE_NAME=cats` and `IMAGES_ACROSS=something to make it approximately square` (e.g. if you have 68 cat pictures, set it to 8). You may also have to set `IMAGE_WIDTH` and `IMAGE_HEIGHT`. It's recommended to keep `IMAGE_GAP` at 2, but you can adjust that if you want.
6. If you want, you can adjust the text as well, currently it's configured to create some Lua. Remember to escape special characters.
7. Run `sprite_from_folder.py` from the CLI or haha who am I joking from your IDE obviously and a file called `catsSprite.png` should be created for you in the `Sprites/` directory.
8. If you followed the above instructions & it doesn't work open a ticket but if you're
    * Trying to make it work with images of non-uniform dimensions (sorry, good luck!!)
    * Editing `sprite_creator.py`
    
    then that's outside of the scope and I can't help
