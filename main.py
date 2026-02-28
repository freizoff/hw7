import time
def time_meas(func):
    start = time.time()
    result   = func()
    end = time.time()
    return result, end - start

def function_slow():
    time.sleep(1)
    return "Task completed"

result, work_time = time_meas(function_slow)

assert result == "Done"
assert work_time >= 1

print("Result:", result)
print("Work time:", work_time)
print("Success!")
