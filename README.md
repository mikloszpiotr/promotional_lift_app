
# 📈 Promotional Lift Estimation App

This Streamlit ML app helps demand planners estimate the **true impact of promotions** using machine learning.  
It compares predicted baseline (non-promoted) sales to actual outcomes and highlights where marketing efforts generate real uplift.

---

## 🧠 Machine Learning Solution

- **Model**: Gradient Boosted Decision Trees (XGBoost)
- **Technique**: Counterfactual estimation using `is_promoted` feature toggle
- **Goal**: Quantify incremental sales driven by promotions vs. baseline demand
- **ML Pipeline**:
  - Trains on pricing, competitor pricing, and promotion flag
  - Simulates predicted sales with and without promotions
  - Computes uplift as the difference
  - Presents ROI and product-level analysis

---

## 📊 Key Dashboard Features

- Upload or preview promotional data
- Train a model and simulate promotional scenarios
- Visualize:
  - Predicted Sales vs. Baseline
  - Estimated Uplift per product
  - ROI lift %
- Explore a product-level uplift summary table

---

## 📂 Folder Structure

```
promotional_lift_app/
├── app.py                  # Main Streamlit app
├── data/                   # Sample promotion data
├── models/                 # Trained uplift model (saved automatically)
├── pages/                  # Streamlit dashboard pages
├── utils/                  # Preprocessing and model logic
├── notebooks/              # Optional analysis
├── README.md
└── requirements.txt
```

---

## 📈 Example Use Case

This app is designed for:
- **Demand planners** looking to justify promotional investments
- **Marketing analysts** assessing uplift effectiveness
- **Supply chain teams** balancing inventory decisions around promotions

---

## 🔧 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔗 References

- [Top 10 Demand Planning Metrics – Arkieva](https://blog.arkieva.com/top-10-demand-planning-metrics/)
- [GBDT Causal Inference Paper – arXiv](https://arxiv.org/html/2401.10895v4)
- [Promotion Lift Examples – ProjectPro](https://www.projectpro.io/article/data-science-supply-chain-management-projects/1113)

---

**Author**: [@mikloszpiotr](https://github.com/mikloszpiotr)  
_Enhancing supply chain decisions with ML-powered analytics._
