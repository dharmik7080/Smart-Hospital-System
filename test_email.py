from utils.email_service import send_alert

def test_connection():
    print("Attempting to send test email to localhost:1025...")
    success = send_alert("O-", 2, "admin@hospital.com")
    
    if success:
        print("SUCCESS: Email sent to SMTP server.")
    else:
        print("FAILURE: Could not send email.")

if __name__ == "__main__":
    test_connection()
