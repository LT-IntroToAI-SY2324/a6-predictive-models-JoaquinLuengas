# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
I think that the model is less accurate because after commenting out the standardscaler, my values would always stay the same no matter what(Both predicted and actual values). I feel like there should be more car purchaces than there are without the standard scaler.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
I think that the model with the standardscaler is mostly accurate, and is accurate enough for the given use. While the model predicted that not many people could purchace a car based on their salery, age, and gender, there are many that can, either those who are older and have saved a lot of money, ro those that are a bit younger but have a very high salery.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did good but coud have done better. Most of the predicted values were 0, wtih many of the acual values being one and vice versa, leading to many inaccuracies with the actual and predicted values. However, about half of the predicted values lined up with the actual values.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

