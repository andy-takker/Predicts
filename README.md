# Predicts
MGM, GM and other forecasting methods

### GM (1, 1)
The grey system theory, which was founded by professor Deng Julong in the 1980s, has huge and far-reaching effects in the scientific development . The grey system theory takes uncertain system with “small sample and poor information” as the research object, and provides a powerful technical support for forecasting and have been successfully employed in various fields and demonstrated satisfactory results, such as the inverted pendulum control , the stock price forecasting, the semiconductor manufacturing layout, the robot fuzzy control, the robot fuzzy control, the building deformation forecasting. During operation, the GM model first accumulates or differentially processes a random sequence, making it regular: 
![equation](https://latex.codecogs.com/gif.latex?x_%7Bk%7D%5E%7B1%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bk%7Dx_%7Bi%7D%5E%7B0%7D)
After that, a differential equation is established for this regular sequence:
![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%5E%7B1%7D%7D%7Bdt%7D&plus;ax%5E%7B1%7D%3Db)
. Through the solution of the differential equation:
![equation](https://latex.codecogs.com/gif.latex?%5Chat%7Bx%7D_%7Bk&plus;1%7D%5E%7B0%7D%3D%5Cleft%20%28%201-e%5E%7Ba%7D%20%5Cright%20%29%5Cleft%20%28%5Chat%7Bx%7D_%7B1%7D%5E%7B0%7D-%5Cfrac%7Bb%7D%7Ba%7D%20%5Cright%20%29e%5E%7B-ak%7D)
, the prediction of the future data of the system can be realized. However, the GM model has obvious requirements for the predicted data. For example, the GM model is well suited to handle approximately 5–10 data. If the amount of data is too large or is fluctuating, the effect predicted by the GM model will be unsatisfactory.

### MGM 
The MGM model usually continues the calculation of the GM model in general. Specifically, the data processing method and the differential equation construction method of the MGM model are the same as the GM model. The difference is that the MGM model divides the prediction process of GM model into a number of prediction rounds, and the data used for each round of prediction is different. To illustratethe differences between the two models. For MGM model, only one unknown piece of data is predicted per round. Furthermore, the data used by the GM model for prediction is invariant, and the data used for each round of the MGM model is different. The specific alternative principle is in line with the physiological process of metabolism. Assume the number of data used for grey prediction is five.  After the first round of MGM model,the initial data is rejected, and the latest data reflecting the characteristics of the system is added. By analogy, each round of data sets used for MGM prediction is the one that best reflects system dynamics. This model overcomes a series of shortcomings of the traditional grey model for inaccurate prediction of large fluctuations in data. After this improvement, the MGM model can be applied to the prediction of large and volatile data sequences. The accuracy of the prediction is also greatly improved.
