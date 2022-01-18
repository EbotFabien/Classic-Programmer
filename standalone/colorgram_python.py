import colorgram
colors = colorgram.extract('Celebrity.jpg', 3)

first_color = colors[0]
RGB=first_color.rgb
HSL=first_color.hsl
proportioN=first_color.proportion
red=RGB[0]
saturation = HSL[1]
Saturation=HSL.s
#print(RGB)
print(red)
#print(HSL)
#print(proportioN)
print(saturation)
print(Saturation)
