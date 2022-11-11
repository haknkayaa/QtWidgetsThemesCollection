
import PySide2
from qt_material import export_theme

extra = {

    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',

    # Font
    'font_family': 'monoespace',
    'font_size': '12px',
    'line_height': '12px',

    'border' : '1px',

    # Density Scale
    'density_scale': '-2',

    # environ
    'pyside6': True,
    'linux': True,

}

export_theme(theme='dark_teal.xml',
             qss='export/dark_teal.qss',
             rcc='resources.rcc',
             output='export/theme',
             prefix='icon:/',
             invert_secondary=False,
             extra=extra,
             )