import sys
import requests
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QGridLayout
)

class CombinedApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Driver and Rider Application")
        self.setGeometry(100, 100, 900, 600)

        # Initialize UI
        self.initUI()

        # Set up timers for automatic updates
        self.driver_timer = QTimer(self)
        self.driver_timer.timeout.connect(self.driver_api_call)
        self.driver_timer.start(10000)  # Update every 10 seconds

        self.rider_timer = QTimer(self)
        self.rider_timer.timeout.connect(self.rider_api_call)
        self.rider_timer.start(10000)  # Update every 10 seconds

    def initUI(self):
        # Create Tabs
        tabs = QTabWidget()
        tabs.addTab(self.create_driver_tab(), "Driver")
        tabs.addTab(self.create_rider_tab(), "Rider")

        # Set Central Widget
        self.setCentralWidget(tabs)

    def create_driver_tab(self):
        """Creates the Driver Tab UI."""
        driver_tab = QWidget()
        layout = QVBoxLayout()

        # Input Section
        input_layout = QGridLayout()
        self.driver_id_input = QLineEdit()
        self.driver_id_input.setPlaceholderText("Enter Driver ID")
        self.driver_update_input = QLineEdit()
        self.driver_update_input.setPlaceholderText("Enter Status (true/false)")

        input_layout.addWidget(QLabel("Driver ID:"), 0, 0)
        input_layout.addWidget(self.driver_id_input, 0, 1)
        input_layout.addWidget(QLabel("Update Status:"), 1, 0)
        input_layout.addWidget(self.driver_update_input, 1, 1)

        # Submit Button
        self.driver_submit_button = QPushButton("Submit")
        self.driver_submit_button.clicked.connect(self.driver_api_call)

        # Output Section
        self.driver_output_area = QTextEdit()
        self.driver_output_area.setReadOnly(True)

        # Assemble Layout
        layout.addLayout(input_layout)
        layout.addWidget(self.driver_submit_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.driver_output_area)

        driver_tab.setLayout(layout)
        return driver_tab

    def create_rider_tab(self):
        """Creates the Rider Tab UI."""
        rider_tab = QWidget()
        layout = QVBoxLayout()

        # Input Section
        input_layout = QGridLayout()
        self.rider_id_input = QLineEdit()
        self.rider_id_input.setPlaceholderText("Enter Rider ID")
        self.rider_update_input = QLineEdit()
        self.rider_update_input.setPlaceholderText("Enter Update Status (true/false)")

        input_layout.addWidget(QLabel("Rider ID:"), 0, 0)
        input_layout.addWidget(self.rider_id_input, 0, 1)
        input_layout.addWidget(QLabel("Update Status:"), 1, 0)
        input_layout.addWidget(self.rider_update_input, 1, 1)

        # Submit Button
        self.rider_submit_button = QPushButton("Submit")
        self.rider_submit_button.clicked.connect(self.rider_api_call)

        # Output Section
        self.rider_output_area = QTextEdit()
        self.rider_output_area.setReadOnly(True)

        # Assemble Layout
        layout.addLayout(input_layout)
        layout.addWidget(self.rider_submit_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.rider_output_area)

        rider_tab.setLayout(layout)
        return rider_tab

    def driver_api_call(self):
        """API call for the Driver tab."""
        driver_id = self.driver_id_input.text()
        update_status = self.driver_update_input.text()

        if not driver_id or not update_status:
            self.driver_output_area.append("Please fill in all fields.\n")
            return

        try:
            # Replace with your Driver API endpoint
            url = "http://localhost:8000/driver/process"
            params = {"id": driver_id, "update": update_status}
            response = requests.get(url, params=params)

            if response.status_code == 200:
                self.driver_output_area.append(f"Response:\n{response.json()}\n")
            else:
                self.driver_output_area.append(f"Error: {response.status_code}\n{response.text}\n")
        except Exception as e:
            self.driver_output_area.append(f"Exception occurred: {e}\n")

    def rider_api_call(self):
        """API call for the Rider tab."""
        rider_id = self.rider_id_input.text()
        update_status = self.rider_update_input.text()

        if not rider_id or not update_status:
            self.rider_output_area.append("Please fill in all fields.\n")
            return

        try:
            # Replace with your Rider API endpoint
            url = "http://localhost:8000/rider/processsing"
            params = {"id": rider_id, "update": update_status}
            response = requests.get(url, params=params)

            if response.status_code == 200:
                self.rider_output_area.append(f"Response:\n{response.json()}\n")
            else:
                self.rider_output_area.append(f"Error: {response.status_code}\n{response.text}\n")
        except Exception as e:
            self.rider_output_area.append(f"Exception occurred: {e}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CombinedApp()
    window.show()
    sys.exit(app.exec_())

