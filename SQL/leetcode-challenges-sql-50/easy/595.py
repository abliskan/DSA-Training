import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    region_data = world.loc[(world['area'] >= 3000000) | (world['population']>=25000000)]
    return region_data[['name','population','area']]