import colorgram as cg

color_list = cg.extract("download.png", 2 ** 32)
color_palette = []

for color in color_list:
    color_palette.append(color.rgb)

print(color_palette)