# def myrange(n):
#     num = 0
#     while num < n:
#         yield num
#         num -= 1







# In [35]: def finder(s): 
#     ...:     while True: 
#     ...:         input_text = yield 
#     ...:         if s in input_text: 
#     ...:             print(input_text) 
#     ...:                                                                                                                                              

# In [36]: finder('a')                                                                                                                                  
# Out[36]: <generator object finder at 0x7f8503373510>

# In [37]: f = finder('python')                                                                                                                         

# In [38]: f                                                                                                                                            
# Out[38]: <generator object finder at 0x7f8503d30b30>

# In [39]: f.send('some text including python')                                                                                                         
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-39-08643d723d98> in <module>
# ----> 1 f.send('some text including python')

# TypeError: can't send non-None value to a just-started generator

# In [40]: f.send(None)                                                                                                                                 

# In [41]: f.send('some text including python')                                                                                                         
# some text including python

# In [42]:  

# In [42]: f.send('not that eork including')                                                                                                            

# In [44]: f.close()                                                                                                                                    





# In [45]: f.throw(NameError, 'gholiiiiii')
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-45-ebc99aa2ed58> in <module>
# ----> 1 f.throw(NameError, 'gholiiiiii')

# NameError: gholiiiiii







# In [49]: def sayhi(name): 
#     ...:     return 'Hello ' + name 
#     ...:                                                                                                                                              

# In [50]: async def _sayhi(name): 
#     ...:     return 'Hello ' + name 
#     ...:                                                                                                                                              

# In [51]: sayhi('gholi')                                                                                                                               
# Out[51]: 'Hello gholi'

# In [52]: _sayhi('gholi')                                                                                                                              
# Out[52]: <coroutine object _sayhi at 0x7f850352e640>










# In [53]: g = _sayhi('gholi ghanem')                                                                                                                   

# In [54]: g                                                                                                                                            
# Out[54]: <coroutine object _sayhi at 0x7f85034b7240>

# In [55]: g.send(None)                                                                                                                                 
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-55-70a3cd01dee6> in <module>
# ----> 1 g.send(None)

# StopIteration: Hello gholi ghanem







# In [56]: def run(coroutine): 
#     ...:     try: 
#     ...:         coroutine.send(None) 
#     ...:     except StopIteration as e: 
#     ...:         return e.value 
#     ...:                                                                                                                                              

# In [57]: run(_sayhi('gholi'))                                                                                                                         
# Out[57]: 'Hello gholi'









# In [58]: async def main():
#     ...:     print(await _sayhi('gholi'))
#     ...:

# In [59]: run(main())
# Hello gholi





# In [60]: async def main(): 
#     ...:     names = ['gholi', 'ghasem', 'ahmad'] 
#     ...:     for name in names: 
#     ...:         print(await _sayhi(name)) 
#     ...:                                                                                                                                              

# In [61]: run(main())                                                                                                                                  
# Hello gholi
# Hello ghasem
# Hello ahmad










# In [62]: # where can you out await?                                                                                                                   

# In [63]: async def fib(n): 
#     ...:     if n < 2: 
#     ...:         return 1 
#     ...:     else: 
#     ...:         return await fib(n-1) + await fib(n-2) 
#     ...:                                                                                                                                              

# In [64]: async def main(): 
#     ...:     for n in range(30): 
#     ...:         print(await fib(n)) 
#     ...:                                                                                                                                              

# In [65]: run(main())                                                                                                                                  
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# 1597
# 2584
# 4181
# 6765
# 10946
# 17711
# 28657
# 46368
# 75025
# 121393
# 196418
# 317811
# 514229
# 832040













# In [66]: async def main(): 
#     ...:         print(fib(15)) 
#     ...:          
#     ...:                                                                                                                                              

# In [67]: main()                                                                                                                                       
# Out[67]: <coroutine object main at 0x7f85036aee40>

# In [68]: run(main())                                                                                                                                  
# <coroutine object fib at 0x7f85036f3040>
# <ipython-input-66-29fab1d86084>:2: RuntimeWarning: coroutine 'fib' was never awaited
#   print(fib(15))
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback










# In [69]: async def main(): 
#     ...:         print(await fib(15)) 
#     ...:                                                                                                                                              

# In [70]: run(main())                                                                                                                                  
# 987









# In [72]: async def okay(): 
#     ...:     f = await fib(10) 
#     ...:     d = {} 
#     ...:     d[await fib(6)] = await fib(2) 
#     ...:     x = await fib(3) - await fib (1) 
#     ...:     print(f, d, x) 
#     ...:                                                                                                                                              

# In [73]: run(okay())                                                                                                                                  
# 89 {13: 2} 2









# In [75]: await fib(10)
# Out[75]: 89








# In [76]: def synchronous(x): 
#     ...:     await fib(x)                                                                                                                             
#   File "<ipython-input-76-0e07101fd00b>", line 2
#     await fib(x)
#     ^
# SyntaxError: 'await' outside async function









# In [79]: def synchronous(): 
#     ...:     return 'string' 
#     ...:                                                                                                                                              

# In [80]: await synchronous()                                                                                                                          
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-80-880eb9444117> in <module>
# ----> 1 await synchronous()

# TypeError: object str can't be used in 'await' expression



# ASYNCOI ===================================================================
import time

def count():
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')

def main():
    for i in range(3):
        count()

if __name__ == '__main__':
    t = time.perf_counter()
    main()
    t2 = time.perf_counter() - t
    print(f'Total time splited: {t2:0.2f} seconds')

# out put:
1
2
3
1
2
3
1
2
3
# Total time splited: 9.00 seconds

# NEXT ONE
# ONE PROCCESS ONE thread
import asyncio


async def count():
    await asyncio.sleep(1)
    print('1')
    await asyncio.sleep(1)
    print('2')
    await asyncio.sleep(1)
    print('3')

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
    asyncio.run(main())
# OUTPUT
1
1
1
2
2
2
3
3
3
# 3 seconds
# as soon as it arrives in the `await asyncio.sleep(1)` python was free to do  ather work.
# ===============
loop = asyncio.get_event_loop()

async def sayhi(name):
    print('Hi', name, 'you are in coroutine.')

# asyncio.run(sayhi('LP'))

try:
    print('starting coroutine')
    coro = sayhi('LP')
    print('entering event loop')
    loop.run_until_complete(coro)
finally:
    print('closing event loop')
    loop.close()


# ====================
async def outer():
    print('in outher')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return result1, result2

async def phase1():
    print('in phase1')
    return 'phase1 result'

async def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)

asyncio.run(outer())
