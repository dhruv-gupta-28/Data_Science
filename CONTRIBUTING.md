# Contributing to Data Science Learning Repository

Thank you for your interest in contributing to this repository! We welcome contributions from learners and educators alike.

## How to Contribute

### 1. Report Issues

If you find bugs, errors, or have suggestions for improvements:

- Create a detailed issue describing the problem
- Include relevant file paths and line numbers
- Provide context about what you were learning/doing

### 2. Add Learning Materials

We welcome new learning materials in the following ways:

#### Adding Practice Problems

- Create new files in appropriate directories
- Use the existing file format and structure
- Include docstrings explaining concepts
- Add practice problems with solutions

#### Improving Existing Content

- Fix typos or unclear explanations
- Add more examples or edge cases
- Improve code comments and documentation
- Update outdated information

#### Creating New Topics

- Propose new topics before creating extensive content
- Ensure the topic fits logically in the directory structure
- Provide comprehensive coverage from basics to advanced

### 3. Submit Pull Requests

#### Before You Start

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit with clear messages: `git commit -m "Add: descriptive message"`

#### Content Guidelines

- **Code Quality**: Follow PEP 8 style guidelines
- **Documentation**: Include docstrings and comments
- **Examples**: Provide practical, realistic examples
- **Testing**: Test code before submitting
- **Naming**: Use clear, descriptive names for functions and variables

#### File Structure

```
topic/
├── 01_basics_explanation.py        # Concepts and examples
├── 02_intermediate_concepts.py     # More advanced ideas
├── 03_advanced_applications.py     # Complex use cases
└── README.md                        # Topic-specific guide (if needed)
```

#### Commit Message Format

```
Type: Brief description (50 chars max)

Detailed explanation of changes (if needed)
- Point 1
- Point 2
```

Types: `Add`, `Fix`, `Update`, `Refactor`, `Improve`, `Doc`

### 4. Documentation Standards

#### Python Files Should Include

```python
"""
Topic Name
==========

Topics Covered:
- Concept 1
- Concept 2
- Concept 3
"""

# ============================================================================
# SECTION HEADING
# ============================================================================

# Code with clear comments
```

#### README Files Should Include

- Overview of the topic
- List of subtopics covered
- Key learning objectives
- Links to related files
- Common mistakes to avoid

### 5. Code Style Guidelines

- **Indentation**: 4 spaces (not tabs)
- **Line Length**: Max 88 characters
- **Naming**:
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
- **Comments**: Use `#` for comments, `"""` for docstrings
- **Imports**: Standard library first, then third-party, then local

Example:

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index.

    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        float: BMI value
    """
    return weight_kg / (height_m ** 2)
```

### 6. Testing Your Changes

Before submitting:

1. Run your Python files to ensure no errors
2. Check for PEP 8 compliance
3. Verify all examples work correctly
4. Review for clarity and completeness

### 7. Pull Request Checklist

- [ ] Code follows PEP 8 style guidelines
- [ ] All new code has docstrings
- [ ] Examples are tested and work
- [ ] No unnecessary files or debug code
- [ ] Changes are logically organized
- [ ] Commit messages are clear
- [ ] Updated relevant README files

### 8. Review Process

- A maintainer will review your PR within 1-2 weeks
- We may suggest changes or improvements
- Please respond to feedback promptly
- Once approved, your PR will be merged!

## Content Suggestions

### Areas We Need Help With

- [ ] More beginner-friendly examples
- [ ] Real-world applications
- [ ] Common pitfalls and how to avoid them
- [ ] Performance optimization examples
- [ ] Data science project walkthroughs
- [ ] Interview preparation materials

### Topics to Expand

- Advanced OOP patterns
- Design patterns
- System design concepts
- Performance optimizations
- Testing strategies

## Questions or Need Help?

- Review existing issues and discussions
- Check relevant README files
- Look at similar files for examples
- Open a discussion for clarification

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Acknowledge others' contributions
- Help beginners and learners
- Maintain a positive learning environment

## Recognition

All contributors will be:

- Listed in the contributors section
- Credited in relevant files
- Recognized for their contributions

Thank you for helping make this repository better for everyone! 🎓

---

**Happy Contributing!**
