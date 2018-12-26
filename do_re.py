import re
def name_ofemail(addr):
    if re.match(r'^[a-zA-Z0-9-]+@[a-zA-Z0-9-]+(.[a-zA-Z0-9-]{3})+$',addr):
        return True
    else:
        return False
print(name_ofemail('3213'))