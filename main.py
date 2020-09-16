class Carbase:
    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name
        self.carrying = float(carrying)

    def get_photo_le_ext(self):
        type_ = str(self.photo_le_name).split('.')
        return type_[1]


class Car(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, passenger_seat_count):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.passenger_seat_count = int(passenger_seat_count)


class Truck(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.body_whl = body_whl
        whl = str(self.body_whl).split('x')
        self.body_length = float(whl[0])
        self.body_width = float(whl[1])
        self.body_height = float(whl[2])

    def get_body_volume(self):
        return float(self.body_length * self.body_height * self.body_width)


class Specmachine(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, extra):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.extra = extra


def get_car_list(filename):
    car_list = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.replace('\n', '').split(';')
            if line[0] == '':
                pass
            else:
                car_list.append(line)
    return car_list


def main():
    car_list = get_car_list('solution.py')
    for i in car_list:
        for j in i:
            if j[0] == 'car':
                cls = Car(j[0], j[1], passenger_seat_count=j[2], carrying=j[4], photo_le_name=j[3])
            if j[0] == 'truck':
                cls = Truck(j[0], brand=[1], photo_le_name=j[3], body_whl=j[4], carrying=j[5])
            if j[0] == 'spec_machine':
                cls = Specmachine(j[0], j[1], j[3], carrying=j[5], extra=j[6])
    return cls         

if __name__ == '__main__':
    main()
