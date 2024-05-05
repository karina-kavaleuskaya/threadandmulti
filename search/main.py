import requests
import time
import threading


class StandartCode:
    def search(self):
        data_one = 'https://www.google.com/'
        data_two = 'https://www.yandex.ru/'
        data_three = 'https://www.youtube.com/'
        my_list = [data_one, data_two, data_three]
        for i in my_list:
            time_before = time.perf_counter()
            requests.get(i)
            time_after = time.perf_counter() - time_before
            print(f'Get request {i} for {time_after}')


class MyThread(threading.Thread):
    def __init__(self, name, value, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.value = value
        self.delay = delay

    def run(self):
        search(self.name, self.value, self.delay)



def search(name, value, delay):
    time.sleep(delay)
    time_before = time.perf_counter()
    result = requests.get(value)
    time_after = time.perf_counter() - time_before
    print(f"Result for {name} is {result} in {time_after}")


def main():
    thread1 = MyThread('Google', 'https://www.google.com/', 0.01)
    thread2 = MyThread('Yandex', 'https://www.yandex.ru/', 0.02)
    thread3 = MyThread('Youtube', 'https://www.youtube.com/', 0.03)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print('Finished.')


code = StandartCode()
code.search()

if __name__ == "__main__":
    main()