# Getting Started

## Prerequisites

Before you begin, ensure you have:
- Python 3.10 or higher
- pip package manager
- Git for version control
- A code editor (VS Code recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/your-project.git
cd your-project
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Copy the example environment file and update values:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
API_KEY=your-api-key
DEBUG=true
```

### 5. Initialize Database

```bash
python manage.py db upgrade
```

## Running the Application

### Development Mode

```bash
python main.py --dev
```

The application will be available at `http://localhost:8000`.

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black .
ruff check .
```

## Project Structure

```
project/
├── src/           # Application source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration files
└── scripts/       # Utility scripts
```

## Next Steps

- Read the [Architecture Guide](architecture.md)
- Review [Best Practices](best_practices.md)
- Check the [API Reference](api_reference.md)
