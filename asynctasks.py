import asyncio
import time

# async def say_after(delay, msg):
#     await asyncio.sleep(delay)
#     print(msg)


# async def main():
#     task1 = asyncio.create_task(say_after(1, 'hello'))
#     task2 = asyncio.create_task(say_after(1,'world'))

#     print(f"started at {time.strftime('%X')}")
    
#     await task1
#     await task2

#     print(f"ended at {time.strftime('%X')}")

# Awaitables ==> coroutines, tasks, futures

async def function():
    return '11'

async def factorial(name, n):
    f = 1
    for i in range(2, n+1):
        print(f"Task {name}: computing factorial {n}, currently i={i}...")
        f *= i
        await asyncio.sleep(1)
    print(f"Task {name}: completed: factorial{n} = {f}")
    return f    

async def main():
    #print(function())
    # create task
    #task1 = asyncio.create_task(function())
    #print(await function())
    L = await asyncio.gather(
        factorial('A', 3),
        factorial('B', 5),
        factorial('C', 7),
    )
    print(L)


asyncio.run(main())