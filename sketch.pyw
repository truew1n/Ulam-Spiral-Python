import tkinter as tk
import time

def main():
    root = tk.Tk()
    root.geometry("350x350")
    root.title("Ulam Spiral")
    root.resizable(False, False)
    App(root)
    root.mainloop()


class App:
    def __init__(self, master):
        self.master = master
        self.stepSize = 10
        self.stepCount = 0
        self.stepVal = 1
        self.drawCanvas = tk.Canvas(self.master, bg="black")
        self.drawCanvas.pack(fill=tk.BOTH, expand=True)
        self.drawCanvas.update()
        w, h = self.drawCanvas.winfo_width()//2, self.drawCanvas.winfo_height()//2
        self.start_time = time.time()
        self.ulam_spiral(w, h)
        print("--- %s seconds ---" % (time.time() - self.start_time))

    def ulam_spiral(self, w, h):
        count = 1
        for x in range(1, ((w+h)*2)//self.stepSize):
            if self.stepCount == 2:
                self.stepVal += 1
                self.stepCount = 0
            self.stepCount += 1

            mod = x % 4
            for i in range(1, self.stepVal+1):
                self.master.update()
                self.master.after(1)
                if self.is_prime(count):
                    self.drawCanvas.create_rectangle(w - self.stepSize // 2, h - self.stepSize // 2, w + self.stepSize // 2, h + self.stepSize // 2, fill="green", outline="")
                if mod == 1:
                    w += self.stepSize
                if mod == 2:
                    h -= self.stepSize
                if mod % 4 == 3:
                    w -= self.stepSize
                if mod % 4 == 0:
                    h += self.stepSize
                count += 1

    @staticmethod
    def is_prime(num):
        p = 2
        primes = []
        if num < 0 or num == 0 or num == 1:
            return False
        else:
            while num >= p**2:
                if num % p == 0:
                    primes.append(p)
                    num = num / p
                else:
                    p += 1
            primes.append(num)
        return True if len(primes) == 1 else False


if __name__ == "__main__":
    main()
