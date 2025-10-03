from typing import List
from src.client import Case
from src.constants import CaseId
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='CS2 Case Calculator', width=600, height=300)
dpg.setup_dearpygui()


def make_case(name: str, cid: CaseId) -> Case:
    return Case(name=name, price=0.0, item_id=cid.value)


cases = [
    make_case("Dreams & Nightmares Case", CaseId.DREAMERS),
    make_case("Fever Case", CaseId.FEVER),
    make_case("Fracture Case", CaseId.FRACTURE),
    make_case("Kilowatt Case", CaseId.KILOWATT),
    make_case("Recoil Case", CaseId.RECOIL),
    make_case("Revolution Case", CaseId.REVOLUTION),
]


def get_case_prices():
    for case in cases:
        case.get_price()


def calc_sum(rows) -> float:
    sum = 0
    if rows:
        for row in rows:
            first_cell = dpg.get_item_children(row, 1)
            if first_cell:
                quantity: int = first_cell[1]
                quantity = dpg.get_value(quantity)
                value: int = first_cell[2]
                value = dpg.get_value(value)
                value = value * quantity
                sum += value
    return sum


def calc_button_callback():
    sum = calc_sum(rows)
    dpg.set_value(sum_text, f'{sum:.2f} uah')


def update_price_column():
    get_case_prices()
    cases_copy = cases.copy()
    if rows:
        for row in rows:
            first_cell = dpg.get_item_children(row, 1)
            if first_cell:
                for i, case in enumerate(cases_copy):
                    name: int = first_cell[0]
                    name = dpg.get_value(name)
                    if name == case.name:
                        value: int = first_cell[2]
                        dpg.set_value(value, case.price*0.87)
                        cases_copy.pop(i)


with dpg.window() as main_window:
    with dpg.table(header_row=True) as table:

        # creating columns
        dpg.add_table_column(label='Name')
        dpg.add_table_column(label='Quantity')
        dpg.add_table_column(label='Price')

        for i, case in enumerate(cases):
            with dpg.table_row():
                dpg.add_text(case.name)
                dpg.add_input_int(default_value=0)
                dpg.add_input_float(default_value=case.price*0.87)
    dpg.add_separator(label='')
    rows = dpg.get_item_children(table, 1)
    sum = calc_sum(rows)
    sum_text = dpg.add_text(default_value=f'{sum:.2f} uah', label='Sum')
    dpg.add_button(label='Calculate', callback=calc_button_callback)
    dpg.add_button(label='Update Prices', callback=update_price_column)


dpg.show_viewport()
dpg.set_primary_window(main_window, True)

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()
