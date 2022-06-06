---
layout: post
title:  "Testing for data science 3: testing with Pandas"
date:   2022-06-07 12:35:24 +0200
categories: software
---
# Unit testing example - mixed layer depth
The chart shows a temperature profile measured by an ARGO float in the North Atlantic in May 2010. 
The profile has a region of relative uniform temperature near the surface known as the mixed layer. We want a function
that will find the depth of the bottom of this layer.

We define the mixed layer depth as the first depth where the temperature is 0.1 degrees colder than the near-surface temperature. We define the near-surface temperature as the average of the top 2 measurements.

### Define our first function for 1D data 
We define our first function. This function takes a 1D array of temperature values and a float to set the temperature
difference threshold. It does a simple loop through the profile until it finds the first index where the temperature difference threshold is passed.
```python
def findMixedLayerIndex(temperature:np.ndarray,thresholdTemperatureDifference:float):
    surfaceTemps = temperature[:2].mean()
    depthIndex = 2
    temperatureDifference = surfaceTemps - temperature[depthIndex]
    while temperatureDifference < thresholdTemperatureDifference:
        depthIndex += 1
        temperatureDifference = surfaceTemps - temperature[depthIndex]
    return depthIndex
```

We now want to test this function with some data. We'll define the temperature array manually.
```python
temperature = np.array([5.0,5.0,4.95,4.89,4.85])
targetDepthIndex = 3
output = mixedLayerIndex(temperature=temperature,thresholdTemperatureDifference=0.1)
assert output == targetDepthIndex,f"output:{output},targetDepthIndex:{targetDepthIndex}"
```
Great - that worked!

We used python's `assert` statement here to test if the output was correct. This is fine when we have scalar values or text, but doesn't cover some scientific use-cases for example:
- if the output is an array as this will be slow
- if we're interested in similarity within a tolerance

### Define our second function for 2D data 

Instead we use Numpy's built-in testing module through `np.testing`. We demonstrate this here by modifying our mixed layer depth index function to work with 2D arrays instead of 1D arrays.

```python
def mixedLayerIndexArray(temperature:np.ndarray,thresholdTemperatureDifference:float):
    surfaceTemps = temperature[:2].mean(axis=0)
    depthIndexList = []
    for col in range(temperature.shape[1]):
        depthIndex = 2
        temperatureDifference = surfaceTemps[col] - temperature[depthIndex,col]
        while (temperatureDifference < thresholdTemperatureDifference) and (depthIndex < temperature.shape[0]-1):
            depthIndex += 1
            temperatureDifference = surfaceTemps[col] - temperature[depthIndex,col]
        depthIndexList.append(depthIndex)
    depthIndexArray = np.array(depthIndexList)
    return depthIndexArray
```

```python
temperature = np.array([
    [5.0,5.0,4.95,4.89,4.85],
    [5.0,5.0,4.95,4.94,4.93]
]).T
print(f"Shape of temperature array: {temperature.shape}")
assert temperature.shape[1] == 2
targetDepthIndexArray = np.array([3,4])
output = mixedLayerIndexArray(temperature=temperature,thresholdTemperatureDifference=0.1)
np.testing.assert_array_equal(output,targetDepthIndexArray)
```

Numpy's testing module also allows you to test whether 2 arrays 
are almost equal within a specified tolerance with `np.testing.assert_array_almost_equal`.

### Testing with dataframes
Testing with dataframes is similar to testing with `numpy`. Pandas comes with its own testing module 
at `pd.testing`.



```python
def mixedLayerIndexDataframe(temperatureDf:pd.DataFrame,thresholdTemperatureDifference:float):
    surfaceTemps = temperatureDf.iloc[:2].mean(axis=0)
    depthIndexList = []
    baseMixedLayerTemperature = []
    for col in temperatureDf.columns:
        depthIndex = 2
        temperatureDifference = surfaceTemps.iloc[col] - temperatureDf.iloc[depthIndex].loc[col]
        while (temperatureDifference < thresholdTemperatureDifference) and (depthIndex < temperature.shape[0]-1):
            depthIndex += 1
            temperatureDifference = surfaceTemps.iloc[col] - temperatureDf.iloc[depthIndex].loc[col]
        depthIndexList.append(depthIndex)
        baseMixedLayerTemperature.append(temperatureDf.iloc[depthIndex].loc[col])

    mixedLayerDf = pd.DataFrame({'depthIndex': depthIndexList,'mlTemp':baseMixedLayerTemperature})
    return mixedLayerDf
```

## Testing principles
The basic principles for all software testing are: Arrange, Act, Assert
  * Arrange: Set things up for the test e.g. load some data
  * Act: Carry out the action you want to test e.g. pass the data to a function
  * Assert: check that the output of the function meets your expectations

- What can you test:
  * Does the function return something?
  * Does it return the right type of object?
  * Does the returned object have the right characteristics e.g. right number of dimensions?
  * Does the returned object make sense e.g. temperature values are in a reasonable range?
  * And so on...

## Unit testing in practice
In practice you need an automated testing framework to:
- set-up a python interpreter
- find the tests in your code directories
- run all the tests and report on the results

I highly recommend the third-party `pytest` package rather than the built-in `unit test` module:
- the syntax for naming tests with pytest is intuitive
- pytest comes with lots of handy third-party extensions to e.g. caclulate test coverage or run tests in parallel
- pytest has more advanced features such as looping through a range of data combinations with parameterised tests or setting up the same data for multiple tests with fixtures

To date I have only used the built-in `unit test` module for certain functionality e.g. for testing if a test will return an exception.


# Test datasets


- Always work with the smallest possible test datasets
- Create the test datasets right at the outset of your project
- Make it very easy to switch between different test datasets and the full dataset
- Have test datasets of multiple sizes
  * Can show if a new issue arises when dataset gets larger
  * Can estimate how long running the full dataset will take
- Never run on the full dataset unless you run on the test dataset first

# What goes in the test dataset?
- Should have the minimum number of data points to get the output you want
- Examples:
  * For a multi-year time series then the test dataset should have data points from at least 2 years
  * For spatial trends have multiple grid points
- If parts of the dataset have special cases include these as additional test datasets
  * Example: analysing ocean model output then have an open ocean test dataset and a coastal test dataset

# Further reading
[Blog post on why we write tests for data analysis and some strategies for what to test](https://www.peterbaumgartner.com/blog/testing-for-data-science/){:target="_blank"}

[Unit testing principles](https://stackify.com/unit-testing-basics-best-practices/){:target="_blank"}

[Intro to unit testing for data science video](https://www.youtube.com/watch?v=Da-FL_1i6ps){:target="_blank"}
