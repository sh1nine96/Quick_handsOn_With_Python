from ctypes import sizeof


class Computer:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage

    def print_specs(self):
        print("display size: " + self.size)
        print("display storage: " + self.storage)


low_spec = Computer("13", "256GB")
high_spec = Computer("27", "1TB")


print("low_spec_computer: ")
low_spec.print_specs()
print("high_spec_computer")
high_spec.print_specs()
