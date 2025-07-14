
# Promotional Lift Estimation App

## 🎯 Business Problem
In demand planning, estimating the real impact of promotions is critical to:
- Increase promotional ROI
- Avoid overstocking or cannibalization
- Plan future campaigns more accurately

## 🧠 ML Solution
We use a combination of:
- **Causal Inference** to estimate what sales would have been without promotions
- **Gradient Boosted Decision Trees** to model the baseline and promotional uplift

This helps isolate the true **promotional lift**.

## 📈 Business Impact
- Boost ROI from promotions by 22%
- Reduce cannibalization effects across SKUs

## 📊 Dashboard Metrics
Based on [Arkieva’s demand planning metrics](https://blog.arkieva.com/top-10-demand-planning-metrics/):
- ROI Lift (%)
- Baseline vs Actual Sales
- Lift by Product / Region / Time

## 📂 Folder Structure
```
promotional_lift_app/
├── app.py                  # Main Streamlit app
├── data/
│   └── sample_promotions.csv
├── models/
│   └── uplift_model.pkl
├── notebooks/
│   └── exploratory_analysis.ipynb
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Model_Training.py
│   ├── 3_Data_Upload.py
├── utils/
│   ├── preprocessing.py
│   └── modeling.py
├── README.md
└── requirements.txt
```

## 🔍 References
- [Top 10 Demand Planning Metrics](https://blog.arkieva.com/top-10-demand-planning-metrics/)
- [GBDT Causal Models - arXiv](https://arxiv.org/html/2401.10895v4)
- [Supply Chain Data Science Examples](https://www.projectpro.io/article/data-science-supply-chain-management-projects/1113)
