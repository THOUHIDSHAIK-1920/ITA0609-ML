"""program 10: Expectation-Maximization (EM) for 1D Gaussian Mixture (two components)
Simple EM implementation (didactic).
"""
import numpy as np
from scipy.stats import norm


def generate_data():
    np.random.seed(0)
    x1 = np.random.normal(loc=-2, scale=0.8, size=200)
    x2 = np.random.normal(loc=3, scale=1.2, size=300)
    return np.hstack([x1, x2])


def em_gmm(x, n_iter=100):
    x = x.reshape(-1, 1)
    n = x.shape[0]
    # init params
    weights = np.array([0.5, 0.5])
    means = np.array([np.min(x), np.max(x)]).ravel().astype(float)
    sigmas = np.array([1.0, 1.0])

    for _ in range(n_iter):
        # E-step: responsibilities
        resp = np.zeros((n, 2))
        for k in range(2):
            resp[:, k] = weights[k] * norm.pdf(x.ravel(), means[k], sigmas[k])
        resp = resp / resp.sum(axis=1, keepdims=True)

        # M-step
        Nk = resp.sum(axis=0)
        weights = Nk / n
        means = (resp * x).sum(axis=0) / Nk
        sigmas = np.sqrt(((resp * (x - means) ** 2).sum(axis=0) / Nk).ravel())

    return weights, means, sigmas


def main():
    x = generate_data()
    w, m, s = em_gmm(x, n_iter=50)
    print("Weights:", w)
    print("Means:", m)
    print("Stds:", s)


if __name__ == '__main__':
    main()
