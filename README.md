# 📈 Trading Bot

An automated trading bot built with Python that fetches market data, analyzes trading signals, and executes trades based on predefined strategies.

## 🚀 Features

* Fetch real-time market data
* Automated buy/sell signal generation
* Trading strategy implementation
* Logging of trading activity
* Secure environment variable management using `.env`

## 🛠️ Tech Stack

* Python
* Requests
* Pandas
* dotenv

## 📂 Project Structure

```
trading_bot/
│
├── main.py          # Main bot execution file
├── strategy.py      # Trading strategy logic
├── utils.py         # Helper functions
├── logs/            # Log files
├── .env             # Environment variables (not pushed to GitHub)
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/teja836/trading_bot.git
cd trading_bot
```

Create a virtual environment:

```
python -m venv .venv
```

Activate the environment:

**Windows**

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

⚠️ Do not commit `.env` to GitHub. It should be included in `.gitignore`.

## ▶️ Running the Bot

Run the main script:

```
python main.py
```

## 📊 Logging

The bot records trading activity and errors in the `logs/` folder for monitoring and debugging.

## 🔒 Security

* Sensitive keys are stored in `.env`
* `.env` is ignored using `.gitignore`
* Never expose API keys in public repositories

## 📌 Future Improvements

* Add multiple trading strategies
* Integrate technical indicators
* Implement backtesting
* Add web dashboard for monitoring

## 👨‍💻 Author

Teja Arepalli
Aspiring Full Stack Developer

GitHub: https://github.com/teja836
