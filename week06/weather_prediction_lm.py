import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import joblib


def main(weather_data_path, alpha_value=0.1):

    # Define the variables we are predicting
    predictors = ["precip", "max_temp", "min_temp"]
    model_file = 'ridge_model.joblib'

    try:
        # Try loading the existing model
        reg = joblib.load(model_file)
    
    except FileNotFoundError:
        # If the model doesn't exist, train and save the model
        reg = Ridge(alpha=alpha_value)

        
        formatted_weather_data = clean_format_data_frame(weather_data_path)

        formatted_weather_data = create_target_predictor(formatted_weather_data)

        training_data = create_train_set(formatted_weather_data)
        print(training_data[predictors].shape)
        print(training_data["target"].shape)
        print(training_data[predictors].isnull().sum())

        testing_data = create_test_set(formatted_weather_data)

        # Fit the model
        try:
            reg.fit(training_data[predictors], training_data["target"])
            print("Model successfully fitted.")
            # Save the trained model to a file
            joblib.dump(reg, 'ridge_model.joblib')
        except Exception as e:
            print(f"Error occurred during model fitting: {e}")

    # Check if the model has the 'coef_' attribute (indicating it has been fitted)
    if hasattr(reg, 'coef_'):
        prediction = predict(reg, testing_data, predictors)
        prediction_accuracy = test_prediction_accuracy(testing_data, prediction)
        print(f"Prediction Accuracy: {prediction_accuracy}")
        compared_prediction = combine_prediction_actuals(testing_data, prediction)
        plot_comparison(compared_prediction)
    else:
        print("Model not fitted successfully.")
    return

def clean_format_data_frame(weather_data):

    # Read the file provided and store as a dataframe using Pandas module
    weather_data = pd.read_csv(weather_data)

    # Assuming the file was a csv file downloaded from NOAA it came with standard columns and labels.
    # Delete columns irrelevant to the machine learning model
    columns_to_delete = ["STATION", "NAME", "PRCP_ATTRIBUTES", "SNWD", "SNWD_ATTRIBUTES", "TMAX_ATTRIBUTES", "TMIN_ATTRIBUTES"]
    weather_data.drop(columns=columns_to_delete, inplace=True)

    # Convert string formatted dates to datetime objects
    weather_data['DATE'] = pd.to_datetime(weather_data["DATE"])

    # Where null values exist, forward fill with previous value.
    try:
        weather_data.fillna(method='ffill', inplace=True)
    except Exception as e:
        print(f"Error occurred during data processing: {e}")

    # Relabel default column labels
    new_column_labels = {'PRCP': 'precip', 'TMAX': 'max_temp', 'TMIN': 'min_temp'}
    weather_data.rename(columns=new_column_labels, inplace=True)

    # Save formatted and cleaned dataframe to a new csv file with added description as "modified"
    try:
        weather_data.to_csv('modified_weatherpalmerairport.csv', index=False)
    except Exception as e:
        print(f"Error occurred while saving the file: {e}")

    return weather_data

def create_target_predictor(weather_data):
    try:
        # Removes the most recent data entry
        weather_data["target"] = weather_data.shift(-1)["max_temp"]
        # Formats data to everything up to the new last data point
        weather_data = weather_data.iloc[:-1,:]
    except Exception as e:
        print(f"Error occurred during data manipulation: {e}")

    return weather_data

def create_train_set(weather_data):

    most_recent_date = weather_data["DATE"].max()

    two_years_ago = most_recent_date - pd.DateOffset(years=2)

    # Limits set on training data to all data up to 2 years behind most recent data entry
    training_data = weather_data.loc[weather_data["DATE"] <= two_years_ago]

    return training_data

def create_test_set(weather_data):

    most_recent_date = weather_data["DATE"].max()

    one_year_ago = most_recent_date - pd.DateOffset(years=1)

    # Limits set on testing data to all data from 1 year behind most recent data entry to present
    test_data = weather_data.loc[one_year_ago <= weather_data["DATE"]]

    return test_data

def predict(reg, test_data, predictors):

    # Using the test_data and the predictors defined, predict future values
    predictions = reg.predict(test_data[predictors])

    return predictions

def test_prediction_accuracy(test_data, predictions):

    # Test prediction accuracy by comparing with test data
    mean_abs_err = mean_absolute_error(test_data["target"], predictions)

    return mean_abs_err

def combine_prediction_actuals(test_data, predictions):

    # Organize results of predictions and actual values in test data for easier comparison
    combined_results = pd.concat([test_data["target"], pd.Series(predictions)], axis=1, ignore_index=True)

    combined_results.columns = ["Actual", "Predicted"]

    return combined_results

def plot_comparison(results):
    try:
        # Plot actual and predicted values with legend and show the plot
        plt.plot(results["Actual"], label="Actual")
        plt.plot(results["Predicted"], label="Predicted")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error occurred during plotting: {e}")
    return


palmer_weather_data = 'week06\weatherpalmerairport9724.csv'
main(palmer_weather_data)