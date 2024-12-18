# asyncio is a library to write concurrent code using the async/await syntax.
import asyncio
import time

"""
An async function is a function declared with the async keyword. It is used to define a coroutine, 
which is a special type of function that can pause its execution and yield control back to the event loop, 
allowing other tasks to run concurrently.
"""

"""
Without async/await:: The synchronous approach blocks each function call until it completes. 
    If each function involves waiting (like a sleep), the total execution time is the sum of all waits.
With async/await:: The asynchronous approach allows tasks to run concurrently. The total execution time 
is roughly equal to the longest individual wait time, as tasks can overlap.
"""

class Async_Await:
    async def Async_func(self):
        print("Before Sleep..")
        await asyncio.sleep(2)
        print("After Sleep")
        
    async def say_helo_2sec(self,name):
        print(f"Hello {name}")
        print("Before sleep 2sec")
        await asyncio.sleep(2)
        print("After sleep 2sec")
        print(f"Good By {name}")
    
    async def say_helo_1sec(self,name):
        print(f"Hello {name}")
        print("Before sleep 1sec")
        await asyncio.sleep(1)
        print("After sleep 1sec")
        print(f"Good By {name}")
    

class Multiple_asny_func:
    async def async_func1(self):
        print(f"started at {time.strftime('%X')}")
        print("1 - first Async func-Before sleep 2sec")
        await asyncio.sleep(2)
        print("1 - first Async func-After sleep 2sec")
        
    async def async_func2(self):
        print("2 - second Async func-Before sleep 1sec")
        await asyncio.sleep(1)
        print("2 - second Async func-After sleep 1sec")

    async def async_func3(self):
        print("3 - three Async func-Before sleep 2sec")
        await asyncio.sleep(2)
        print("3 - three Async func-After sleep 2sec")
        print(f"End at {time.strftime('%X')}")

class without_async:
    def func1(self):
        print(f"started at {time.strftime('%X')}")
        print('before sleep 1')
        time.sleep(2)
        print('after sleep 1')
        
    def func2(self):
        print('before sleep 2')
        time.sleep(1)
        print('after sleep 2')
        
    def func3(self):
        print('before sleep 3')
        time.sleep(2)
        print('after sleep 3')
        print(f"End at {time.strftime('%X')}")


class async_gather_method:
    async def fetch_data(self,url):
        print(f"Fetching data from {url}")
        await asyncio.sleep(2)  # Non-blocking sleep
        print(f"Data fetched from {url}")

        

async def main():
    obj = Async_Await()
    
    # asyncio.run(obj.Async_func())
    
    # # witout scheduling the task
    # task3 = obj.say_helo_2sec('Jhon')
    # task4 = obj.say_helo_2sec('Doe')
    
    # # scheduling the task
    # task1 = asyncio.create_task(obj.say_helo_2sec('Jhon'))
    # task2 = asyncio.create_task(obj.say_helo_2sec('Doe'))
    
    # # asyncio.ensure_future() 
    # e_task1 = asyncio.ensure_future(obj.say_helo_2sec('Jhon'))
    # e_task2 = asyncio.ensure_future(obj.say_helo_2sec('Jhon'))
    
    
    # await task3
    # await task4

    # await task1
    # await task2
    
    # await e_task1
    # await e_task2
    

    obj1 = Multiple_asny_func()
    # await obj1.async_func1()
    # await obj1.async_func2()
    # await obj1.async_func3()
    
    # obj1_task1 = asyncio.create_task(obj1.async_func1())
    # obj1_task2 = asyncio.create_task(obj1.async_func2())
    # obj1_task3 = asyncio.create_task(obj1.async_func3())
    
    # await obj1_task1
    # await obj1_task2
    # await obj1_task3
    
    obj2 = without_async()
    # obj2.func1()
    # obj2.func2()
    # obj2.func3()
    

    obj3 = async_gather_method()
    urls = ["http://example.com", "http://example.org", "http://example.net"]
    # Create a list of tasks for concurrent execution
    tasks = [obj3.fetch_data(url) for url in urls]
    # # Run all tasks concurrently
    """
    asyncio.gather() is a convenient way to handle multiple concurrent tasks and collect their 
    results. It simplifies managing multiple coroutines by running them in parallel and waiting 
    for all of them to complete. This is particularly useful in scenarios where you need to 
    perform multiple I/O-bound operations simultaneously and gather their results efficiently.
    """
    await asyncio.gather(*tasks)
    # # (* is like args)
asyncio.run(main())