import os
import sprite_creator

SUFFIX = ''
SPRITE_NAME = 'subattr'
IMAGE_DIR = 'Sprites/' + SPRITE_NAME + ' Images'
DATA_FILE_LOCATION = 'Sprites/' + SPRITE_NAME + 'Sprite' + SUFFIX + '.txt'
IMAGE_WIDTH = 93
IMAGE_HEIGHT = 93
IMAGE_GAP = 2
IMAGES_ACROSS = 3

SPRITE_FILE_NAME = 'Sprites/' + SPRITE_NAME + 'Sprite' + SUFFIX

sprite = sprite_creator.Sprite(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGES_ACROSS, IMAGE_GAP, SPRITE_FILE_NAME)
sprite.create_new()

lines = [
    """const {}_SPRITE_PROPS = {{""".format(SPRITE_NAME.upper())
]

for pos, fname in enumerate(os.listdir(IMAGE_DIR)):
    name = fname.replace('.png', '')
    sprite.add_next_image_from_file(IMAGE_DIR + '/' + fname)
    lines.append('\tsubattr{}: new SpriteCoordinates({}, {}, {}, {}, "{}"),'
                 .format(pos, sprite.current_x, sprite.current_y, IMAGE_WIDTH, IMAGE_HEIGHT,
                         f"{SPRITE_NAME}Sprite.png"))

lines.append("""}""")

with open(DATA_FILE_LOCATION, 'w', encoding="utf-8") as f:
    f.write('\n'.join(lines))

sprite.save()

print("Width: " + str(sprite.sheet_width))
print("Height: " + str(sprite.sheet_height))
