from client import Case
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")

dpg.show_viewport()

dreamers_case = Case(name='Dreams & Nightmares Case',
                     price=0.0, item_id=176288467)
dreamers_case.get_price()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    # print("this will run every frame")
    dpg.render_dearpygui_frame()

dpg.destroy_context()
