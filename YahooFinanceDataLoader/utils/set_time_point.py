import datetime

def set_time_point(dt):
    """
        The function takes date as an input and returs 
        a timestamp in seconds
        Input: date, format "yyyy-mm-dd"
        Return: date timestamp in seconds since 1970-01-01
    """
    year, month, day = dt.split("-")  
    
    # input date is valid
    try:
        input_time = datetime.datetime(int(year), int(month), int(day)) 

    except ValueError as err:
        raise err
      
    return int(input_time.timestamp())

if __name__ == '__main__':
    d = '2019-02-15'
    print(set_time_point(d))

    