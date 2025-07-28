# Project Structure

```
BlockChainProject/
├── 📁 src/                          # Source code modules
│   ├── __init__.py                  # Package initialization
│   ├── analyzer.py                  # Core analysis engine
│   ├── data_loader.py              # Data loading and cleaning
│   ├── visualizer.py               # Visualization creation
│   └── utils.py                    # Helper functions
│
├── 📁 data/                         # Data files
│   ├── historical_data.csv         # Trading data from Hyperliquid
│   └── fear_greed_index.csv        # Fear/Greed Index data
│
├── 📁 outputs/                      # Generated outputs
│   ├── .gitkeep                    # Keeps directory in git
│   └── *.png                       # Generated charts
│
├── 📁 examples/                     # Usage examples
│   └── basic_usage.py              # Example implementations
│
├── 📄 main.py                       # Main execution script
├── 📄 config.py                     # Configuration settings
├── 📄 requirements.txt              # Python dependencies
├── 📄 setup.py                      # Package setup
├── 📄 README.md                     # Project documentation
├── 📄 .gitignore                    # Git ignore rules
└── 📄 PROJECT_STRUCTURE.md          # This file
```

## Key Files Description

### Core Modules (`src/`)
- **`analyzer.py`**: Main analysis engine with `BitcoinSentimentAnalyzer` class
- **`data_loader.py`**: Handles loading and cleaning of CSV data files
- **`visualizer.py`**: Creates all charts and visualizations
- **`utils.py`**: Common utility functions and helpers

### Configuration
- **`config.py`**: Centralized configuration for paths, colors, and settings
- **`requirements.txt`**: Python package dependencies

### Usage
- **`main.py`**: Primary script to run complete analysis
- **`examples/basic_usage.py`**: Demonstrates different usage patterns

### Data
- **`data/`**: Contains the CSV files for analysis
- **`outputs/`**: Generated charts and reports are saved here

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run analysis:**
   ```bash
   python main.py
   ```

3. **View results:**
   - Check console output for insights
   - View generated charts in `outputs/` directory

## Clean Architecture Benefits

✅ **Modular**: Each component has a single responsibility  
✅ **Reusable**: Components can be used independently  
✅ **Maintainable**: Easy to modify and extend  
✅ **Testable**: Each module can be tested separately  
✅ **Professional**: Follows Python best practices