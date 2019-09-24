import datetime

def set_time_point(dt):
    """
        The function takes date as an input and returs 
        a timestamp in seconds
        Input: date, format "yyyy-mm-dd"
        Return: date timestamp in seconds since 1970-01-01
        
        Error is raised if date is less than '2000-01-01'
        Error is raised if date is greater than or equal to current date
            (we are dealing with historical data)
    """
    year, month, day = dt.split("-")  
    
    current_time = datetime.datetime.now()
    
    # input date is valid
    try:
        input_time = datetime.datetime(int(year), int(month), int(day)) 
        # input date is less than 2000-01-01
        if (input_time.date() < datetime.date(2000, 1, 1)):
            raise ValueError("The smallest possible date is '2000-01-01'")
        # input date is greater or equal to current date
        if (input_time.date() >= current_time.date()): 
            raise ValueError("Input date is greater than or equal to the current date.")
    except ValueError as err:
        raise err
      
    return int(input_time.timestamp())

if __name__ == '__main__':
    d = '2019-09-15'
    print(set_time_point(d))

    