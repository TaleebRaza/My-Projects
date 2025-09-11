# ➖➖➖➖➖➖➖➖➖➖➖ Importing Modules ➖➖➖➖➖➖➖➖➖➖➖
import requests
import sys
import os
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from habit_tracker_GUI import Ui_MainWindow
from load_data import DataLoader


# ➖➖➖➖➖➖➖➖➖➖➖ Helper Function ➖➖➖➖➖➖➖➖➖➖➖
def resource_path(relative_path):
    """Get the absolute path to the bundled resource file."""
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # In a normal Python script, use the current directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_response(url, json, header=None):
    """
    Sends a POST request and returns a string with the status or error message.

    Parameters:
        url (str): The URL endpoint to send the POST request to.
        json (dict): The data to be sent in the request body.
        header (dict, optional): The headers for the request.

    Returns:
        str: The response message, including error handling if necessary.
    """
    response_message = ""
    response_data = None

    try:
        # Sending POST request
        response = requests.post(url=url, json=json, headers=header, timeout=10)  # Added timeout

        # Raise an exception for HTTP error responses (non-2xx status codes)
        response.raise_for_status()

        try:
            # No need to assign response.text here, since no JSON parsing is done
            response_message = "Request successful."
        except ValueError:
            response_message = f"Failed to parse response as JSON. Raw response: {response.text}"

    # Specific exception handling for different request errors
    except requests.exceptions.Timeout as e:
        response_message = f"Request timed out: {e}"
    except requests.exceptions.TooManyRedirects as e:
        response_message = f"Too many redirects: {e}"
    except requests.exceptions.ConnectionError as e:
        response_message = f"Network error: {e}"
    except requests.exceptions.HTTPError as e:
        # Catch HTTP errors like 400, 401, 500, etc.
        response_message = e.response.json().get("message", "Unknown error")

        if e.response.status_code == 400:
            response_message += "\nBad Request. Please check the request parameters."
        elif e.response.status_code == 401:
            response_message += "\nAuthentication failed (401 Unauthorized)"
        elif e.response.status_code == 403:
            response_message += "\nForbidden access (403)"
        elif e.response.status_code == 404:
            response_message += "\nEndpoint not found (404)"
        elif e.response.status_code == 500:
            response_message += "\nInternal server error (500)"
    except requests.exceptions.RequestException as e:
        response_message = f"Request failed: {e}"
    except Exception as e:
        response_message = f"An unexpected error occurred: {e}"

    return response_message


class HabitTracker(Ui_MainWindow, QMainWindow):
    PIXELA_USER_API_ENDPOINT = "https://pixe.la/v1/users"

    def __init__(self):
        """
        Initializes the HabitTracker UI and sets up various widgets, buttons, and actions.
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pixela Graph Maker")
        # 🟢 Use the helper function to set the window icon
        self.setWindowIcon(QIcon(resource_path("logo.png")))

        self.response_output_box.setText("Please Read Instructions carefully."
                                         "\n1. Add/Create Account."
                                         "\n2. Add/Create a graph to update"
                                         "\n3. Use the date and quantity slider to update the graph with a value."
                                         "\n\nNote: Read the result of your actions here.")

        # Initialize variables
        self.username = ""
        self.token = ""
        # 🟢 The DataLoader.py is also a data file, so it needs to be imported using the resource_path
        # You would need to update the `load_data.py` file to handle file paths properly as well,
        # but for this example, we'll assume it doesn't try to open external files itself.
        self.data_loader = DataLoader()

        # Attempt to load and apply UI stylesheet
        try:
            # 🟢 Use the helper function to open the stylesheet file
            with open(file=resource_path("ui_stylesheet.qss"), mode="r") as stylesheetfile:
                stylesheet = stylesheetfile.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print("No stylesheet found")

        # Initial states for account and graph creation
        self.account_authenticated = False
        self.graph_created = False

        # Set up widget states and connect buttons
        self.authenticate_widgets()
        self.graph_widgets()
        self.graph_data_widgets()
        self.load_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.connect_buttons()

        self.graph_config = None

    def connect_buttons(self):
        """
        Connects button click events to their corresponding functions.
        """
        self.account_button.clicked.connect(self.get_account)
        self.edit_account_button.clicked.connect(self.enable_widgets)
        self.graph_detail_button.clicked.connect(self.get_graph)
        self.save_button.clicked.connect(self.save_data)
        self.load_button.clicked.connect(self.load_data)
        self.update_graph_button.clicked.connect(self.update_graph)

    def enable_widgets(self):
        """
        Enables the widgets for account editing when 'Edit Account Details' button is clicked.
        """
        sender = self.sender()
        button = sender.text()

        if button == "Edit Account Detials":
            self.authenticate_widgets(enable=True)
            self.graph_widgets()
            self.graph_data_widgets()
            self.load_button.setEnabled(False)
            self.save_button.setEnabled(False)

    def authenticate_widgets(self, enable: bool = True):
        """
        Enables or disables the authentication widgets.

        Parameters:
            enable (bool): True to enable widgets, False to disable them.
        """
        self.username_textbox.setEnabled(enable)
        self.token_textbox.setEnabled(enable)
        self.account_button.setEnabled(enable)

    def graph_widgets(self, enable: bool = False):
        """
        Enables or disables the graph-related widgets.

        Parameters:
            enable (bool): True to enable widgets, False to disable them.
        """
        self.colors_dropdown.setEnabled(enable)
        self.graph_name_text.setEnabled(enable)
        self.graph_unit_text.setEnabled(enable)
        self.graph_detail_button.setEnabled(enable)
        self.int_type.setEnabled(enable)
        self.float_type.setEnabled(enable)
        self.graph_id_box.setEnabled(enable)

    def graph_data_widgets(self, enable: bool = False):
        """
        Enables or disables the graph data-related widgets.

        Parameters:
            enable (bool): True to enable widgets, False to disable them.
        """
        self.date_widget.setEnabled(enable)
        self.quantity.setEnabled(enable)
        self.update_graph_button.setEnabled(enable)

    def save_data(self):
        """
        Saves the current user's graph details and password to the file.
        """
        data = {
            "password": self.token,
            "graphDetails": {
                "id": self.graph_id,
                "name": self.graph_name_text.text(),
                "unit": self.graph_unit_text.text(),
                "type": "int" if self.int_type.isChecked() else "float",
                "color": self.colors_dropdown.currentText()
            }
        }

        # Update DataLoader object with new user data
        self.data_loader.username = self.username
        self.data_loader.data[self.data_loader.username] = data
        self.data_loader.save_data()

    def load_data(self):
        """
        Loads the user's graph data from the file and updates the UI fields.
        """
        try:
            data = self.data_loader.load_user_data(self.username)["graphDetails"]
            self.graph_name_text.setText(data["name"])
            self.graph_id_box.setText(data["id"])
            self.graph_unit_text.setText(data["unit"])
            self.int_type.setChecked(True) if data["type"] == "int" else self.float_type.setChecked(True)

            # Set the color dropdown to the saved color
            index = self.colors_dropdown.findText(data["color"])
            self.colors_dropdown.setCurrentIndex(index)
        except TypeError:
            self.response_output_box.setHtml(f"No Data To Load. Please input data in the graph fields and save again.")

    def get_account(self):
        """
        Gets the account information (username and token) from the UI and authenticates the user.
        """
        self.username = self.username_textbox.text()
        self.token = self.token_textbox.text()

        user_parameters = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

        # Set header for authentication
        self.header = {"X-USER-TOKEN": self.token}

        # Make the authentication request
        pixela_response_text = get_response(url=self.PIXELA_USER_API_ENDPOINT, json=user_parameters)

        if "already exist" in pixela_response_text.lower() or "successful" in pixela_response_text.lower():
            self.response_output_box.setHtml(f"{pixela_response_text} Click below to visit your account<br>"
                                             f'<a href="https://pixe.la/@{self.username}" style="color: green; font-size: 20px; font-weight: bold; ">https://pixe.la/@{self.username}</a>')
            self.graph_widgets(enable=True)
            self.authenticate_widgets(enable=False)
            self.load_button.setEnabled(True)
        else:
            self.response_output_box.setHtml(pixela_response_text)

            # Store user data in DataLoader
            self.data_loader.username = self.username
            self.data_loader.token = self.token

    def get_graph(self):
        """
        Retrieves the graph details from the UI, creates the graph, and saves the data.
        """
        color = self.colors_dropdown.currentText()
        graph_name = self.graph_name_text.text()
        unit = self.graph_unit_text.text()
        unit_type = "int" if self.int_type.isChecked() else "float"
        self.graph_id = (graph_name + str(randint(1, 10))) if len(
            self.graph_id_box.text()) <= 1 else self.graph_id_box.text()

        graph_config = {
            "id": self.graph_id,
            "name": graph_name,
            "unit": unit,
            "type": unit_type,
            "color": color
        }

        # API endpoint to create the graph
        graph_endpoint = f"{self.PIXELA_USER_API_ENDPOINT}/{self.username}/graphs"

        # Send the request to create the graph
        response = get_response(url=graph_endpoint, json=graph_config, header=self.header)

        if "already exist" in response.lower() or "successful" in response.lower():
            self.response_output_box.setHtml(f"{response}. Please update the graph or visit using the link below<br>"
                                             f'<a href="{graph_endpoint}/{graph_config["id"]}" style="color: green; font-size: 20px; font-weight: bold;" >{graph_endpoint}/{graph_config["id"]}</a>')

            # Enable graph data widgets
            self.graph_data_widgets(enable=True)
            self.graph_widgets(enable=False)
            self.save_button.setEnabled(True)
        else:
            self.response_output_box.setHtml(response)

        # Store graph data in DataLoader
        self.data_loader.graph_data = graph_config


    def update_graph(self):
        """
        Updates the graph data (quantity and date) for the user.
        """
        update_endpoint = f"{self.PIXELA_USER_API_ENDPOINT}/{self.username}/graphs/{self.graph_id}"

        # Prepare update data
        date = self.date_widget.date().toString("yyyyMMdd")
        quantity = str(self.quantity.value())

        update_parameters = {
            "date": date,
            "quantity": quantity
        }

        # Send the request to update the graph
        response = get_response(url=update_endpoint, json=update_parameters, header=self.header)

        self.response_output_box.setHtml(f"{response}. Click Below to view<br>"
                                         f'<a href="{update_endpoint}" style="color: green; font-size: 20px; font-weight: bold;" >{update_endpoint}</a>')


# ➖➖➖➖➖➖➖ Main Execution Block ➖➖➖➖➖➖➖
if __name__ == '__main__':
    # Create the application and window
    app = QApplication([])

    # Instantiate the HabitTracker class
    window = HabitTracker()


    # Show the window
    window.show()

    # Start the application's event loop
    app.exec()