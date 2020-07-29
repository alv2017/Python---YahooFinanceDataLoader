from YahooFinanceDataLoader import get_assets_from_csv

datafile = 'Data/assets.csv'
fieldlist = ['Symbol', 'Company']

assetList = get_assets_from_csv(datafile, fieldlist)

print(assetList)