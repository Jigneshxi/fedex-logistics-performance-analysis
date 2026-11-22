import pytest
import pandas as pd
import numpy as np

@pytest.fixture(scope="module")
def df():
    csv_file = "FedEx_Logistics_Dataset.csv"
    data = pd.read_csv(csv_file)
    data['Scheduled_Date'] = pd.to_datetime(data['Scheduled Delivery Date'], format='%d-%b-%y', errors='coerce')
    data['Delivered_Date'] = pd.to_datetime(data['Delivered to Client Date'], format='%d-%b-%y', errors='coerce')
    data['Delivery_Delay_Days'] = (data['Delivered_Date'] - data['Scheduled_Date']).dt.days
    data['Delivery_Status'] = data['Delivery_Delay_Days'].apply(lambda x: 'On-Time' if x <= 0 else 'Delayed')
    return data

def test_dataset_shape_and_records(df):
    assert len(df) == 10324, "Dataset must contain exactly 10,324 rows"
    assert df.shape[1] >= 33, "Dataset must have at least 33 raw attributes"

def test_sla_compliance_rate(df):
    on_time_rate = (df['Delivery_Status'] == 'On-Time').mean() * 100
    assert 88.0 <= on_time_rate <= 89.0, f"Expected ~88.5% on-time delivery, got {on_time_rate:.2f}%"

def test_delay_calculation_validity(df):
    assert df['Delivery_Delay_Days'].isnull().sum() == 0, "No null delivery delays allowed"
    delayed_subset = df[df['Delivery_Delay_Days'] > 0]
    assert (delayed_subset['Delivery_Status'] == 'Delayed').all(), "All positive delay days must be labeled 'Delayed'"

def test_transport_mode_consistency(df):
    modes = df['Shipment Mode'].dropna().unique()
    assert set(['Air', 'Truck', 'Air Charter', 'Ocean']).issubset(set(modes))

def test_insurance_value_correlation(df):
    sub = df[['Line Item Value', 'Line Item Insurance (USD)']].dropna()
    corr = sub.corr().iloc[0, 1]
    assert corr > 0.90, f"Expected strong ad valorem correlation (>0.90), got {corr:.3f}"
