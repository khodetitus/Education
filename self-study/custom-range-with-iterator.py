class CustomRange:
    def __init__(self, stop, start=0, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        if isinstance(value, int):
            self._start = value
        else:
            raise TypeError

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, value):
        if isinstance(value, int):
            self._stop = value
        else:
            raise TypeError

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        if isinstance(value, int):
            self._step = value
        else:
            raise TypeError

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            if self.step > 0:
                number = self.start
                self.start += self.step
                return number
            elif self.start > self.stop:
                pass
        elif self.step < 0:
            if self.start > self.stop:
                number = self.start
                self.start += self.step
                return number
            elif self.start < self.stop:
                pass

        elif self.step == 0:
            raise ValueError
        raise StopIteration


my_custom_range = CustomRange(10, 30)
for num in my_custom_range:
    print(num)
