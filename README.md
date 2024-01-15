# Convert to decimal time
A small python library to convert standard time to decimal time. 

# What is decimal time 
Decimal time is the representation of the time of day using units which are decimally related. Essentially decimal times operates with powers of 10. 

- DTs = Decimal Time second
- DTm = Decimal Time minute
- DTh = Decimal Time hour
This classification is unofficial

| Unit     | Decimal Time | Equivalent in SI seconds |
|----------|--------------|--------------------------|
| Seconds  | 1 DTs        | 0.864                    |
| Minutes  | 1 DTm        | 86.4                     |
| Hours    | 1 DTh        | 8,640                    |

# Functions
The following are the descriptions of the functions and their required input. 
- `getSeconds`: Takes an int argument that represents the SI seconds and returns an int that represents the DT seconds.
- `getMinutes`: Takes an int argument that represents the SI seconds and returns an int that represents the DT minutes.
- `getHours`: Takes an int argument that represents the SI seconds and returns an int that represents the DT hours. 
- `getTimeNow`: Gets the system time and returns an array that contains the current hours, minutes and seconds in DT. 

# Example usage
After you install the library using the command `pip install /path/to/file/convertToDecimalTime_TolisSth-1.0.0-py3-none-any.whl`, you can start using the library writing scripts like the following: 
```
from convert import getMinutes

x = int(input("Minutes: ")) 
print("Minutes: ", getMinutes(x)) 
```
output: 
Let's say that my input is 3600, the output will be: `Minutes: 41`.

# Motiation for this project 
The motivation for this small project came from an article featured on Hacker news that contained a link to the wikipedia article for decimal time. Decimal is not widely used and that's why there was no library to handle the conversions. It is likely that this library won't be used anywhere because of how little decimal time is used but it is great to always have the option. 
