# Video Presentation Script: FedEx Logistics Performance Analysis
**AlmaBetter Capstone Project: Numerical Programming in Python**  
**Student / Presenter:** Jignesh Kumar  
**Target Duration:** 15.0 Minutes (8 Structured Sections)

---

## ⏱️ Section 1: Introduction (1.5 Minutes)
- **Presenter Spoken Script**:
  > "Hello everyone, my name is Jignesh Kumar, and today I am excited to present my Capstone Project: **FedEx Logistics Performance Analysis and Global Supply Chain Optimization**.
  > This analysis is situated within the international freight forwarding and global health logistics domain. FedEx Logistics manages complex international consignments carrying critical medical diagnostics and pharmaceuticals to over 40 countries across Africa, Asia, and the Americas.
  > The primary objective is to diagnose transit bottlenecks, assess vendor SLA compliance, evaluate freight mode trade-offs, and deliver an empirical optimization framework.
  > The core technology stack includes Python 3, Pandas and NumPy for vectorized data wrangling, Matplotlib and Seaborn for statistical storytelling, SciPy for hypothesis testing, and Google Colab as the interactive execution environment."

- **What Interviewer Evaluates**:
  - Clarity of project objective
  - Domain fluency and analytical context

---

## ⏱️ Section 2: Problem Understanding (2.0 Minutes)
- **Presenter Spoken Script**:
  > "Let's examine the core business problem. Global supply chains operate under tight delivery deadlines where transit delays can lead to stockouts of life-saving antiretrovirals, monetary penalties, and customer churn.
  > In this project, we analyze 10,324 global shipments across 33 attributes, capturing purchase order dates, scheduled delivery milestones, fulfillment channels, vendor INCO agreements, shipment modes, package weights, and freight expenditures.
  > Our key questions are:
  > First: Does the choice of transportation mode (Air vs Ocean vs Truck) dictate delivery punctuality?
  > Second: Do specific countries or management structures exhibit systemic delay clusters?
  > Third: How do vendor INCO terms and lead times impact fulfillment reliability?
  > And Fourth: What economic principles govern freight costs and line item insurance?"

---

## ⏱️ Section 3: Data Understanding & Preparation (2.0 Minutes)
- **Presenter Spoken Script**:
  > "Now turning to data preparation. The raw dataset contains 10,324 records. While dates like Scheduled Delivery Date and Delivered to Client Date had 100% completeness, several critical columns contained mixed audit strings:
  > For example, Weight in Kilograms contained entries like 'Weight Captured Separately', and Freight Cost contained 'Freight Included in Commodity Cost'.
  > We applied defensive data wrangling:
  > First, we parsed dates into proper datetime objects and computed `Delivery_Delay_Days` by subtracting the Scheduled Date from Delivered Date.
  > Shipments with delay days less than or equal to zero were classified as 'On-Time', while those with positive days were categorized as 'Delayed'.
  > Second, we coerced non-numeric strings in Weight and Freight to floating-point numbers.
  > Third, we computed the Procurement Lead Time by measuring the interval between Purchase Order dispatch and Scheduled Delivery Date.
  > This gave us a clean, robust tabular structure for exploration."

---

## ⏱️ Section 4: EDA Design & Analysis Flow (2.5 Minutes)
- **Presenter Spoken Script**:
  > "Our exploratory data analysis followed a structured, hypothesis-driven hierarchy:
  > We began with **Univariate Analysis** to establish baseline distributions: calculating the overall SLA compliance rate, frequency of shipment modes, and top destination countries.
  > Next, we transitioned to **Bivariate Analysis** to evaluate relationships between operational levers and delivery outcomes: examining delay rates across shipment modes, comparing field office management against centralized PMO teams, and correlating INCO terms with vendor timeliness.
  > Finally, we performed **Multivariate Analysis**: analyzing the interaction between physical cargo weight, commodity valuation, and freight costs, culminating in correlation heatmaps and pairwise scatter matrices.
  > This structured sequence ensured every visualization built upon the prior insight without disconnected jumping."

---

## ⏱️ Section 5: Key Visualizations & Insights (2.0 Minutes)
- **Presenter Spoken Script**:
  > "Here are the top findings from our 15 visualizations:
  > **Finding 1**: The overall on-time delivery rate is 88.51%, with 11.49% experiencing delays.
  > **Finding 2**: Transport mode significantly drives timeliness. Air freight is the most reliable at a 9.60% delay rate. In stark contrast, Ocean freight experiences an elevated 17.52% delay rate, and Trucking suffers a 16.08% delay rate due to cross-border clearance.
  > **Finding 3**: Geographic divergence is prominent. Vietnam achieved an exceptional 0.87% delay rate, while Mozambique (18.38%) and Zambia (15.81%) experienced significant delays due to port and infrastructure friction.
  > **Finding 4**: Vendor INCO terms reveal that CIP (0.36%) and FCA (1.01%) offer the lowest delays, whereas internal Regional Distribution Centers suffer a 17.15% delay rate.
  > **Finding 5**: Insurance cost exhibits a near-perfect correlation of r = 0.962 with Commodity Value, proving insurance is computed ad valorem rather than based on transit friction."

---

## ⏱️ Section 6: Business Interpretation & Data Storytelling (2.0 Minutes)
- **Presenter Spoken Script**:
  > "What do these insights mean for supply chain stakeholders?
  > First, modal choice represents a clear speed-versus-cost trade-off. While Ocean is economical for massive payloads (median 4,800 kg), its 17.5% delay rate makes it unsuitable for emergency replenishment.
  > Second, decentralized management works: South Africa Field Office achieved a 98.25% on-time rate, outperforming centralized PMO - US.
  > Third, long-horizon orders face compounding vulnerability: delayed shipments had an average lead time of 114.7 days versus 105.2 days for on-time shipments. Breaking procurement into phased delivery milestones mitigates this risk."

---

## ⏱️ Section 7: Testing, Notebook Quality & Challenges (1.5 Minutes)
- **Presenter Spoken Script**:
  > "To ensure rigorous quality, all analysis was structured into a clean, pre-executed Jupyter notebook adhering strictly to the AlmaBetter Capstone rubric:
  > Every chart contains answers to: Why the chart was chosen, what insights were found, and the strategic business impact.
  > We implemented an automated pytest test suite (`test_fedex_logistics.py`) that validates row counts (10,324), schema types, and the 88.5% SLA benchmark.
  > Key challenges included managing mixed-type strings in weight and freight columns and handling right-skewed monetary distributions, which we resolved using robust median metrics and logarithmic scaling."

---

## ⏱️ Section 8: Conclusion, Learnings & Improvements (1.5 Minutes)
- **Presenter Spoken Script**:
  > "In conclusion, this project delivered an empirical roadmap for FedEx Logistics, isolating delay triggers across modes, geographies, and procurement terms.
  > Key learnings include the power of vectorized Pandas transformations, statistical hypothesis validation, and translating distribution charts into executive business decisions.
  > For future enhancements, we can:
  > 1. Build a predictive machine learning classifier (e.g. XGBoost) to forecast delivery delay risk at PO creation.
  > 2. Develop an interactive PowerBI or Streamlit executive dashboard for real-time shipment tracking.
  > Thank you for your time, and I look forward to your questions!"

---

## 🎓 Follow-up Interview Questions & Model Answers

### Q1: Why did you choose these specific chart types?
**Answer**:
> "I selected chart types tailored to variable types and analytical goals: pie and bar charts for categorical composition (SLA status, shipment modes), horizontal bar charts for high-cardinality ranking (top 10 countries, INCO terms), KDE and violin plots for skewed continuous variables (lead time, delay days), log-log scatter plots with regression trends for heavy-tailed monetary variables, and correlation heatmaps for multivariate interactions."

### Q2: Which insight was the most actionable and why?
**Answer**:
> "The finding on Vendor INCO Terms was the most actionable: shipments fulfilled via CIP and FCA achieved under 1.1% delay rates, whereas shipments routed through Regional Distribution Centers (RDCs) experienced a 17.15% delay rate. This provides immediate leverage for procurement managers to renegotiate vendor contracts toward CIP agreements."

### Q3: How did you handle missing or inconsistent data?
**Answer**:
> "Columns like `Weight (Kilograms)` and `Freight Cost (USD)` contained alphanumeric strings such as 'Weight Captured Separately' and 'Freight Included in Commodity Cost'. I used `pd.to_numeric(errors='coerce')` to parse valid numbers while converting unrecorded placeholders to NaN, ensuring statistical calculations remained uncorrupted without discarding entire rows."

### Q4: What further analysis would you perform next?
**Answer**:
> "I would incorporate external geospatial distance matrices and seasonal weather datasets to isolate seasonal monsoon and port strike delays from carrier-driven delays."

### Q5: How would you extend this project into machine learning or dashboard development?
**Answer**:
> "I would formulate a binary classification problem (`Is_Delayed`) using XGBoost and LightGBM, incorporating engineered features like lead time, vendor historical delay rate, and modal risk score, deployed as a REST API and real-time PowerBI dashboard."
