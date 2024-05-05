import queue
import threading
import time

class StandartCode:
    def math(self):
        value_one = 2
        value_two = 5
        value_three = 7
        my_list = [value_one, value_two, value_three]

        for i in my_list:
            time_before = time.perf_counter()
            value = (((i ** 1856) / (i ** 1668)) * (i ** 95)) / (((i ** 186) / (i ** 168)) * (i ** 9))
            time_after = time.perf_counter() - time_before
            print(f"Result is {value} in {time_after}" )


code = StandartCode()
code.math()


class MyThread(threading.Thread):
    def __init__(self, name, value, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.value = value
        self.delay = delay

    def run(self):
        math(self.name, self.value, self.delay)



def math(name, value, delay):
    time.sleep(delay)
    time_before = time.perf_counter()
    result = (((value ** 1856) / (value ** 1668)) * (value ** 95)) / (((value ** 186) / (value ** 168)) * (value ** 9))
    time_after = time.perf_counter() - time_before
    print(f"Result for {name} is {result} in {time_after}")


def main():
    thread1 = MyThread('A', 2, 0.01)
    thread2 = MyThread('B', 5, 0.02)
    thread3 = MyThread('C', 7, 0.03)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print('Finished.')


if __name__ == "__main__":
    main()




