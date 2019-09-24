from YahooFinanceDataLoader import download_bulk_data

assetsList = ['AAPL', 'ADBE', 'AMZN', 'CSCO', 'FB', 'GOOG', 'GOOGL', 'IBM', 'INTC',
          'MSFT', 'NFLX', 'NVDA', 'ORCL', 'QCOM', 'FAKE'] 
start_date = '2018-01-01'
end_date = '2018-01-31'
interval = '1d'
data_directory = 'Downloads/bulk'
maxNThreads = 20
nTrials = 3

failed_downloads = download_bulk_data(assetsList, start_date, end_date, interval, data_directory,
                maxNThreads, nTrials)

print('Failed downloads: ', failed_downloads)