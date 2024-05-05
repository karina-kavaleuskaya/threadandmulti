import multiprocessing
import time
import requests

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        pname = self.name

        while True:
            temp_task = self.task_queue.get()
            if temp_task is None:
                self.task_queue.task_done()
                break

            print('%s processing task: %s' % (pname, temp_task))

            answer = temp_task.search(pname, temp_task.x)
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task():
    def __init__(self, x):
        self.x = x

    def search(self, name, value):
        time.sleep(0.1)
        time_before = time.perf_counter()
        result = requests.get(value)
        time_after = time.perf_counter() - time_before
        return f"Result for {name} is {result} in {time_after}"

    def __str__(self):
        return 'Checking if %s is a prime or not.' % self.x


if __name__ == '__main__':
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    n_consumers = multiprocessing.cpu_count()
    print('Spawning %i consumers...' % n_consumers)
    consumers = [Consumer(tasks, results) for _ in range(n_consumers)]
    for consumer in consumers:
        consumer.start()

    # Enqueueing jobs
    my_input = ['https://www.google.com/', 'https://www.yandex.ru/', 'https://www.youtube.com/']
    for item in my_input:
        tasks.put(Task(item))

    # Adding poison pills to signal the consumers to exit
    for _ in range(n_consumers):
        tasks.put(None)

    tasks.join()

    while not results.empty():
        temp_result = results.get()
        print('Result:', temp_result)

    print('Done.')