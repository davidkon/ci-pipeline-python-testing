
# Continuous Integration Pipeline with Automated Tests

## Project Overview

This project demonstrates a robust Continuous Integration (CI) pipeline for a Python application using automated testing and static code analysis. It integrates backend unit tests, frontend UI tests, and API tests into a seamless workflow triggered on every push or pull request to the main branch. The pipeline is implemented using GitHub Actions, showcasing modern QA automation practices for full-stack Python projects.

---

## Repository Structure

```
/ci-pipeline-python-testing
│
├── /src
│   └── app.py               # Dummy Flask app
│
├── /tests
│   ├── test_backend.py      # Backend tests
│   ├── test_frontend.py     # Frontend tests (API/UI)
│   └── test_api.py          # API tests
│
├── pyproject.toml           # Project metadata and dependencies
├── requirements.txt         # (Optional) For legacy or quick installs
├── .gitignore               # Ignore venvs, caches, etc.
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow
└── README.md                # Project documentation
```

---

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or newer
- [pip](https://pip.pypa.io/en/stable/)
- (Recommended) [hatch](https://hatch.pypa.io/latest/) for modern builds

### 2. Clone the Repository

```bash
git clone https://github.com/davidkon/ci-pipeline-python-testing.git
cd ci-pipeline-python-testing
```

### 3. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install the Project and Development Dependencies

**Recommended (using `pyproject.toml`):**
```bash
pip install -e .[dev]
```
or, if using [hatch](https://hatch.pypa.io/latest/install/):
```bash
pip install hatch
hatch env create
hatch shell
```

---

## Running the Application

To start the Flask app locally:
```bash
export FLASK_APP=src/app.py
flask run
```
Or simply:
```bash
python src/app.py
```
Visit [http://localhost:5000](http://localhost:5000) to see the app.

---

## Running Tests

Run all tests with:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src --cov-report=term
```

---

## Linting

Check code style and quality:
```bash
flake8 src tests
```

---

## Continuous Integration

This project uses GitHub Actions for CI. The workflow (`.github/workflows/ci.yml`) will:

- Set up Python
- Install dependencies
- Lint the code
- Run all tests with coverage
- Upload coverage reports as artifacts

The workflow runs on every push and pull request to the `main` branch.

---

## Project Highlights

- **Modular Test Suites:** Separate tests for backend, API, and frontend.
- **Modern Packaging:** Uses `pyproject.toml` for dependencies and metadata.
- **CI/CD Ready:** Out-of-the-box GitHub Actions workflow.
- **Best Practices:** Virtual environments, code linting, and coverage reporting.

---

## Future Enhancements

- Add continuous deployment steps
- Integrate security and performance testing
- Add notification integrations (e.g., Slack, email)
- Expand test coverage and scenarios

---

## License

[MIT License](LICENSE)

---

**Happy testing!**  
If you have questions or suggestions, feel free to open an issue or pull request.

---