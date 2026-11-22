# Executive Diagnostic Report: FedEx Logistics Global Performance Analysis
**AlmaBetter Capstone Project: Numerical Programming in Python**  
**Author:** Jignesh Kumar  
**Domain:** Supply Chain Analytics, Freight Operations & Global Logistics

---

## 1. Executive Summary
This report delivers an empirical performance evaluation of FedEx Logistics' international health supply chain operations across **10,324 shipments** spanning 43 recipient nations. The study investigates transport mode efficiency, vendor fulfillment agreements (INCO terms), regional delay bottlenecks, and cost scaling economics.

### Key Performance Indicators:
- **Total Shipment Volume**: 10,324 consignments
- **Overall SLA Compliance**: 88.51% On-Time (9,138 shipments) | 11.49% Delayed (1,186 shipments)
- **Air Freight Reliability**: 9.60% delay rate across 6,113 consignments (benchmark performer)
- **Ocean Freight Delay Vulnerability**: 17.52% delay rate across 371 consignments
- **Insurance Pricing Mechanism**: Near-perfect ad valorem pricing correlation ($r = 0.962$) with commodity value.

---

## 2. Statistical Hypothesis Testing Summary

| Hypothesis | Test Applied | Test Statistic | p-value | Decision | Business Takeaway |
|---|---|---|---|---|---|
| **H1: Delay across Transport Modes (Air vs Ocean)** | Mann-Whitney U Test | $U = 1,225,483.5$ | $p = 1.48 	imes 10^{-6}$ | **Reject H0** | Ocean shipments suffer statistically significant greater transit delays than Air shipments. |
| **H2: Vendor INCO Term vs Timeliness** | Chi-Square Test ($\chi^2$) | $\chi^2 = 342.18$ ($df = 7$) | $p = 4.12 	imes 10^{-70}$ | **Reject H0** | Delivery punctuality is strongly dependent on the commercial contract term (CIP/FCA outperform EXW/RDC). |
| **H3: Country Delay Variation** | One-Way ANOVA | $F = 43.82$ ($df = 4$) | $p = 1.09 	imes 10^{-35}$ | **Reject H0** | Destination country infrastructure and customs clearance create significant delay disparities. |

---

## 3. Strategic Recommendations Roadmap
1. **Dynamic Modal Allocation**: Avoid ocean freight for urgent diagnostic replenishment; maintain air freight corridors.
2. **Contractual Transition to CIP/FCA**: Shift vendor agreements toward carriage and insurance paid terms.
3. **Regional Decentralization**: Empower regional field offices to replicate the 98.25% on-time performance achieved in South Africa.
4. **Lead-Time Buffer Management**: Establish automated risk flags for purchase orders exceeding 100 days of lead time.
