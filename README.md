# Diabetes Prediction

This repository contains a Flask web application designed to predict diabetes using a K-Nearest Neighbors (KNN) model. The prediction is based on user-inputted medical attributes, such as Glucose level, Blood Pressure, and BMI, among others. The model was trained on a dataset containing several medical attributes of individuals and whether or not they had diabetes. 

## Project Structure

- `analysis.ipynb` - Jupyter notebook containing the analysis of different machine learning algorithms on the dataset and their performance.
- `app.py` - The Flask application.
- `model.py` - Script used to train the model and generate `knn_model.pkl` and `scaler.pkl`.
- `/templates/index.html` - Contains HTML files for the web interface.
- `/static/style.css` - Contains CSS files for styling the web interface. 
- `knn_model.pkl` - The serialized KNN model used for making predictions.
- `scaler.pkl` - The serialized scaler used to normalize input features.

## User Interface

https://github.com/sherwinvishesh/Diabetes-Prediction/assets/60791187/e0fc12df-9042-46da-b793-425cff62c46c




## Analysis Summary

The analysis conducted in `analysis.ipynb` tested various machine learning models on the dataset to identify which model provides the most accurate predictions for diabetes. The results of the analysis are as follows:

- **K-Nearest Neighbors (KNN):** Achieved the highest accuracy of **81.1%**.
- **Support Vector Machine (SVM):** Achieved an accuracy of **79.8%**.
- **Logistic Regression:** Achieved an accuracy of **80.5%**.

Based on this analysis, the KNN model was chosen for the web application due to its superior performance.





## Installation

To run Diabetes-Prediction on your local machine, you need Python 3.6+ installed. Follow these steps:

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/sherwinvishesh/Diabetes-Prediction.git
    ```
2. Navigate to the project directory.
    ```bash
    cd Diabetes-Prediction
    ```
3. Install the required Python packages.
    ```bash
    pip install Flask scikit-learn numpy pandas
    ```
    `If you are getting any errors while installing the above`
    Then you have to create a virtual environment and run this program, here are the steps:
    Create a Virtual Environment:
    ```bash
    python3 -m venv path/to/venv
    ```
    Activate the Virtual Environment:
    mac or linux 
    ```bash
    source path/to/venv/bin/activate
    ```

    For Windows:
    ```bash
    path\to\venv\Scripts\activate
    ```
4. Run the `model.py` to generate `knn_model.pkl` and `scaler.pkl`
    ```bash
    python3 model.py
    ```


5. Run the Flask application.
    ```bash
    python3 app.py
    ```





## Usage

After running the application and accessing it at `http://127.0.0.1:5000/`, follow these steps to receive a diabetes prediction:

1. **Enter Medical Information**: Fill in the form with the medical attributes required by the model. The required inputs include:

   - **Pregnancies**: Number of times pregnant
   - **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
   - **Blood Pressure**: Diastolic blood pressure (mm Hg)
   - **Skin Thickness**: Triceps skin fold thickness (mm)
   - **Insulin**: 2-Hour serum insulin (mu U/ml)
   - **BMI**: Body mass index (weight in kg/(height in m)^2)
   - **Diabetes Pedigree Function**: A function that scores the likelihood of diabetes based on family history
   - **Age**: Age (years)

2. **Submit for Prediction**: After filling in the form with the necessary medical information, click the "Predict" button to submit the data for prediction.

3. **View Prediction Result**: The prediction result will be displayed on the page, indicating whether the inputted attributes suggest a diagnosis of diabetes ("Yes" for diabetic, "No" for not diabetic).

### Example Usage Scenario

- Suppose you want to know the diabetes prediction for an individual with the following attributes:
  - Pregnancies: 2
  - Glucose: 138
  - Blood Pressure: 62
  - Skin Thickness: 35
  - Insulin: 0
  - BMI: 33.6
  - Diabetes Pedigree Function: 0.627
  - Age: 47
  
  You would enter these values into the form and click "Predict" to see if the model predicts this individual as diabetic or not.



## Contributing

Contributions to enhance this project are welcomed. Please feel free to fork the repository, make changes, and submit pull requests.

## Support

If you encounter any issues or have any questions, please submit an issue on the GitHub issue tracker or feel free to contact me.


## License

This project is open source and available under the [Apache-2.0 license](LICENSE).

## Acknowledgments


- Thanks to everyone who visits and uses this page. Your interest and feedback are what keep us motivated.
- Special thanks to all the contributors who help maintain and improve this project. Your dedication and hard work are greatly appreciated.
- Special acknowledgment to Kavya11-2 for her project [Diabetic_Prediction](https://github.com/Kavya11-2/Diabetic_Prediction_Internship). It served as a significant inspiration for this project, demonstrating the powerful impact of Machine Learning.

## Disclaimer

This tool is intended for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## Connect with Me

Feel free to reach out and connect with me on [LinkedIn](https://www.linkedin.com/in/sherwinvishesh) or [Instagram](https://www.instagram.com/sherwinvishesh/).

---

Made with ❤️ by Sherwin



