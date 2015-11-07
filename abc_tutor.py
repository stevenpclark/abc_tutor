import pyglet
import random
import colorsys

num_sound_variants = 4

window = pyglet.window.Window(fullscreen=True)
#window = pyglet.window.Window(fullscreen=False)
window.set_exclusive_keyboard()

label = pyglet.text.Label('', anchor_x='center', anchor_y='center')

font_names = ['Geneva', 'Georgia', 'Arial', 'Tahoma', 'Verdana', 'Times New Roman', 'Raleway', 'Courier New', 'Lucida Console']

sound_dict = dict()
keys = range(97,123) #a-z
keys.extend(range(48,58)) #0-9
for k in keys:
    c = chr(k)
    variants = []
    for i in range(num_sound_variants):
        fn = 'sounds/%s%d.wav'%(c,i)
        variants.append(pyglet.media.load(fn, streaming=False))
    sound_dict[c] = variants

padding = 200

@window.event
def on_draw():
    window.clear()
    label.draw()


@window.event
def on_key_press(symbol, modifiers):
    try:
        c = chr(symbol)
        variants = sound_dict.get(c, None)
        if variants:
            random.choice(variants).play()
            if random.random() > 0.5:
                label.text = c
            else:
                label.text = c.upper()

            label.x = random.randint(padding, window.width-padding)
            label.y = random.randint(padding, window.height-padding)
            label.font_name = random.choice(font_names)
            label.font_size = random.randint(128,384)
            #color = [random.randint(100,255) for i in range(3)]
            color = colorsys.hsv_to_rgb(random.random(), 1, 1)
            color = [int(x*255) for x in color]
            color.append(255)
            label.color = color
    except ValueError:
        pass

pyglet.app.run()

