import asyncio


async def worker_one(queue: asyncio.Queue):
    print("HERE_____________HEREREEEEEE")
    result = await queue.get()
    await asyncio.sleep(3)
    print("Worker: 1")
    print(result())
    queue.task_done()


async def worker_two(queue: asyncio.Queue):
    result = await queue.get()
    await asyncio.sleep(1)
    print("Worker: 2")
    print(result())
    queue.task_done()


async def worker_three(queue: asyncio.Queue):
    result = await queue.get()
    await asyncio.sleep(1)
    print("Worker: 3")
    print(result())
    queue.task_done()


async def Queue():

    # ----- Queue ------
    queue = asyncio.Queue()

    def test_fnc_one():
        print("HERE_____________Zzzzzzz")
        return f"1 ------>>>> "

    def test_fnc_two():
        return f"2 ------>>>> "

    def test_fnc_three():
        return f"3 ------>>>> "

    def test_fnc_four():
        return f"4 ------>>>> "

    queue.put_nowait(test_fnc_one)
    queue.put_nowait(test_fnc_two)
    queue.put_nowait(test_fnc_three)
    queue.put_nowait(test_fnc_four)

    # --- worker tasks to process the queue concurrently
    # TODO Producer here ------>
    print("HERE_____________1")
    task_one = asyncio.create_task(worker_one(queue))
    task_two = asyncio.create_task(worker_two(queue))
    task_three = asyncio.create_task(worker_three(queue))
    task_four = asyncio.create_task(worker_two(queue))

    # wait until queue is fully processed
    # TODO Consumer here ---->
    print("HERE_____________2")
    await queue.join()
    print("HERE_____________END")

    # Cancel all worker tasks.
    task_one.cancel()
    task_two.cancel()
    task_three.cancel()
    task_four.cancel()

    # wait until all worker tasks are cancelled
    await asyncio.gather(task_one, task_two, task_three)
    print("QUEUE COMPLETE")

asyncio.run(Queue(), debug=True)