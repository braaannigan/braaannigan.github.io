---
layout: post
title:  "Fast looping with Numba"
date:   2017-11-25 16:35:24 +0200
categories: numerics
---
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Fast looping in python with Numba
tl;dr Just-In-Time compilers can give significant speed-ups over vectorised calculations, but you should be aware of potential pitfalls with this rapidly developing technology.

## Thou shalt not loop in python, most of the time
One of the most useful things you can learn as you begin as a
scientific programmer in python
is to avoid writing loops to perform calculations.  These loops are known to
be **so much slower** than equivalent *vectorised* calculations.  For example,
compare this simple sum of two matrices as a loop versus a vectorised
operation using the + operator.

First we define two input arrays:
```python
import numpy as np
data = np.random.rand(1000000)
data2 = np.random.rand(1000000)
```
We can define a looping function as:
```python
def loop_sum( data, data2 ):
    sum_array = np.empty_like( data )
    for idx in np.arange( len( data ) ):
        sum_array[idx] = data[idx] + data2[idx]
    return sum_array
```
while a vectorised addition function would be:
```python
def vectorised_sum( data, data2 ):
    return data + data2
```
To run the loop it takes:
```python
%timeit loop_sum( data, data2 )
348 ms ± 3.21 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
while the vectorised function takes:
```python
%timeit vectorised_sum( data, data2 )
1.11 ms ± 51.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
In this case the vectorised calculation is about 300 times faster.

The reason for this faster performance [has been explained before:](http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)
python needs to do a lot less type checking when working with arrays rather than individual values. In addition, the data in an array is always stored in a contiguous block in memory, whereas the underlying data in other structures such as lists might be scatted around the memory.

## Is there a role for looping then?
One problem with this focus on vectorised operations is that when the calculation is complicated, it is often easier to write loops than the equivalent
vectorised operation.  Indeed, when I'm figuring out a calculation on
a grid, I often work it out on paper in a loop format and then have to
convert this loop to a vectorised operation.  This extra step can be a problem, as
doing the vectorisation often gives me a headache when figuring out
edge cases such as dealing with coastlines in numerical models.

One way to stick with the looping option, is to use the
[Numba](http://Numba.pydata.org) package. You then write your loop
function as before, but this time add the *decorator* ```@jit``` to the start of your function:
```python
from Numba import jit

@jit
def numba_loop_sum( data, data2 ):
    sum_array = np.empty_like( data )
    for idx in np.arange( len( data ) ):
        sum_array[idx] = data[idx] + data2[idx]
    return sum_array
```
By adding ```@jit``` as a decorator your function
is transformed into a "Just-In-Time" function that is compiled
into fast machine code when you call the function. We can compare the performance of this operation with Numba to the vectorised function:
```python
%timeit numba_loop_sum( data, data2 )
3.42 ms ± 20.2 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
and we see that it is about 3 times slower than the
vectorised calculation.

## But wasn't that slower than the vectorised calculation?
Ok, so the vectorised calculation was a lot faster in that case, so it may be worth the extra work to do the vectorisation.  However, let's compare a more complicated case that is more similar to the problem I was working on this week.

The vectorised version is here:
```python
def complicated_vectorised_calc( data, data2 ):
    total = (data**2 * data2**2)**0.5 + data**3 + data2**4
    return total
```
while the corresponding Numba loop is here:
```python
@jit
def Numba_loop_calc( data, data2 ):
    total = np.empty_like( data )
    for idx in np.arange( len( data ) ):
        total[idx] = (data[idx]**2 * data2[idx]**2)**0.5 + data[idx]**3 + data2[idx]**4
    return total
```
We can compare the performance and find that for the vectorised calculation it takes about 122 ms per calculation, while the Numba calculation takes 4 ms. So in this case Numba gives a speed up of 30 times.

## What's going on with that?
A major selling point of NumPy is that it compiles and carries out your calculations in C. As such, you might expect it to offer similar performance to a compiled function decorated with ```@jit```, rather than being 30 times slower.  

The reason for this slowdown, is that NumPy may not be doing exactly when you think it is doing in the compiled layer.  For the complicated calculation, you might guess than NumPy is doing something like the loop in ```Numba_loop_calc``` with all the type declarations and so on that you would expect in C.

However, NumPy is actually doing a series of sub-loops for each operation that makes up the overall loop and this introduces extra computational overhead.  NumPy also needs to create at least one temporary array to hold the output of the sub-loops that have already been carried out, and so NumPy requires more memory and more calls to memory.  This is all explained by Nathaniel Smith (a person who knows a lot more about NumPy than I do!) in the video below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/fowHwlpGb34?rel=0" frameborder="0" allowfullscreen></iframe>

What all this means is that as your calculation becomes more complicated, the attraction of writing a loop decorated with ```@jit``` increases. This is particularly the case if the creation of temporary arrays means that your calculation is causing memory errors.

## Great, so there's no downsides.
Unfortunately, there is a catch.  The main one is that the automatic compilation built into Numba is very complicated, so for most users it's not going to be very clear what is happening or whether something is silently going wrong.  If you do use Numba, then it might be a good time to [write a test function](http://swcarpentry.github.io/python-novice-inflammation/08-defensive/) to make sure your output is what you expect.

A further issue is that the tech in automatic compilation is still rapidly maturing.  It would be reasonable to expect Numba to continue evolving over the coming years.  This can mean that the API changes or even that changes to the underlying algorithm mean the output you get changes.

The output of the NumPy function and the Numba function also differ for some values in the output arrays on my machine.  These differences are small (order 1e-16), but nonetheless exist.

## So, where are we headed?
The rapid development in Just-In-Time compilation has raised an interesting question discussed by Nathaniel Smith in the above video: should NumPy be developed to take advantage of this capability?

The problem is that the JIT compilers can't see down to the C library in NumPy. Instead, Numab works with NumPy because the developers of Numba have gone through each of the NumPy functions that they support and developed compiled code for the functions.  This isn't a long-term solution for many reasons.  For example, every time the underlying NumPy function changes, someone will have to make sure Numba is changed accordingly.  It also means you'd have to start from scratch if you want to start using a different kernel such as PyTorch or TensorFlow.

In the meantime, it's good to be aware of the strengths and weaknesses of JIT compilers for optimising your code.
