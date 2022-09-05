birthday_candles = [3, 2, 1, 3, 9]
dict_candles = {}

def birthdayCakeCandles(candles):
    tallest = max(candles) # First, set the height of the max height candle.
    for i in candles: # Iterate through array
        if i in dict_candles: # If value at index in the dictionary, add 1 to occurrences
            dict_candles[i] += 1
        else:
            dict_candles[i] = 1 # Else, add it to dictionary as first occurrence
    return dict_candles[tallest] # Return the count of the highest candle.

print(birthdayCakeCandles(birthday_candles))

