import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    both=((products["low_fats"]=='Y') & (products["recyclable"]=='Y'))
    return products.loc[both,['product_id']]