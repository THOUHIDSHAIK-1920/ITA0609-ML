from sklearn.mixture import GaussianMixture
import numpy as np

def main():
    X = np.array([[1000],[1200],[1500],[5000],[5500],[6000]])

    model = GaussianMixture(n_components=2, random_state=42)
    model.fit(X)

    print("Customer Clusters:")
    print(model.predict(X))


if __name__ == '__main__':
    main()
