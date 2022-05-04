class Elevator:
    def __init__(self, floors=5, current_floor=3):
        self.floors = floors
        self.current_floor = current_floor

    def up(self):
        if self.current_floor >= self.floors:
            print('Лифт не может подняться выше')
        else:
            self.current_floor += 1
            print(f'Лифт поднимается на {self.current_floor} этаж')

    def down(self):
        if self.current_floor <= 1:
            print('Лифт не может опуститься ниже')
        else:
            self.current_floor -= 1
            print(f'Лифт опускается на {self.current_floor} этаж')
