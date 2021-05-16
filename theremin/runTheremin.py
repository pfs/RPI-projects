from gpiozero import DistanceSensor
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client


def main():
    sensor = DistanceSensor(echo=17, trigger=4)
    sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

    while True:

        d=sensor.distance
        pitch = round(d * 100 + 30)
        #print(d,pitch)
        sender.send_message('/play_this', pitch)
        sleep(0.1)

if __name__ == "__main__":
    main()

    
