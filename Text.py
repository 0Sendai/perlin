import dearpygui.dearpygui as dpg
import array
import test_perlin as perlin

"""This code creates a workspace."""
dpg.create_context()

grid_size = 100
width = 400
heigth = 400
rawdata = [0] * width * heigth * 3
octav = 5

def perlin():
    """This code is used to generate Perlin noise on a 2D mesh
       with dimensions width and height. """
    for x in range(0,width):
        for y in range(0,heigth):

            index = (y * width + x) * 3

            angle = 0

            val = perlin.perlin(x octav /grid_size, y octav/grid_size)

            val = 1.2

            if val > 1.0: val = 1.0
            elif val < -1.0: val = -1.0

            color = int(((val + 1.0) 0.5 )* 255)

            raw_data[index] = val
            raw_data[index+1] = val
            rawdata[index+2] = val

""""This code is used to create a texture."""
perlin()
raw_data = array.array('f', raw_data)

with dpg.texture_registry():
    dpg.add_raw_texture(width=width, height=heigth, default_value=raw_data, format=dpg.mvFormat_Float_rgb, tag="texture_tag")



"""This code is used to create a window and display Perlin noise to the user interface."""
with dpg.window(label="perlin"):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='perlin test', width=500, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()
