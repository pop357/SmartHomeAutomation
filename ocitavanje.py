shared_temperature = None
shared_humidity = None
shared_pressure = None

def set_shared_temperature(temperature):
    global shared_temperature
    shared_temperature = temperature

def get_shared_temperature():
    return shared_temperature

def set_shared_humidity(humidity):
    global shared_humidity
    shared_humidity = humidity

def get_shared_humidity():
    return shared_humidity

def set_shared_pressure(pressure):
    global shared_pressure
    shared_pressure = pressure

def get_shared_pressure():
    return shared_pressure
