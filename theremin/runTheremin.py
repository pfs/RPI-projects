from gpiozero import DistanceSensor
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client


_max_pitch=100

def main():
    sensor = DistanceSensor(echo=17, trigger=4)
    sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

    last_pitch=-1
    
    while True:

        d=sensor.distance
        pitch = round(d * 100 + 30)
        pitch = last_pitch if pitch>_max_pitch else pitch
        last_pitch = pitch
        print(last_pitch,pitch)
        if pitch<0 :continue

        sender.send_message('/play_this', pitch)
        sleep(0.1)

if __name__ == "__main__":
    main()

    
