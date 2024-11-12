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
