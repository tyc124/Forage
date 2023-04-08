from app import dash_app

def test_header(dash_input):
    dash_input.start_server(dash_app)
    dash_input.wait_for_element('#header', timeout=10)


def test_visualization_exists(dash_input):
    dash_input.start_server(dash_app)
    dash_input.wait_for_element('#visualzation', timeout=10)


def test_region_exists(dash_input):
    dash_input.start_server(dash_app)
    dash_input.wait_for_element('#region_picker', timeout=10)