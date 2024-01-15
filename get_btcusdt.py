import pandas as pd
import asyncio
import sqlalchemy
from binance import Client
from binance import BinanceSocketManager

import config

client = Client(config.API_KEY, config.API_SECRET)
bsm = BinanceSocketManager(client)

def createframe(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','p']]
    df.columns = ['symbol', 'time', 'price']

    # change type to float
    df.price = df.price.astype(float)

    # change time to readable format
    df.time = pd.to_datetime(df.time, unit='ms')

    return df

async def btcusdt():
    socket = bsm.trade_socket('BTCUSDT')
    engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')
    while True:
        await socket.__aenter__()
        msg = await socket.recv()
        frame = createframe(msg)
        frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
        print(frame)
        await asyncio.sleep(1)
    print(createframe(msg))

    

asyncio.run(btcusdt())
