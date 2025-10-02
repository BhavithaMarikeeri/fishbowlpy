# 🐠 fishbowlpy

A Python library for interacting with the Fishbowl App API - access bowls, posts, and comments programmatically.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/fishbowlpy.svg)](https://badge.fury.io/py/fishbowlpy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 What is fishbowlpy?

**fishbowlpy** is a Python library that provides a simple and intuitive interface to interact with [Fishbowl App](https://www.fishbowlapp.com). Whether you're building automation tools, analyzing community discussions, or creating integrations, fishbowlpy makes it easy to access Fishbowl's content programmatically.

### What is Fishbowl App?

Fishbowl App is an anonymous professional networking platform (a Glassdoor initiative) where professionals can:
- 💼 Discuss workplace insights anonymously
- 🤝 Request and offer job referrals
- 💡 Share career advice and experiences
- 🗣️ Engage in industry-specific conversations

Visit [fishbowlapp.com](https://www.fishbowlapp.com) to learn more.

---

## ✨ Features

- 🔐 **Easy Authentication** - Simple login interface
- 🎯 **Bowl Access** - Fetch posts from specific professional communities (bowls)
- 📝 **Post Retrieval** - Get posts with full content and metadata
- 💬 **Comment Access** - Read comments and discussions
- 🚀 **Lightweight** - Minimal dependencies, fast performance
- 📚 **Well Documented** - Comprehensive docs and examples

---

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Install from PyPI

```bash
pip install fishbowlpy
```

### Install from Source

```bash
git clone https://github.com/mukulbindal/fishbowlpy.git
cd fishbowlpy
pip install -e .
```

---

## 🚀 Quick Start

### Basic Example

```python
from fishbowlpy.fishbowlclient import FishBowlClient

# Initialize the client
client = FishBowlClient()

# Fetch posts from a specific bowl
posts = client.get_posts(bowl_name='tech-india')

# Display posts
for post in posts:
    print(f"Post ID: {post['id']}")
    print(f"Content: {post['content']}")
    print("-" * 50)
```

### Fetching Posts from Multiple Bowls

```python
from fishbowlpy.fishbowlclient import FishBowlClient

client = FishBowlClient()

# List of bowls to fetch from
bowls = ['tech-india', 'consulting', 'product-management']

for bowl_name in bowls:
    print(f"\n=== Posts from {bowl_name} ===")
    posts = client.get_posts(bowl_name=bowl_name)
    print(f"Found {len(posts)} posts")
```

### Working with Post Details

```python
from fishbowlpy.fishbowlclient import FishBowlClient

client = FishBowlClient()
posts = client.get_posts(bowl_name='tech-india')

# Access post information
for post in posts[:5]:  # First 5 posts
    print(f"Title: {post.get('title', 'No title')}")
    print(f"Author: {post.get('author', 'Anonymous')}")
    print(f"Likes: {post.get('likes', 0)}")
    print(f"Comments: {post.get('comment_count', 0)}")
    print()
```

---

## 📚 Documentation

Full API documentation is available at: **[https://mukulbindal.github.io/fishbowlpy/](https://mukulbindal.github.io/fishbowlpy/)**

### Key Methods

| Method | Description | Parameters |
|--------|-------------|------------|
| `FishBowlClient()` | Initialize the client | None |
| `get_posts(bowl_name)` | Fetch posts from a bowl | `bowl_name` (str): Name of the bowl |
| `get_comments(post_id)` | Get comments for a post | `post_id` (str): ID of the post |

---

## 🤝 Contributing

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### How to Contribute

1. **Explore Issues**: Check the [Issues](https://github.com/mukulbindal/fishbowlpy/issues) tab for open tasks
2. **Propose Features**: Have an idea? Create a new issue to discuss it
3. **Follow Guidelines**: Read our contribution guidelines before submitting PRs
4. **Submit PR**: Create a pull request with your changes

### Contribution Guidelines

- Write clear, descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Follow existing code style and conventions
- One feature/fix per pull request

---

## 🙏 Contributors

Special thanks to everyone who has contributed to this project:

- [@jaymeklein](https://github.com/jaymeklein) - Jayme Klein

**Want to see your name here?** Contribute to the project!

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'fishbowlpy'`
- **Solution**: Ensure you've installed the package: `pip install fishbowlpy`

**Issue**: Connection errors or timeouts
- **Solution**: Check your internet connection and verify Fishbowl App is accessible

**Issue**: Empty results from `get_posts()`
- **Solution**: Verify the bowl name is correct and publicly accessible

### Getting Help

- 📖 Check the [Documentation](https://mukulbindal.github.io/fishbowlpy/)
- 🐛 Report bugs in [Issues](https://github.com/mukulbindal/fishbowlpy/issues)
- 💬 Ask questions in [Discussions](https://github.com/mukulbindal/fishbowlpy/discussions)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Maintainer**: Mukul Bindal

- 📧 Email: mukulbindal170299@gmail.com
- 🐙 GitHub: [@mukulbindal](https://github.com/mukulbindal)

---

## ⭐ Show Your Support

If you find fishbowlpy useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing to the codebase

---

**Made with ❤️ by the open-source community**