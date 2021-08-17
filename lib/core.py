#!/usr/bin/python3



from aux import Binance





def main():
  exchange = Binance()
  symbol = "BTCUSDT"
  timeframe = "1M"
  limit = 16000
  filename = "./"+symbol+"_"+timeframe+".dat"
  df = exchange.GetSymbolKlines(symbol, timeframe, limit)
  df.to_csv(filename, sep='\t')



if __name__ == "__main__":
    main()