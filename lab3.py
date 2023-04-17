import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


class ImageProcessingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")

        # Image variables
        self.image = None
        self.photo_image = None
        self.original_image = None
        self.image_width = 800
        self.image_height = 600

        # Create GUI elements
        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_image)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)

        self.image_canvas = tk.Canvas(self.master, width=self.image_width, height=self.image_height)
        self.image_canvas.pack(side=tk.TOP, expand=1)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side=tk.BOTTOM)
        self.reset_button = tk.Button(self.button_frame, text="Reset Image", command=self.reset_image)
        self.reset_button.pack(side=tk.LEFT)
        self.select_image_button = tk.Button(self.button_frame, text="Выбрать изображение",
                                             command=self.open_file_dialog)
        self.select_image_button.pack()

        self.gray_button = tk.Button(self.button_frame, text="Convert to Gray", command=self.convert_to_gray)
        self.gray_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.button_frame, text="Save Image", command=self.save_image)
        self.save_button.pack(side=tk.RIGHT)
        # Affine transformation buttons
        self.affine_frame = tk.Frame(self.master)
        self.affine_frame.pack(side=tk.BOTTOM)

        self.move_button = tk.Button(self.affine_frame, text="Переместить", command=self.move_image)
        self.move_button.pack(side=tk.LEFT)

        self.scale_button = tk.Button(self.affine_frame, text="Масштабировать", command=self.scale_image)
        self.scale_button.pack(side=tk.LEFT)

        self.rotate_button = tk.Button(self.affine_frame, text="Повернуть", command=self.rotate_image)
        self.rotate_button.pack(side=tk.LEFT)

        self.shift_button = tk.Button(self.affine_frame, text="Сдвинуть", command=self.shift_image)
        self.shift_button.pack(side=tk.LEFT)

        self.channel_buttons = []
        for channel in ["Red", "Green", "Blue"]:
            button = tk.Button(self.button_frame, text=f"Show {channel} Channel",
                               command=lambda ch=channel: self.show_channel(ch))
            self.channel_buttons.append(button)
            button.pack(side=tk.LEFT)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.original_image = self.image.copy()
            self.display_image(self.image)

    def reset_image(self):
        if self.image:
            self.display_image(self.original_image)
            self.image = self.original_image

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.original_image = self.image.copy()
            self.display_image(self.image)

    def display_image(self, image, x=None, y=None):
        # image = image.resize((self.image_width, self.image_height), resample=Image.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(image)
        if x and y:
            self.image_canvas.create_image(x, y, image=self.photo_image, anchor=tk.NW)
        else:
            self.image_canvas.create_image(0, 0, image=self.photo_image, anchor=tk.NW)

    def convert_to_gray(self):
        if self.image:
            self.image = self.image.convert("L")
            self.display_image(self.image)

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.image.save(file_path)

    def show_channel(self, channel):
        if self.image.mode == "RGB":
            r, g, b = self.image.split()
            if channel == "Red":
                channel_image = Image.merge("RGB",
                                            (r, Image.new("L", self.image.size, 0), Image.new("L", self.image.size, 0)))
            elif channel == "Green":
                channel_image = Image.merge("RGB",
                                            (Image.new("L", self.image.size, 0), g, Image.new("L", self.image.size, 0)))
            elif channel == "Blue":
                channel_image = Image.merge("RGB",
                                            (Image.new("L", self.image.size, 0), Image.new("L", self.image.size, 0), b))
        else:
            channel_image = self.image.copy()
            print(self.image.mode)
        self.display_image(channel_image)

    def move_image(self):
        # Get user input for move distance
        x_offset = int(input("Введите смещение по x: "))
        y_offset = int(input("Введите смещение по y: "))

        # Perform affine transformation
        if self.image:
            # self.image = self.image.transform(self.image.size, Image.AFFINE, (1, 0, x_offset, 0, 1, y_offset))
            self.display_image(self.image, x_offset, y_offset)

            # Add horizontal scrollbar
            if not hasattr(self, "xscrollbar"):
                self.xscrollbar = tk.Scrollbar(self.master, orient=tk.HORIZONTAL)
                self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

            self.image_canvas.config(xscrollcommand=self.xscrollbar.set)
            self.xscrollbar.config(command=self.image_canvas.xview)

            # Add vertical scrollbar
            if not hasattr(self, "yscrollbar"):
                self.yscrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL)
                self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.image_canvas.config(yscrollcommand=self.yscrollbar.set)
            self.yscrollbar.config(command=self.image_canvas.yview)

    def scale_image(self):
        # Get user input for scale factor
        scale_factor = float(input("Введите коэффициент масштабирования: "))

        # Perform affine transformation
        if self.image:
            new_size = (int(self.image.size[0] * scale_factor), int(self.image.size[1] * scale_factor))
            self.image = self.image.resize(new_size)
            self.display_image(self.image)

    def rotate_image(self):
        # Get user input for rotation angle
        angle = float(input("Введите угол поворота (в градусах): "))

        # Perform affine transformation
        if self.image:
            self.image = self.image.rotate(angle, expand=True)
            self.display_image(self.image)

    def shift_image(self):
        # Get user input for shift distance
        x_offset = int(input("Введите смещение по x: "))
        y_offset = int(input("Введите смещение по y: "))

        # Perform affine transformation
        if self.image:
            self.image = self.image.resize((self.image_width + x_offset, self.image_height + y_offset), resample=Image.LANCZOS)
            self.display_image(self.image)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
