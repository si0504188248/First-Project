def dd_to_dms(dd, is_latitude=True):
   
    if is_latitude:
        direction = "N" if dd >= 0 else "S"
    else:
        direction = "E" if dd >= 0 else "W"
    
    abs_dd = abs(dd)
    
    degrees = int(abs_dd)
    
    minutes_float = (abs_dd - degrees) * 60
    minutes = int(minutes_float)
    
    seconds = round((minutes_float - minutes) * 60, 2)
    
    return [degrees, minutes, seconds, direction]

def main():
    print("--- Coordinate Converter (DD to DMS) ---")
    
    try:
        user_input = float(input("Enter Decimal Degrees (e.g., -149.9002): "))
        
        coord_type = input("Is this Latitude? (y/n): ").lower()
        is_lat = True if coord_type == 'y' else False
        
        result = dd_to_dms(user_input, is_lat)
        
        print(f"\nSuccess! The DMS result is: {result}")
        
    except ValueError:
        print("Error: Please enter a valid decimal number.")

if __name__ == "__main__":
    main()

 