# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage   # encapsulated (private) attribute

    # Getter for storage
    def get_storage(self):
        return self.__storage

    # Setter for storage
    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Storage must be positive!")

    def phone_info(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"

# Inherited class (Polymorphism with phone_info)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    # Overriding method (Polymorphism)
    def phone_info(self):
        return f"{self.brand} {self.model} (Gaming) with {self.get_storage()}GB storage and {self.gpu} GPU"


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, "Adreno 730")

print(phone1.phone_info())       # Samsung Galaxy S22 with 128GB storage
print(gaming_phone.phone_info()) # Asus ROG Phone 6 (Gaming) with 256GB storage and Adreno 730 GPU
