import streamlit as st

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="AEROGUARD",
    page_icon="🛰️",
    layout="wide"
)

# ----------------------------------------------------
# Header
# ----------------------------------------------------
st.title("🛰️ AEROGUARD")

st.subheader(
    "AI-Powered Satellite Change Detection Framework "
    "for Airport OLS Encroachment Monitoring"
)

st.markdown("---")

# ----------------------------------------------------
# About
# ----------------------------------------------------
st.header("Overview")

st.write(
    """
AEROGUARD is an AI-assisted geospatial monitoring framework that
combines Sentinel-2 satellite imagery, Google Earth Engine,
NDVI-based change detection, Deep Learning (U-Net),
GIS analytics, and ICAO-inspired Obstacle Limitation Surface (OLS)
assessment to automatically identify potential airport encroachments.
"""
)

# ----------------------------------------------------
# Features
# ----------------------------------------------------
st.header("Key Features")

st.markdown("""
- 🛰️ Sentinel-2 Multi-temporal Satellite Monitoring
- 🌱 NDVI Change Detection
- 🤖 U-Net Deep Learning Comparison
- 🌊 NDWI Water Filtering
- 🗺️ GIS Polygon Extraction
- ✈️ ICAO OLS Assessment
- 📊 Interactive Dashboard
- 📄 Automated PDF Report
- 📧 Email Alert Generation
""")

# ----------------------------------------------------
# Results
# ----------------------------------------------------
st.header("Notebook Results")

col1, col2 = st.columns(2)

with col1:
    st.metric("Detected Polygons", "301")
    st.metric("OLS Intersections", "184")

with col2:
    st.metric("Critical Alerts", "13")
    st.metric("High Severity", "90")

st.markdown("---")

st.info(
    "This dashboard is the landing page. "
    "Future versions will integrate the complete "
    "NDVI and U-Net processing pipeline."
)

# ----------------------------------------------------
# Footer
# ----------------------------------------------------
st.markdown("---")
st.caption("Developed by AK LABS | Neo-Nexus 36.1")