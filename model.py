import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def predict_viral(df):
    # Print the columns to debug
    print("Columns in the dataframe:", df.columns)
    
    # Assuming 'url' and ' shares' are the columns of interest
    if 'url' not in df.columns or ' shares' not in df.columns:
        raise KeyError("The required columns 'url' and ' shares' are not present in the DataFrame.")
    
    # Drop the 'url' column
    df = df.drop(columns=['url'])
    
    # Example: Categorize shares if not already done in your preprocessing step
    def categorize_shares(shares):
        if shares < 1500:
            return 'Not Viral'
        elif shares < 3000:
            return 'Quite Viral'
        else:
            return 'Viral'

    df['shares_category'] = df[' shares'].apply(categorize_shares)
    X = df.drop(columns=[' shares', 'shares_category'])
    y = df['shares_category']

    # Encode the target variable
    labelencoder = LabelEncoder()
    y = labelencoder.fit_transform(y)

    # Normalize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train the model (this is just for demonstration; in practice, you would load a pre-trained model)
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_scaled, y)
    
    predictions = model.predict(X_scaled)
    df['predictions'] = labelencoder.inverse_transform(predictions)
    
    return df[['predictions']]


