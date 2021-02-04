def sma(data_feed:list,time_period:int=None) -> float:
    """
        simple moving average
        
        formula : 

        (a1+a2+a3+a4+a5.....) / n
        note : n is number of elements

        exmaple :
        
        >>> from trindipy import sma
        >>> a = [22,333.412,234.787,2234.123]
        >>> sm = sma(data_feed=a)
        >>> print(sm)
        ... 706.0805
        >>> print(type(sm))
        ... float

    """
    if not time_period:
        time_period = len(data_feed)
    else:
        time_period = time_period

    return sum(data_feed) / time_period