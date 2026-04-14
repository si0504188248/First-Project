def dd_to_dms(dd, is_latitude=True):
    """
    Converts Decimal Degrees (DD) to Degrees, Minutes, and Seconds (DMS).
    is_latitude: True for North/South, False for East/West.
    """
    # קביעת הכיוון לפי סוג הקואורדינטה והסימן (חיובי/שלילי)
    if is_latitude:
        direction = "N" if dd >= 0 else "S"
    else:
        direction = "E" if dd >= 0 else "W"
    
    # עבודה עם הערך המוחלט לצורך החישוב המתמטי
    abs_dd = abs(dd)
    
    # 1. המעלות הן החלק השלם
    degrees = int(abs_dd)
    
    # 2. חישוב הדקות מהשארית
    minutes_float = (abs_dd - degrees) * 60
    minutes = int(minutes_float)
    
    # 3. חישוב השניות מהשארית של הדקות ועיגול ל-2 ספרות
    seconds = round((minutes_float - minutes) * 60, 2)
    
    return [degrees, minutes, seconds, direction]

def main():
    print("--- Coordinate Converter (DD to DMS) ---")
    
    try:
        # קליטת המספר מהמשתמש
        user_input = float(input("Enter Decimal Degrees (e.g., -149.9002): "))
        
        # בחירת סוג הקואורדינטה לקביעת הכיוון
        coord_type = input("Is this Latitude? (y/n): ").lower()
        is_lat = True if coord_type == 'y' else False
        
        # ביצוע ההמרה
        result = dd_to_dms(user_input, is_lat)
        
        # הדפסת התוצאה הסופית
        print(f"\nSuccess! The DMS result is: {result}")
        
    except ValueError:
        print("Error: Please enter a valid decimal number.")

if __name__ == "__main__":
    main()