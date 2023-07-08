
#Расчет скорости движения машины от точки А до точки Б

def Speed(distance, time):
    """To evaluate the speed of the car by the time
        it takes to move from point A to point B"""
    return distance/time

def check_speed(speed_value):
    if speed_value <= 60:
        result = "Driving as in the sity"
    elif speed_value <= 70:
        result = "Little driving experience"
    elif speed_value <= 90:
        result = "You have enought driving experience"
    elif speed_value <= 120:
        result = "You are an experienced driver"
    else:
        result = "You must not exceed the speed limit"
    return result