class OurArray:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size

    def get_at(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        return None

    def set_at(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value

    def resize(self, new_size):
        if new_size <= 0:
            return
        
        new_data = [0] * new_size
        
        # copy old values
        for i in range(min(self.size, new_size)):
            new_data[i] = self.data[i]
        
        self.data = new_data
        self.size = new_size

    def print_array(self):
        print(self.data)


# Example
arr = OurArray(3)
arr.set_at(0, 4654)
arr.set_at(1, 921)
arr.set_at(2, 762)

arr.print_array()

arr.resize(5)
arr.print_array()

print(arr.get_at(1))






## 25