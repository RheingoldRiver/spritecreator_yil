import os
import sprite_creator

SUFFIX = ''
SPRITE_NAME = 'champion'
IMAGE_DIR = 'Sprites/' + SPRITE_NAME #+ ' Images'
DATA_FILE_LOCATION = 'Sprites/' + SPRITE_NAME + 'Sprite' + SUFFIX + '.txt'
IMAGE_WIDTH = 30
IMAGE_HEIGHT = 30
IMAGE_GAP = 1
IMAGES_ACROSS = 13

SPRITE_FILE_NAME = 'Sprites/' + SPRITE_NAME + 'Sprite' + SUFFIX

sprite = sprite_creator.Sprite(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGES_ACROSS, IMAGE_GAP, SPRITE_FILE_NAME)
sprite.create_new()

lines = [
    "{",
    f'\t"imageWidth": {IMAGE_WIDTH},',
    f'\t"imageHeight": {IMAGE_HEIGHT},',
    '\t"sprites": {'
]

images = list(os.listdir(IMAGE_DIR))

for pos, fname in enumerate(images):
    name = fname.replace('.png', '')
    sprite.add_next_image_from_file(IMAGE_DIR + '/' + fname)
    lines.append('\t\t"{}": {{\n\t\t\t"x": {},\n\t\t\t"y": {}\n\t\t}}{}'
                 .format(name.replace('_0.webp', ''), sprite.current_x, sprite.current_y, ',' if pos < len(images) - 1 else ''))

lines.insert(3, f'\t"sheetHeight": {sprite.sheet_height},',)
lines.insert(3, f'\t"sheetWidth": {sprite.sheet_width},',)

lines.append("""\t}""")
lines.append("""}""")

with open(DATA_FILE_LOCATION, 'w', encoding="utf-8") as f:
    f.write('\n'.join(lines))

sprite.save()
