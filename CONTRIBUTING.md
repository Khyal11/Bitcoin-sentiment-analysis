# Contributing to Bitcoin Sentiment Analysis Project

Thank you for your interest in contributing to this project! We welcome contributions from the community.

## 🚀 How to Contribute

### 1. Fork the Repository
- Click the "Fork" button at the top right of the repository page
- Clone your fork locally:
  ```bash
  git clone https://github.com/yourusername/bitcoin-sentiment-analysis.git
  cd bitcoin-sentiment-analysis
  ```

### 2. Set Up Development Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests to ensure everything works
python main.py
```

### 3. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
- Write clean, documented code
- Follow Python PEP 8 style guidelines
- Add comments for complex logic
- Update documentation if needed

### 5. Test Your Changes
- Ensure your code runs without errors
- Test with sample data
- Verify visualizations generate correctly

### 6. Commit Your Changes
```bash
git add .
git commit -m "Add: Brief description of your changes"
```

### 7. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```
Then create a Pull Request on GitHub.

## 🎯 Areas for Contribution

### Code Improvements
- **Performance optimization**
- **Additional analysis metrics**
- **New visualization types**
- **Enhanced error handling**
- **Code refactoring**

### Documentation
- **API documentation**
- **Tutorial improvements**
- **Example additions**
- **README enhancements**

### Features
- **Additional data sources**
- **Real-time data integration**
- **Machine learning models**
- **Web interface**
- **API endpoints**

## 📋 Code Style Guidelines

### Python Code Style
- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Example:
```python
def calculate_sentiment_performance(data: pd.DataFrame, 
                                  sentiment_column: str = 'classification') -> dict:
    """
    Calculate performance metrics by sentiment category.
    
    Args:
        data: DataFrame containing trading and sentiment data
        sentiment_column: Column name containing sentiment classifications
        
    Returns:
        Dictionary with performance metrics by sentiment
    """
    # Implementation here
    pass
```

### Commit Message Format
- Use clear, descriptive commit messages
- Start with action verb (Add, Fix, Update, Remove)
- Keep first line under 50 characters
- Add detailed description if needed

Examples:
```
Add: New correlation analysis function
Fix: Data loading error for missing timestamps
Update: Visualization color scheme for better accessibility
```

## 🐛 Reporting Issues

### Bug Reports
When reporting bugs, please include:
- **Description**: Clear description of the issue
- **Steps to reproduce**: Detailed steps to recreate the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: Python version, OS, package versions
- **Data**: Sample data if relevant (anonymized)

### Feature Requests
For feature requests, please include:
- **Description**: Clear description of the feature
- **Use case**: Why this feature would be useful
- **Implementation ideas**: Any thoughts on implementation
- **Examples**: Similar features in other tools

## 🔍 Code Review Process

### What We Look For
- **Functionality**: Does the code work as intended?
- **Code quality**: Is it clean, readable, and well-structured?
- **Documentation**: Are changes properly documented?
- **Testing**: Have changes been tested?
- **Performance**: Does it maintain or improve performance?

### Review Timeline
- Initial review within 48 hours
- Feedback and discussion as needed
- Final approval and merge

## 📚 Resources

### Documentation
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

### Project Resources
- [Project Structure](PROJECT_STRUCTURE.md)
- [Usage Examples](examples/basic_usage.py)
- [Configuration Guide](config.py)

## 🤝 Community Guidelines

### Be Respectful
- Use welcoming and inclusive language
- Respect different viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Be Collaborative
- Help others learn and grow
- Share knowledge and resources
- Provide constructive feedback
- Support fellow contributors

## 📞 Getting Help

If you need help with contributing:
- Check existing issues and discussions
- Create a new issue with the "question" label
- Reach out to maintainers
- Join community discussions

## 🎉 Recognition

Contributors will be:
- Listed in the project contributors
- Mentioned in release notes for significant contributions
- Invited to join the core team for outstanding contributions

Thank you for contributing to the Bitcoin Sentiment Analysis Project! 🚀