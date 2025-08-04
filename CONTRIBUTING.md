# Contributing to Reflex Web

Thank you for your interest in contributing to the Reflex website! This repository contains the source code for [reflex.dev](https://reflex.dev), the official website for the Reflex web framework.

## Getting Started

### Prerequisites

- Python 3.10+
- Git

### Local Development Setup

1. **Fork the repository**
   ```bash
   # Fork the repo on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/reflex-web.git
   cd reflex-web
   ```

2. **Set up your development environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   python -m pip install .
   ```

3. **Run the development server**
   ```bash
   reflex run
   ```
   
   The website will be available at `http://localhost:3000/`

## Making Contributions

### Types of Contributions

We welcome contributions in the following areas:

- **Content Updates**: Blog posts, documentation improvements, examples
- **Bug Fixes**: Fixing issues with the website functionality
- **UI/UX Improvements**: Enhancing the user experience and design
- **Performance Optimizations**: Making the site faster and more efficient
- **Accessibility**: Improving accessibility features

### Before You Start

1. Check the [Issues](https://github.com/reflex-dev/reflex-web/issues) to see if someone is already working on what you want to contribute
2. For significant changes, please open an issue first to discuss your proposed changes
3. Make sure your contribution aligns with the project's goals and style

### Development Workflow

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style and conventions
   - Ensure your changes work locally by testing with `reflex run`

3. **Test your changes**
   ```bash
   # Run any existing tests
   python -m pytest tests/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add meaningful commit message"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Provide a clear description of your changes

### Code Style and Standards

- Follow Python PEP 8 style guidelines
- Use meaningful variable and function names
- Write clear, concise commit messages
- Ensure your code is well-documented
- Keep changes focused and atomic

### Content Guidelines

When contributing content (blog posts, documentation, examples):

- Use clear, concise language
- Include relevant examples and code snippets
- Ensure accuracy of technical information
- Follow the existing content structure and style
- Include appropriate metadata and frontmatter where applicable

## Pull Request Guidelines

### Before Submitting

- [ ] Test your changes locally with `reflex run`
- [ ] Ensure no broken links or missing assets
- [ ] Check that your changes are responsive on different screen sizes
- [ ] Verify that your changes don't break existing functionality

### Pull Request Description

Please include:

- A clear description of what your PR does
- Screenshots/GIFs for UI changes
- Any breaking changes or migration notes
- Related issue numbers (if applicable)

## Getting Help

- **Questions**: Open a [Discussion](https://github.com/reflex-dev/reflex-web/discussions)
- **Bugs**: Open an [Issue](https://github.com/reflex-dev/reflex-web/issues)
- **Community**: Join the [Reflex Discord](https://discord.gg/T5WSbC2YtQ)

## Project Structure

```
reflex-web/
├── assets/          # Static assets (images, fonts, etc.)
├── blog/           # Blog posts and related content
├── docs/           # Documentation files
├── pcweb/          # Main website code
├── scripts/        # Build and deployment scripts
├── tests/          # Test files
└── README.md
```

## Recognition

Contributors will be recognized in:
- The project's contributor list
- Release notes for significant contributions
- The Reflex community Discord

## Code of Conduct

This project follows the Reflex community guidelines. Please be respectful and constructive in all interactions.

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to Reflex Web! 🚀