# Write you Pandas statement below
import pandas as pd

def find_match_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[(products['low_fats'] == 'Y') & products['recyclable'] == 'Y']
    return result[['product_id']]