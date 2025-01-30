import pandas as pd

def find_customer_name(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer[(customer['referee_id'].isnull()) | (customer['referee_id'] != 2)][['name']]
    return customer