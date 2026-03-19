# Configuration Guide

## Environment Variables

All configuration is managed through environment variables. Create a `.env` file in the project root.

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `postgresql://user:pass@localhost:5432/db` |
| `API_KEY` | API authentication key | `sk-abc123...` |
| `SECRET_KEY` | Application secret for signing | `your-random-secret-key` |

### Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | `false` | Enable debug mode |
| `LOG_LEVEL` | `INFO` | Logging verbosity: DEBUG, INFO, WARNING, ERROR |
| `PORT` | `8000` | Server port |
| `WORKERS` | `4` | Number of worker processes |
| `CACHE_TTL` | `3600` | Cache time-to-live in seconds |
| `MAX_CONNECTIONS` | `100` | Database connection pool size |

## Configuration Files

### config.yaml

```yaml
app:
  name: "My Application"
  version: "1.0.0"

database:
  pool_size: 10
  timeout: 30

cache:
  backend: "redis"
  host: "localhost"
  port: 6379

logging:
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: "logs/app.log"
```

### Loading Configuration

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
```

## Environment-Specific Settings

### Development
```
DEBUG=true
LOG_LEVEL=DEBUG
DATABASE_URL=postgresql://dev:dev@localhost:5432/dev_db
```

### Production
```
DEBUG=false
LOG_LEVEL=WARNING
DATABASE_URL=postgresql://prod:secure@prod-db:5432/prod_db
WORKERS=8
```

## Secrets Management

For production, use a secrets manager instead of `.env` files:

- AWS Secrets Manager
- HashiCorp Vault
- Google Secret Manager
- Azure Key Vault

Never commit secrets to version control.
