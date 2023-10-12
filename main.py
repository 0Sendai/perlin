import dearpygui.dearpygui as dpg
import array
import perlin

"""This code creates a workspace."""
dpg.create_context()

grid_size = 70
width = 1000
heigth = 1000
raw_data = [0] * width * heigth * 3


"""This code is used to generate Perlin noise on a 2D mesh
       with dimensions width and height. """
for x in range(0,width):
    for y in range(0,heigth):

        index = (y * width + x) * 3

    
        octav = 1
        amp = 1
        val = 0
        index = (y * width + x) * 3
        for i in range(0,10):
            val += perlin.perlin(x * octav / grid_size, y * octav / grid_size) * amp
       
            octav *= 2
           
            amp /= 2
              

        val *= 1.2

        if val > 1.0: val = 1.0
        elif val < -1.0: val = -1.0

        color = int(((val + 1.0) * 0.5 )* 255)

        raw_data[index] = color / 255
        raw_data[index+1] = color / 255
        raw_data[index+2] = color / 255
        
           

""""This code is used to create a texture."""

raw_data = array.array('f', raw_data)

with dpg.texture_registry():
    dpg.add_raw_texture(width=width, height=heigth, default_value=raw_data, format=dpg.mvFormat_Float_rgb, tag="texture_tag")



"""This code is used to create a window and display Perlin noise to the user interface."""
with dpg.window(label="perlin"):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='perlin test', width=1000, height=1100)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
