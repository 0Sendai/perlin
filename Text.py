import dearpygui.dearpygui as dpg
import array
import test_perlin as perlin

"""Creating a working field"""
dpg.create_context()

grid_size = 100
width = 400
heigth = 400
rawdata = [0] * width * heigth * 3
octav = 5

def perlin():
    """This code is used to generate Perlin noise on a 2D mesh
       with dimensions width and height. Each point (x, y) in
       the grid calculates a noise value and uses it to determine
       the brightness of the pixel's color. The resulting values
       are stored in the raw_data array, which will
       be used to create an image or other noise visualization."""
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

""""This code is used to create a texture based
    on the generated Perlin noise and register
    it using the dpg library."""
perlin()
raw_data = array.array('f', raw_data)

with dpg.texture_registry():
    dpg.add_raw_texture(width=width, height=heigth, default_value=raw_data, format=dpg.mvFormat_Float_rgb, tag="texture_tag")



"""This code is used to create a window displaying
   the generated Perlin noise and display it in the
   user interface using the Dear PyGui library."""
with dpg.window(label="perlin"):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='perlin test', width=500, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
dpg.destroy_context()
