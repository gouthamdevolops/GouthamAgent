# Contributing Guidelines

Thank you for your interest in contributing to **GouthamAgent**! We welcome bug fixes, documentation improvements, unit tests, and feature enhancements.

To keep the repository clean and maintainable, please follow these guidelines:

---

## 🛠️ Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gouthamdevolops/GouthamAgent.git
   cd GouthamAgent
   ```
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Ensure Docker is running**:
   The execution sandbox utilizes Docker. Pull the required image:
   ```bash
   docker pull python-data:3.12
   ```

---

## 🧪 Testing Guidelines

Before opening a pull request, verify that all unit tests pass:
```bash
python -m unittest discover tests/
```

If you add new features (e.g., helper prompt builders or sanitization rules), write corresponding tests in the `tests/` directory.

---

## 🎨 Style & Formatting

We use **Ruff** for linting and formatting. You can run checks locally:
```bash
ruff check .
```

Please ensure:
- Variables and function arguments are fully type-hinted.
- Code blocks contain descriptive comments.
- No secrets or API credentials (like `.env` files) are committed.

---

## 📥 Pull Request Process

1. Fork the repo and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit with descriptive messages.
3. Open a Pull Request referencing the Issue it addresses.
4. Ensure the GitHub Actions CI suite passes successfully.
