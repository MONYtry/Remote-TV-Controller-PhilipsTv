# Philips SmartHome Controller

A Python-based Smart Home controller for Philips TVs that allows remote control and status monitoring over the local network.

## 📌 About the Project

Philips SmartHome Controller is a Python application that communicates with a Philips TV through its network API.

The goal of this project was to explore:
- Network communication with IoT devices
- API authentication
- Smart Home automation
- Secure handling of configuration data

The application allows users to monitor and control their TV without using the physical remote control.

---

## ✨ Features

✅ Check current TV power status  
✅ Turn TV on  
✅ Turn TV off  
✅ Toggle TV power state  
✅ Secure configuration using environment variables  
✅ Local network communication  

---

## 🛠️ Technologies

- **Python 3**
- **Philips TV API**
- **python-dotenv**
- **Network communication**
- **Git & GitHub**

---

## 📂 Project Structure


Philips-TV-Controller/
│
├── smarthome.py # Main application
├── Config.env.example # Example configuration
├── .gitignore # Ignored files
└── README.md # Documentation


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/Philips-TV-Controller.git
2. Install dependencies
pip install -r requirements.txt
3. Configure environment variables

Create a file called:

Config.env

Add your own configuration:

TV_IP=your_tv_ip
TV_CLIENT_ID=your_client_id
TV_TOKEN=your_token

⚠️ Never upload your real credentials to GitHub.

▶️ Usage

Run the application:

python smarthome.py

The program will connect to the configured Philips TV and display the current power status.

Example:

Status: nicht in benutzung (Info: False)
🔐 Security

Sensitive information such as:

Authentication tokens
Device credentials
Local IP addresses

are stored outside the source code using environment variables.

🚀 Future Improvements

Possible future features:

 Graphical User Interface (GUI)
 Multiple device support
 Web dashboard
 Voice assistant integration
 Automation rules
 Logging system
👨‍💻 Author

Created by Leon

This project was built to improve my skills in:

Python development
Networking
IoT systems
Software organization
