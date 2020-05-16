def make_car(manufacturer, model, **color):
    """Print car information"""
    color['manufacturer_name'] = manufacturer
    color['model_name'] = model
    return color

color = make_car('BMW', 'M4',
             color='blue')
print(color)