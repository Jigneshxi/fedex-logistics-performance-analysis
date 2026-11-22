# FedEx Logistics Performance Analysis & Global Supply Chain Optimization
**AlmaBetter Capstone Project — Numerical Programming in Python**  
**Author:** Jignesh Kumar | **Program:** MS in AI & ML (AlmaBetter & Woolf University)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-darkblue.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-100%25%20Completed-brightgreen.svg)]()
[![Tests](https://img.shields.io/badge/Pytest-5%2F5%20Passing-success.svg)]()

---

## 📌 Business Overview
FedEx Logistics manages complex, highly distributed international supply chains with shipments spanning multiple continents, transit modes, and rigorous compliance agreements. This capstone project provides an exhaustive empirical investigation into **10,324 global consignments**, evaluating shipment methods, purchase order lifecycle timelines, vendor agreements (INCO terms), and product pricing dynamics.

---

## 🎯 Core Architectural Questions Answered

```
+------------------------------------+       +------------------------------------+
|     1. Management Teams            |       |     2. Transportation Modes        |
|  PMO-US (11.5% delay) vs Field     | ----> |  Air (9.6% delay) vs Ocean (17.5%) |
|  Offices (1.8% delay).             |       |  Truck (16.1% delay).              |
+------------------------------------+       +------------------------------------+
                  |                                             |
                  v                                             v
+------------------------------------+       +------------------------------------+
|     3. Geographic Variance         |       |     4. Vendor INCO Terms           |
|  Vietnam (0.9% delay) vs           | ----> |  CIP (0.4%) & FCA (1.0%) vs        |
|  Mozambique (18.4% delay).         |       |  RDC Warehouse (17.2% delay).      |
+------------------------------------+       +------------------------------------+
                  |                                             |
                  v                                             v
+------------------------------------+       +------------------------------------+
|     5. Lead Time Dynamics          |       |     6. Insurance Economics         |
|  Delayed orders have longer mean   | ----> |  Line Item Insurance is ad valorem |
|  lead time (114.7d vs 105.2d).     |       |  (r = 0.962 with Commodity Value). |
+------------------------------------+       +------------------------------------+
```

---

## 📊 Summary of 15 Structured Visualizations

- **Chart 1**: Overall Delivery Status (88.51% On-Time, 11.49% Delayed)
- **Chart 2**: Transportation Mode Volume Distribution (Air: 59.2%, Truck: 27.4%, Ocean: 3.6%)
- **Chart 3**: Delay Rate Across Modes (Air: 9.60% vs Ocean: 17.52%)
- **Chart 4**: Top 10 Destination Countries by Volume (South Africa: 1,406, Nigeria: 1,194)
- **Chart 5**: Country Delay Rates (Vietnam: 0.87% vs Mozambique: 18.38%)
- **Chart 6**: Management Team Timeliness (PMO - US vs Field Offices)
- **Chart 7**: Vendor INCO Term vs Delay Rate (CIP/FCA < 1.1% vs RDC: 17.15%)
- **Chart 8**: Scheduled Lead Time Distribution (On-Time vs Delayed)
- **Chart 9**: Shipment Weight (kg) Across Modes (Ocean median 4,800 kg vs Air 450 kg)
- **Chart 10**: Freight Cost vs Weight Log-Log Scaling ($r = 0.469$)
- **Chart 11**: Insurance vs Line Item Value Ad Valorem Correlation ($r = 0.962$)
- **Chart 12**: Weight vs Line Item Insurance Relationship ($r = 0.623$)
- **Chart 13**: Product Group Delay Rates (ARV: 11.2%, HRDT: 12.4%)
- **Chart 14**: Multivariate Correlation Matrix Heatmap
- **Chart 15**: Pairwise Scatter Matrix of Operational Drivers

---

## 🧪 Automated Pytest Verification
Run the automated test suite locally:
```bash
pytest tests/test_fedex_logistics.py -v
```
All 5 automated tests verify row count (10,324), date calculations, SLA bounds, and correlation constraints.

---

## 📁 Repository Directory Structure
```
FedEx_Logistics_Performance_Analysis/
├── FedEx_Logistics_Dataset.csv          # Official 10,324-row logistics dataset
├── M2_FedEx_Logistics_EDA.ipynb         # Master executed Jupyter notebook (15 charts, 3 hypothesis tests)
├── VIDEO_PRESENTATION_SCRIPT.md         # 15-minute presentation script & interview Q&A
├── DOCUMENTATION_REPORT.md              # Executive stakeholder diagnostic report
├── tests/
│   └── test_fedex_logistics.py          # Pytest verification test suite
└── README.md                            # High-level overview & guide
```
