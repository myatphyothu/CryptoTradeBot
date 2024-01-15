import pandas as pd
import asyncio
import sqlalchemy
from binance import Client
import os

import config

os.environ['KMP_DUPLICATE_LIB_OK']='True'

client = Client(config.API_KEY, config.API_SECRET)
engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')


#df.price.plot()


# if price is rising by x % --> buy
# if profit is above 0.15% or loss is -0.15% --> sell

def strategy(entry, lookback, qty, open_position=False):
    
    df = pd.read_sql('BTCUSDT', engine)
    
    # Buy condition
    while True:
        
        lookbackperiod = df.iloc[-lookback:]
        cumret = (lookbackperiod.price.pct_change()+1).cumprod()-1
        
        # if we don't have open posiiton
        if not open_position:
            if cumret[cumret.last_valid_index()] > entry:
                order = client.create_order(symbol='BTCUSDT', side='BUY', type='MARKET', quantity=qty)
                print(order)
                open_position = True
                break
                
    # Sell condition
    if open_position:
        while True:
            sincebuy = df.loc[df.Time > pdf.to_datetime(order['transactTime'], unit='ms')]
            
            if len(sincebuy) > 1:
                sincebuyret = (sincebuy.price.pct_change()+1).cumprod()-1
                last_entry = sincebuyret[sincebuyret.last_valid_index()]
                if last_entry > 0.0015 or last_entry < -0.0015:
                    order = client.create_order(symbol='BTCUSDT', side='SELL', type='MARKET', quantity=qty)
                    print(order)
                    open_position = False
                    break


strategy(0.001, 60, 0.001)