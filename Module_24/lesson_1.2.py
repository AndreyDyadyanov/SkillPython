class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    screen_resolution = 'WQHD'
    screen_frequency = 60

class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = False

monitor_1 = Monitor()
monitor_2 = Monitor()
monitor_2.screen_frequency = 144
monitor_3 = Monitor()
monitor_3.screen_frequency = 70
monitor_4 = Monitor()

print(monitor_1.screen_frequency, monitor_2.screen_frequency, monitor_3.screen_frequency, monitor_4.screen_frequency)

headphones_1 = Headphones()
headphones_2 = Headphones()
headphones_2.micro = True
headphones_3 = Headphones()
headphones_3.micro = True

print(headphones_1.micro, headphones_2.micro, headphones_3.micro)