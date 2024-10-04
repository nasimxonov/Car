from pydub import AudioSegment
from pydub.playback import play

class Car():
    def __init__(self, nomi,narxi, raqami,brendi="Chevrolet", max_tezligi=220, rangi="black"):
        self.name = nomi
        self.brend = brendi
        self.price  = narxi
        self.number = raqami
        self.max_speed = max_tezligi
        self.color = rangi
        self.speed = 0

    def info(self):
        print(f"nomi : {self.name} , narxi : {self.price} , rangi : {self.color}")

    def start(self):
        if self.speed > 0:
            print("mashina allaqachon o't olgan ")
            return
        
        
        sound = AudioSegment.from_mp3('dars/OOP/sound.mp3')
        print("Moshina ishga tushdi...")
        play(sound) 
        self.speed =5

    def stop(self):
        if self.speed ==0:
            print("Mashina allaqachion to'xtagan")
        else:
            print("Mashina to'xtadi")
            self.speed = 0

    def add_speed(self,a):
        if self.speed + a > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed+=a
        print("tezlik oshdi",self.speed)
    
    def sub_speed(self,a):
        if self.speed-a<0:
            self.speed =0
            print("Mashina to'xtadi .")
        else:
            self.speed -=a
            print("Mashina sekinlashmoqda .. ",self.speed)

            

c1 = Car("BMW M5", 'BMW', 200, "40A777AA", 400, "black")
cars = []
for i in range(2):
    nomi = input("nomi : ")
    narx = int(input("narx : "))
    raqami = input("raqami")
    cars.append(Car(nomi,narx,raqami))


for i in cars:
    print(f"nomi : {i.name} , narxi {i.price}")
    i.start()