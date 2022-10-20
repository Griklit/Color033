from . import color033

error = color033(color='black', back_color='red', high_light=True, under_line=True)
warning = color033(color='black', back_color='yellow', high_light=True)
info = color033(color='blue')
message = color033(color='white', low_light=True)
