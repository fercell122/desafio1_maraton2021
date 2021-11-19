from sklearn.base import BaseEstimator


# All sklearn Transforms must have the `transform` and `fit` methods
class OutletTypeEncoder(BaseEstimator):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        data = data.dropna(axis='index', how='any', subset=['CHECKING_BALANCE'])
        data['CHECKING_BALANCE'] = data['CHECKING_BALANCE'].replace(['NO_CHECKING'],[0])
        data['EXISTING_SAVINGS'] = data['EXISTING_SAVINGS'].replace(['UNKNOWN'],[0])
        data['CHECKING_BALANCE'] = data['CHECKING_BALANCE'].apply(float)
        data['EXISTING_SAVINGS'] = data['EXISTING_SAVINGS'].apply(float)
        
    
        return data
