# Contributing to HexHub

Thank you for your interest in contributing to HexHub! This document provides guidelines and instructions for contributing.

## 🌟 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as the issue might already exist.

**When creating a bug report, include:**
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Your OS and environment details
- Any relevant screenshots or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:
- A clear description of the proposed feature
- Why this feature would be useful
- Any examples of how it should work

### Adding New Drivers

This is the most common contribution! Follow these steps:

1. **Fork the repository**
2. **Edit `data/drivers.json`**:
   - Follow the schema in `data/drivers_schema.json`
   - Include all required fields
   - Provide accurate hardware IDs
   - Test installation commands if possible

3. **Run the README generator**:
   ```bash
   python scripts/generate_readme.py
   ```

4. **Verify your changes**:
   ```bash
   python -m json.tool data/drivers.json > /dev/null && echo "Valid JSON"
   ```

5. **Commit and create a Pull Request**

### Improving Documentation

Documentation improvements are always welcome:
- Fix typos
- Clarify unclear sections
- Add examples
- Translate content (if applicable)

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Run `python scripts/generate_readme.py` to update generated content
- [ ] Validate JSON files with `python -m json.tool <file>.json`
- [ ] Test your changes locally
- [ ] Update documentation if needed
- [ ] Follow the code style used in the project

### PR Title Format

Use clear, descriptive titles:
- ✅ `Add driver for Realtek RTL8822BE Wi-Fi adapter`
- ✅ `Fix broken download link for NVIDIA drivers`
- ❌ `Update file`

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New driver entry
- [ ] Bug fix
- [ ] Documentation update
- [ ] Feature addition
- [ ] Other (please describe)

## Testing
- [ ] JSON validated
- [ ] README regenerated
- [ ] Commands tested (if applicable)

## Related Issues
Closes #XXX (if applicable)
```

## 💻 Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/HexHub.git
cd HexHub

# Create a branch
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Validate and generate
python -m json.tool data/drivers.json > /dev/null
python scripts/generate_readme.py

# Commit
git commit -m "Your commit message"
git push origin feature/your-feature-name
```

## 📜 Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## 🏆 Recognition

Contributors will be recognized in:
- The README.md contributors section
- GitHub Contributors graph
- Release notes (for significant contributions)

## ❓ Questions?

Feel free to open an issue with the "Question" label if you have any questions about contributing!

---

**Thank you for making HexHub better! 🎉**
