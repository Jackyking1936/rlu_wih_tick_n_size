#%%
for i in range(0):
    print(i)
# %%
{
    "event": "data",
    "data": {
        "symbol": "2330",
        "type": "EQUITY",
        "exchange": "TWSE",
        "market": "TSE",
        "bid": 567,
        "ask": 568,
        "price": 568,
        "size": 4778,
        "volume": 54538,
        "isClose": true,
        "time": 1685338200000000,
        "serial": 6652422
    },
    "id": "<CHANNEL_ID>",
    "channel": "trades"
}
#%%
import pickle
from pathlib import Path

from fubon_neo.sdk import FubonSDK, Mode, Order
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

my_file = Path("./info.pkl")
if my_file.is_file():
    with open('info.pkl', 'rb') as f:
        user_info_dict = pickle.load(f)
    
sdk = FubonSDK()
accounts = sdk.login(user_info_dict['id'], user_info_dict['pwd'], user_info_dict['cert_path'])
active_acc = accounts.data[0]
print(active_acc)

#%%

def handle_message(message):
    print(message)

sdk.init_realtime(Mode.Normal)  # 建立行情連線

stock = sdk.marketdata.websocket_client.stock
stock.on('message', handle_message)
stock.connect()
stock.subscribe({
    'channel': 'trades',
    'symbol': '1587'
})
# %%
def tick_diff_price_cal(limit_up_price, diff_num):
    epsilon = 0.0000001
    for i in range(abs(diff_num)):
        if limit_up_price <= 10:
            limit_up_price = limit_up_price-0.01
        elif limit_up_price <= 50:
            limit_up_price = limit_up_price-0.05
        elif limit_up_price <= 100:
            limit_up_price = limit_up_price-0.1
        elif limit_up_price <= 500:
            limit_up_price = limit_up_price-0.5
        elif limit_up_price <= 1000:
            limit_up_price = limit_up_price-1
        elif limit_up_price > 1000:
            limit_up_price = limit_up_price-5

    return round(limit_up_price+epsilon, 2)

# %%
tick_diff_price_cal(1020, 5)
# %%
