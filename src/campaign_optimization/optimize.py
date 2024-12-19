import joblib
import numpy as np

def optimize_campaign_params(model_path, iterations=100):
    model = joblib.load(model_path)
    best_ctr = 0
    best_params = None
    for _ in range(iterations):
        age = np.random.randint(20,60)
        clicks = np.random.randint(10,300)
        impressions = np.random.randint(200,1000)
        cost = np.random.randint(50,500)
        ctr_pred = model.predict([[age, clicks, impressions, cost]])[0]
        if ctr_pred > best_ctr:
            best_ctr = ctr_pred
            best_params = {"age":age, "clicks":clicks, "impressions":impressions, "cost":cost}
    return best_params, best_ctr

if __name__ == "__main__":
    params, ctr = optimize_campaign_params("campaign_model.pkl", iterations=100)
    print("Best Params:", params)
    print("Estimated CTR:", ctr)