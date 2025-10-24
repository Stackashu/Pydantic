# Pydantic Project

This project demonstrates Pydantic usage for data validation and settings management.

## Setup

1. Make sure Python is installed on your system
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Running Examples

```bash
python examples/basic_models.py
python examples/settings_example.py
python examples/advanced_models.py
```

## Project Structure

- `examples/` - Example Pydantic models and usage
  - `basic_models.py` - Basic Pydantic model examples
  - `settings_example.py` - Settings management with pydantic-settings
  - `advanced_models.py` - Advanced validation and relationships
- `requirements.txt` - Python dependencies
- `env.example` - Environment variables template
- `README.md` - This file

## Features Demonstrated

### Basic Models (`basic_models.py`)
- Field validation with constraints
- Custom validators
- Enum usage
- JSON serialization
- Error handling

### Settings Management (`settings_example.py`)
- Environment variable loading
- Nested settings configuration
- Environment prefixes
- .env file support with python-dotenv

### Advanced Models (`advanced_models.py`)
- Complex validation rules
- Root validators
- Model relationships
- Custom methods
- Date validation
- Regex validation

## Environment Variables

Copy `env.example` to `.env` and customize the values for your environment.
