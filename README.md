In our project, we've utilized the DWD Weather Data East Germany API to access accurate and up-to-date meteorological data from the eastern region of Germany. 
This API offers detailed information on weather conditions such as temperature, precipitation, wind speed, and more. 
By integrating this API into our project, we were able to obtain reliable data to enhance the accuracy and functionality of our applications or analyses related to weather in this specific area.

Observations:
From the entire dataset, we will only need a few variables from 2021, as the dataset you provided us with was from 2021 and it would make sense to use that.

When analyzing the 2021 data, we observe that we have few variables with values. Therefore, we will use those that make the most sense for our study. In our case, we will use 'sunshine' and 'precipitation'.
The entire process to obtain meaningful data is explained in the code (Data4Good_1.ipynb).

On the other hand, (Dataprepatation.ipynb) we merged datasets, removed uninteresting variables, and focused on a subset of the input data. In Particular, we analyzed accidents that occurred near the sensors in Berlin.
Once we merge all the CSV files, we can start analyzing them. On one hand, we've developed a Deep Learning model where we employ an MLP to predict accident probabilities. We're using the sigmoid activation function since we're interested in values between 0 and 1.

To build this neural network, we encountered many dimensionality issues. Typically, inputs have the same dimensions, but in our case, they do not. Therefore, we had to follow a logic to generate meaningful dimensions that do not affect the final value. 
To train the data, we need to perform forward and backpropagation, where we then calculate the loss function. We've used Binary Cross Entropy to classify the labels in a binary manner. However, we've used PyTorch, which is a Python library that helps us perform calculations very efficiently and internally computes backpropagation, so we don't have to worry about it. This makes it very useful as neural networks start to increase in complexity.

Once we have all the probabilities (predicted values by Neural Net), we can create various applications. In our case, we have developed a Python script that takes the accident probabilities. 
These probabilities are linked to the coordinates of Berlin with latitude and longitude, so we can relate them to the distance to accident sensors. With this, we can establish a relationship between accident intensity and frequency and create a heatmap.

Thanks to an API, we've created an interactive graphical interface that allows zooming to view areas with a higher probability of accidents at that moment.
With this, we'll be able to redirect people/drivers when there's a certain risk of accidents.

To be usable in real life, what we have done is create an architecture to make it a real-time system, meaning that data is sent periodically to be executed automatically. This ensures that citizens have up-to-date data and allows us to redirect traffic to reduce the likelihood of accidents. To do this, the structure is based on three sources of information: Police, Sensors, Weather. This is sent to a Kafka Data Broker which will send it to a node to execute Python scripts, the output will go to another Data Broker which will send the result that will be the input for the deep learning model, then this would be sent to another Kafka Data broker, which will send the data to another Python script to create a heatmap of accident probabilities in Berlin which will serve to improve the life of people in Berlin.

Finally, we can see that this system allows us to make it scalable to large scales.

