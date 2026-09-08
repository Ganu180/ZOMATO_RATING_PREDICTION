import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Zomato Restaurant Rating Predictor",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #f7f8fc;
    }

    /* Main container */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #e23744;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #666666;
        margin-bottom: 25px;
    }

    /* Section headings */
    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #222222;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    /* Prediction result */
    .prediction-number {
        font-size: 55px;
        font-weight: 800;
        color: #e23744;
        text-align: center;
    }

    .prediction-label {
        text-align: center;
        font-size: 18px;
        color: #666666;
    }

    .stars {
        text-align: center;
        font-size: 32px;
        color: #ffb400;
        letter-spacing: 5px;
    }

    .prediction-message {
        text-align: center;
        font-size: 21px;
        font-weight: 700;
        color: #333333;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #888888;
        font-size: 14px;
        padding-top: 25px;
        margin-top: 40px;
        border-top: 1px solid #dddddd;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL PATH
# ============================================================

MODEL_PATH = Path("zomato_rating_model.pkl")


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🍽️ Zomato Restaurant Rating Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict a restaurant\'s expected rating using Machine Learning.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CHECK MODEL
# ============================================================

if not MODEL_PATH.exists():

    st.error(
        "❌ Model file not found."
    )

    st.info(
        "Make sure 'zomato_rating_model.pkl' "
        "is present in the same folder as app.py."
    )

    st.stop()


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load(MODEL_PATH)


model = load_model()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 Model Information")

    st.divider()

    st.subheader("Algorithm")

    st.write(
        "🌲 Random Forest Regression"
    )

    st.subheader("Task")

    st.write(
        "Restaurant Rating Prediction"
    )

    st.subheader("Output")

    st.write(
        "Rating out of 5"
    )

    st.divider()

    st.subheader("📊 Model Performance")

    st.metric(
        "R² Score",
        "0.741"
    )

    st.metric(
        "MAE",
        "0.160"
    )

    st.metric(
        "RMSE",
        "0.223"
    )

    st.divider()

    st.info(
        """
        The model uses restaurant information,
        preprocessing, One-Hot Encoding and
        Random Forest Regression.
        """
    )


# ============================================================
# RESTAURANT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">📝 Restaurant Information</div>',
    unsafe_allow_html=True
)

st.caption(
    "Enter the restaurant details below."
)


# ============================================================
# TWO COLUMN INPUT
# ============================================================

left_col, right_col = st.columns(2)


# ============================================================
# LEFT COLUMN
# ============================================================

with left_col:

    st.subheader("🏪 Restaurant Details")

    online_order = st.selectbox(
        "Online Order Available?",
        ["Yes", "No"],
        help="Does the restaurant provide online ordering?"
    )

    book_table = st.selectbox(
        "Table Booking Available?",
        ["Yes", "No"],
        help="Can customers reserve a table?"
    )

    location = st.text_input(
        "📍 Location",
        placeholder="Example: Banashankari",
        help="Restaurant location."
    )

    rest_type = st.text_input(
        "🏪 Restaurant Type",
        placeholder="Example: Casual Dining",
        help="Type of restaurant."
    )

    cuisines = st.text_input(
        "🍛 Cuisines",
        placeholder="Example: North Indian, Chinese",
        help="Cuisine types served by the restaurant."
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

with right_col:

    st.subheader("📊 Restaurant Statistics")

    listed_in_type = st.text_input(
        "📋 Listed In Type",
        placeholder="Example: Delivery",
        help="Restaurant listing category."
    )

    listed_in_city = st.text_input(
        "🏙️ Listed In City",
        placeholder="Example: Banashankari",
        help="City/category in which the restaurant is listed."
    )

    votes = st.number_input(
        "👍 Number of Votes",
        min_value=0,
        value=100,
        step=1,
        help="Total votes received by the restaurant."
    )

    approx_cost = st.number_input(
        "💰 Approximate Cost for Two",
        min_value=0.0,
        value=500.0,
        step=50.0,
        help="Approximate cost for two people."
    )


# ============================================================
# BUILD MODEL INPUT
# ============================================================

def build_input():

    # Get exact columns used during model training
    expected_columns = list(
        model.named_steps["preprocessor"].feature_names_in_
    )

    raw_input = {

        "online_order":
            1 if online_order == "Yes" else 0,

        "book_table":
            1 if book_table == "Yes" else 0,

        "votes":
            votes,

        "location":
            location.strip(),

        "rest_type":
            rest_type.strip(),

        "cuisines":
            cuisines.strip(),

        "approx_costfor_two_people":
            approx_cost,

        "listed_intype":
            listed_in_type.strip(),

        "listed_incity":
            listed_in_city.strip()
    }


    # Possible column-name variations

    column_aliases = {

        "approx_cost_for_two_people":
            "approx_costfor_two_people",

        "listed_in_type":
            "listed_intype",

        "listed_in_city":
            "listed_incity"
    }


    normalized_input = {}


    for column in expected_columns:

        if column in raw_input:

            normalized_input[column] = raw_input[column]

        elif column in column_aliases:

            original_column = column_aliases[column]

            normalized_input[column] = raw_input[
                original_column
            ]

        else:

            normalized_input[column] = None


    # Create DataFrame

    input_data = pd.DataFrame(
        [normalized_input],
        columns=expected_columns
    )


    # Numerical columns

    numerical_columns = [

        "online_order",
        "book_table",
        "votes",
        "approx_costfor_two_people"
    ]


    for column in numerical_columns:

        if column in input_data.columns:

            input_data[column] = pd.to_numeric(
                input_data[column],
                errors="coerce"
            )


    # Categorical columns

    categorical_columns = [

        "location",
        "rest_type",
        "cuisines",
        "listed_intype",
        "listed_incity"
    ]


    for column in categorical_columns:

        if column in input_data.columns:

            input_data[column] = (
                input_data[column]
                .astype(str)
            )


    return input_data


# ============================================================
# BUTTONS
# ============================================================

st.divider()

predict_col, reset_col = st.columns([3, 1])


with predict_col:

    predict_button = st.button(
        "🔮 Predict Restaurant Rating",
        type="primary",
        use_container_width=True
    )


with reset_col:

    reset_button = st.button(
        "↻ Reset",
        use_container_width=True
    )


# ============================================================
# RESET
# ============================================================

if reset_button:

    st.rerun()


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # Required fields

    required_fields = {

        "Location":
            location,

        "Restaurant Type":
            rest_type,

        "Cuisines":
            cuisines,

        "Listed In Type":
            listed_in_type,

        "Listed In City":
            listed_in_city
    }


    missing_fields = [

        name

        for name, value
        in required_fields.items()

        if not value.strip()
    ]


    if missing_fields:

        st.warning(
            "⚠️ Please fill in: "
            + ", ".join(missing_fields)
        )


    else:

        try:

            # Build input

            input_data = build_input()


            # Predict

            prediction = model.predict(
                input_data
            )[0]


            # Keep rating between 0 and 5

            prediction = max(
                0,
                min(
                    5,
                    float(prediction)
                )
            )


            # ==================================================
            # RATING CATEGORY
            # ==================================================

            if prediction >= 4.5:

                stars = "★★★★★"

                message = (
                    "🌟 Excellent Restaurant"
                )


            elif prediction >= 4.0:

                stars = "★★★★☆"

                message = (
                    "⭐ Very Good Restaurant"
                )


            elif prediction >= 3.0:

                stars = "★★★☆☆"

                message = (
                    "👍 Good Restaurant"
                )


            elif prediction >= 2.0:

                stars = "★★☆☆☆"

                message = (
                    "⚠️ Needs Improvement"
                )


            else:

                stars = "★☆☆☆☆"

                message = (
                    "🔻 Low Rating"
                )


            # ==================================================
            # RESULT
            # ==================================================

            st.divider()

            st.subheader(
                "🎯 Prediction Result"
            )


            st.markdown(
                '<div class="prediction-label">'
                'Predicted Restaurant Rating'
                '</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                f'<div class="prediction-number">'
                f'{prediction:.2f} / 5'
                f'</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                f'<div class="stars">'
                f'{stars}'
                f'</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                f'<div class="prediction-message">'
                f'{message}'
                f'</div>',
                unsafe_allow_html=True
            )


            # ==================================================
            # SUMMARY
            # ==================================================

            st.subheader(
                "📌 Prediction Summary"
            )


            summary1, summary2, summary3 = st.columns(3)


            with summary1:

                st.metric(
                    "Online Order",
                    (
                        "Available"
                        if online_order == "Yes"
                        else "Not Available"
                    )
                )


            with summary2:

                st.metric(
                    "Total Votes",
                    f"{votes:,}"
                )


            with summary3:

                st.metric(
                    "Cost for Two",
                    f"₹{approx_cost:,.0f}"
                )


            # ==================================================
            # MODEL INPUT
            # ==================================================

            with st.expander(
                "🔍 View Data Sent to Model"
            ):

                st.dataframe(
                    input_data,
                    use_container_width=True,
                    hide_index=True
                )


        except Exception as e:

            st.error(
                f"❌ Prediction failed: {e}"
            )


# ============================================================
# HOW IT WORKS
# ============================================================

st.divider()

st.subheader(
    "🧠 How the Model Works"
)

st.write(
    "Restaurant Data"
    " → "
    "Preprocessing"
    " → "
    "One-Hot Encoding"
    " → "
    "Random Forest Regression"
    " → "
    "Predicted Rating"
)


# ============================================================
# ABOUT PROJECT
# ============================================================

with st.expander(
    "📚 About This Project"
):

    st.markdown(
        """
        ### Zomato Rating Prediction

        This project predicts a restaurant's expected
        rating using Machine Learning.

        **Algorithm**

        - Random Forest Regression

        **Features**

        - Online Order
        - Table Booking
        - Votes
        - Location
        - Restaurant Type
        - Cuisines
        - Approximate Cost for Two
        - Listed In Type
        - Listed In City

        **Model Performance**

        - R² Score: **0.741**
        - MAE: **0.160**
        - RMSE: **0.223**

        **Technology Stack**

        - Python
        - Pandas
        - Scikit-learn
        - Streamlit
        - Joblib

        **Note:** The prediction is an estimate generated
        by the machine-learning model and is not a guarantee
        of the actual restaurant rating.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🍽️ Zomato Rating Prediction<br>
        Random Forest Regression • Python • Pandas •
        Scikit-learn • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)