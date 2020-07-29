import os
import csv

def get_assets_from_csv(csv_file, field_list):
    """
        Input:
            csv_file: location of csv file containing a list of assets
            field_list: csv file field list, it has to contain a field names
                at the top, and a field named 'Symbol'.
                We will be reading assets from this field
        Returns a list of symbols read from csv file       
    """
    # check if csv file exists
    if not os.path.isfile(csv_file):
        msg = "File '{0}' does not exist.".format(csv_file)
        raise FileNotFoundError(msg)
    
    assetlist = []
    
    fieldlist = field_list
    with open(csv_file) as datafile:
        reader = csv.DictReader(datafile, fieldnames = fieldlist)
        #ignore the first row
        next(reader) 
        for row in reader:
            assetlist.append(row['Symbol'].strip())
        
    return assetlist    
    
    