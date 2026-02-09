
# Smart Hospital Management System 🏥

A comprehensive Python-based Hospital Management System built with Streamlit. This application streamlines hospital operations, including patient registration, doctor appointments, blood bank inventory management, and AI-powered medical consultations.

## Features
-   **Admin Dashboard**: Manage staff, doctors, and system users.
-   **Reception Desk**: Patient registration and status updates.
-   **Doctor's Cabin**: View appointments, access patient history, and use AI for preliminary diagnosis and treatment planning.
-   **Blood Bank**: Monitor blood stock levels with automated alerts for critical shortages.
-   **Medical AI**: Integrated with Google Gemini for symptom analysis and treatment suggestions.

## 🔒 Security Note
This repository is configured to exclude sensitive information:
-   **Environment Variables**: `.env` files containing API keys (e.g., Google Gemini API) are excluded.
-   **Patient Data**: All local JSON data files in the `data/` directory are excluded to protect patient privacy and comply with data security standards.
-   **Configuration**: Streamlit secrets and local configuration files are omitted.

## 🚀 How to Run

### Prerequisites
-   Python 3.8+
-   Streamlit

### Setup
1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd hospital_management_system
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Ensure you include `streamlit`, `pandas`, `numpy`, `google-generativeai`, `python-dotenv` in your requirements)*

4.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Google Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

5.  **Run the Application**:
    ```bash
    streamlit run main.py
    ```

6.  **Login**:
    -   Use default credentials (if applicable) or create an Admin user via the interface if the system allows initialization.

---
*Built with ❤️ using Streamlit and Google Gemini.*
