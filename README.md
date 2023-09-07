### Project goals
- try to create a different model for each county
- Find the key drivers of property value for single family properties. 


### Project description

- I've been asked to come up with a new model for determining tax value using features created by me for single family properties. This use a dataframe from Zillow in 2017. 

### Project planning (lay out your process through the data science pipeline)

### Initial hypotheses

- Split into different counties since location could be a big factor in home value
- Finished sqft and amount of bedrooms will make a difference in price
- Look into bathrooms as well

### Acquire: 
- Acquire the data from SQL 
- You will need to use the properties_2017, predictions_2017, and propertylandusetype tables.

### Explore: 
- Why do some properties have a much higher value than others when they are located so close to each other?
- Why are some properties valued so differently from others when they have nearly the same physical attributes but only differ in location?
- Is having 1 bathroom worse for property value than having 2 bedrooms?

### Modeling: 
- Use drivers in explore to build predictive models of different types
- Evaluate models on train and validate data
- Select the berst model based on accuracy
- Evaluate the test data


### Data dictionary:
- Make table for Features used

### How to Reproduce
- Clone this repo
- Acuire dazta from MySql (Should make a zillow.csv after)
- Run Notebook

### Key findings 

### Takeaways and Conclusions

### Recommendations