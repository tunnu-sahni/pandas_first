# product recommend 

import pandas as pd

def simple_recommend(df: pd.DataFrame, user_id: int, user_col='user_id', prod_col='product_id'):
    user_products = set(df[df[user_col]==user_id][prod_col])
    popular = df[prod_col].value_counts().index.tolist()
    recs = [p for p in popular if p not in user_products][:5]
    return recs