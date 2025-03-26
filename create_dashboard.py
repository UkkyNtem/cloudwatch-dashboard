import subprocess

DASHBOARD_NAME = "UkMonitoringDashboard"
JSON_FILE = "cloudwatch_dashboard.json"

def create_dashboard():
    try:
        result = subprocess.run([
            "aws", "cloudwatch", "put-dashboard",
            "--dashboard-name", DASHBOARD_NAME,
            "--dashboard-body", f"file://{JSON_FILE}"
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Dashboard '{DASHBOARD_NAME}' created successfully.")
        else:
            print("❌ Error creating dashboard:")
            print(result.stderr)

    except Exception as e:
        print("Exception occurred:", e)

if __name__ == "__main__":
    create_dashboard()

