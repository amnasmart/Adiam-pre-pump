import requests
import datetime

def fetch_binance_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    return response.json()

def detect_early_pumps(data):
    signals = []
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in data:
        try:
            symbol = item['symbol']
            if not symbol.endswith('USDT'):
                continue
            price_change = float(item['priceChangePercent'])
            volume = float(item['quoteVolume'])

            if price_change > 2 and price_change < 5 and volume > 500000:
                last_price = float(item['lastPrice'])
                entry = round(last_price * 1.001, 6)
                target = round(last_price * 1.03, 6)
                stoploss = round(last_price * 0.99, 6)

                signal = f"""
📈 Coin: {symbol}
📍 Entry: {entry}
🎯 Target: {target}
🛑 Stoploss: {stoploss}
⏰ Time: {now}
💪 Signal Strength: Medium
"""
                signals.append(signal)
        except:
            continue
    return signals

def main():
    print("🔍 Scanning for Early Pump Coins...
")
    data = fetch_binance_data()
    signals = detect_early_pumps(data)

    if signals:
        for s in signals:
            print(s)
    else:
        print("No early pump coins detected at the moment.")

if __name__ == "__main__":
    main()
