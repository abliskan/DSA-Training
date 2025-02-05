import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df_total_req = confirmations.groupby('user_id')['action'].count().reset_index()
    df_total_conf  =confirmations[confirmations.action =='confirmed'
                           ].groupby('user_id')['action'].count().reset_index()
    df_rate = signups.merge(df_total_req, how = 'left'
               ).merge(df_total_conf , how = 'left', on = 'user_id')
    df_rate['confirmation_rate'] =  ((df_rate.action_y)/ (df_rate.action_x)).round(2)   

    return df_rate.iloc[:,[0,4]].fillna(0)