# Red Team Task Automator 🤖💻

A Python-based automation tool that uses OpenAI's GPT API to suggest command-line techniques, tools, and methodologies for red team operations like enumeration, privilege escalation, lateral movement, and more.

---

## 🔥 Features

- Accepts red team scenarios as input
- Uses OpenAI's GPT API to generate relevant commands
- Helps with reconnaissance, exploitation, post-exploitation
- Simple CLI interface for fast suggestions
- Great for learning or speeding up red team workflows

---

## 📁 Project Structure

```
red-team-automator/
├── red_team_automator.py
├── requirements.txt
├── README.md
└── .env (optional, to store your API key)
```

---

## 🛠️ Installation

Clone the repository and set up your Python environment:

```bash
git clone https://github.com/your-username/red-team-automator.git
cd red-team-automator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📦 Requirements

- Python 3.7+
- openai
- dotenv (optional, if using `.env` file)

To install manually:

```bash
pip install openai python-dotenv
```

---

## 🔑 API Key Setup

You need an OpenAI API key to use this tool.

### Option 1: Set it in your terminal session

**Linux/macOS:**
```bash
export OPENAI_API_KEY="your-api-key"
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-api-key"
```

### Option 2: Store it in a `.env` file (optional)

Create a `.env` file in the same directory and add:

```
OPENAI_API_KEY=your-api-key
```

---

## ⚙️ Usage

```bash
python red_team_automator.py
```

You'll be prompted to enter a red team task:

```
Enter red team task or scenario: Active Directory enumeration
```

Example output:

```
Suggested commands:
- nmap -p 389,636,3268,3269 --script ldap* <target>
- ldapsearch -x -h <DC_IP> -b "dc=example,dc=com"
- Use tools: BloodHound, SharpHound
```

---

## 📸 Screenshot (Optional)

> *(You can add a screenshot of terminal usage here if you'd like)*

---

## ⚠️ Note

- This tool **does not execute commands**, it only provides suggestions.
- Make sure to follow legal and ethical guidelines during real-world usage.

---

## 🧾 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

- GitHub: [@muuhsi](https://github.com/muuhsi)
