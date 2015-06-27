from tkinter import *
from tkinter import ttk


class Window(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Fruit Machine")

        self.title("Fruit Machine")
        self.geometry('800x600')

        self.mainframe = ttk.Frame(self)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.pack(expand=True)

        self.canvas = TheCanvas(self.mainframe)

        self.wheel_images = GetImages()
        self.wheel_1 = Wheel(self.canvas, self.wheel_images, 400, 300)


class TheCanvas(Canvas):

    def __init__(self, mainframe):
        Canvas.__init__(self, mainframe)
        self.mainframe = mainframe
        self.canvas = Canvas(self.mainframe, width=800, height=600, bg= 'black')
        self.canvas.pack()

# *******************************************************************


class GetImages(object):

    def __init__(self):

        self.wheel_images = []
        # Creates a list of Number.png formatted as string
        for each in range(1,10):
            self.wheel_images.append("images\\" + str(each) + ".png")

        # Re-creates list with the image in it's place
        for each in range(len(self.wheel_images)):
            self.wheel_images[each] = PhotoImage(file=self.wheel_images[each])

    def __getitem__(self, index):
        return self.wheel_images[index]


class Wheel(object):

    def __init__(self, canvas, wheel_images, x, y):
        self.x = x
        self.y = y
        self.wheel_item = []
        self.count = 0
        self.wheel_images = wheel_images
        self.canvas = canvas
        for i in range(8):
            self.wheel_item.append(self.canvas.create_image(self.x, self.y, image=self.wheel_images[i]))

    def __getitem__(self, index):
        return self.wheel_item[index]

    def wheel_time(self):
        self.canvas.after(10, self.wheel_count)

    def wheel_count(self):

        self.canvas.lower(self.wheel_item[self.count])
        if self.count == 7:
            self.count = 0
        else:
            self.count += 1
        self.canvas.update()
        self.wheel_time()



# *********************************************************************


root = Window()
root.mainloop()
