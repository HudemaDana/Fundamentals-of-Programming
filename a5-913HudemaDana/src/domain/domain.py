class Complex:

    def __init__(self, real, imaginary):
        self._real = real
        self._im = imaginary
        self._pair = [real, imaginary]

    def get_real(self):
        return self._real

    def get_im(self):
        return self._im

    def set_pair(self, list):
        list.append(self._pair)
