import pandas as pd

data = {
    "customer": ["Ana","Luis","Ana","Pedro","Luis","Ana"],
    "country": ["CO","CO","MX","CO","MX","CO"],
    "product": ["Cement","Cement","Concrete","Cement","Concrete","Concrete"],
    "quantity": [10, -2, 5, 8, 0, 7],
    "price": [50, 50, 60, 50, 60, 60]
}

df = pd.DataFrame(data)
