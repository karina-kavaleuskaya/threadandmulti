import threading
import time

class Order:
    def __init__(self, resources, processing_time):
        self.resources = resources
        self.processing_time = processing_time

class Worker(threading.Thread):
    def __init__(self, name, resource_manager):
        threading.Thread.__init__(self)
        self.name = name
        self.resource_manager = resource_manager

    def run(self):
        while True:
            order = self.resource_manager.get_order()
            if order is None:
                break

            print(f'{self.name} starts processing order')

            try:
                time.sleep(order.processing_time)
            except Exception as e:
                print(f'An error occurred while sleeping: {str(e)}')

            print(f'{self.name} finishes processing order')

            self.resource_manager.complete_order()

class ResourceManager:
    def __init__(self, orders):
        self.orders = orders
        self.lock = threading.Lock()
        self.completed_orders = 0
        self.total_orders = len(orders)

    def get_order(self):
        self.lock.acquire()

        if self.completed_orders >= self.total_orders:
            self.lock.release()
            return None

        order = self.orders[self.completed_orders]
        self.completed_orders += 1

        self.lock.release()
        return order

    def complete_order(self):
        self.lock.acquire()

        self.completed_orders += 1

        self.lock.release()

class OrderProcessor:
    def __init__(self, orders, num_workers):
        self.orders = orders
        self.resource_manager = ResourceManager(orders)
        self.workers = []
        for i in range(num_workers):
            worker = Worker(f'Worker-{i+1}', self.resource_manager)
            self.workers.append(worker)

    def process_orders(self):
        try:
            for worker in self.workers:
                worker.start()

            for worker in self.workers:
                worker.join()
        except Exception as e:
            print(f'An error occurred: {str(e)}')

        print('All orders processed.')

orders = [
    Order(['Resource 1', 'Resource 2'], 2),
    Order(['Resource 2', 'Resource 3'], 3),
    Order(['Resource 3', 'Resource 4'], 1),
    Order(['Resource 1', 'Resource 4'], 2)
]

order_processor = OrderProcessor(orders, 2)
order_processor.process_orders()