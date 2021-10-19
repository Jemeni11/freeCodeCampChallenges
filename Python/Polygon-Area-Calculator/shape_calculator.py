class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = int(width)
        self.height = int(height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width) -> None:
        self.width = int(new_width)

    def set_height(self, new_height) -> None:
        self.height = int(new_height)

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> int:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(0, self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, rect):
        return (self.width // rect.width) * (self.height // rect.height)



class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, new_side) -> None:
        self.height = new_side
        self.width = new_side
    
    def set_width(self, new_width) -> None:
        self.set_side(new_width)

    def set_height(self, new_height) -> None:
        self.set_side(new_height)
