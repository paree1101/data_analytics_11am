import yfinance as yf
import time

# Update these tickers based on your simulation
watch_list = ['AAPL', 'TSLA', 'GOOGL', 'MSFT'] 

def monitor_market():
    print("--- STARTING LIVE DATA FEED ---")
    print("TICKER | PRICE | CHANGE % | DAY RANGE | VARIANCE (GAP)")
    print("-" * 65)
    
    while True:
        for ticker_symbol in watch_list:
            stock = yf.Ticker(ticker_symbol)
            # Fetching 1-day data to get the Open, High, and Low
            data = stock.history(period='1d')
            
            if not data.empty:
                current_price = data['Close'].iloc[-1]
                open_price = data['Open'].iloc[0]
                day_high = data['High'].max()
                day_low = data['Low'].min()
                
                # 1. Percent Change: The distance from the start
                percent_change = ((current_price - open_price) / open_price) * 100
                
                # 2. Variance/Gap: The "swing" or journey of the day
                variance_gap = day_high - day_low
                
                print(f"{ticker_symbol:<6}: ${current_price:<7.2f} | {percent_change:>+6.2f}% | ${day_low:.2f}-${day_high:.2f} | Gap: ${variance_gap:.2f}")
        
        print("-" * 30)
        time.sleep(60) # Wait 1 minute before the next update

if __name__ == "__main__":
    monitor_market()