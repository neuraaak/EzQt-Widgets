# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.1] - 2024-12-19

### 📚 Documentation Reorganization
- **API Documentation Structure** : Reorganized technical documentation into `docs/api/` folder
- **Improved Navigation** : Better separation between general and API documentation
- **Style Guide Integration** : Moved `STYLE_GUIDE.md` to API documentation section
- **Updated Links** : All documentation links updated to reflect new structure

### 🔄 Structural Changes
- **New API Documentation Folder** : `docs/api/` for all widget API documentation
- **Centralized Style Guide** : `docs/api/STYLE_GUIDE.md` for coding standards
- **Updated MANIFEST.in** : Reflects new documentation structure for distributions
- **Enhanced README** : Updated main documentation index with new structure

### 📁 Updated Documentation Structure
```
docs/
├── README.md                    # Main documentation index
├── api/                        # 🎯 API Documentation
│   ├── README.md              # API documentation guide
│   ├── WIDGETS_DOCUMENTATION.md
│   ├── BUTTONS_DOCUMENTATION.md
│   ├── INPUTS_DOCUMENTATION.md
│   ├── LABELS_DOCUMENTATION.md
│   ├── MISC_DOCUMENTATION.md
│   └── STYLE_GUIDE.md         # Coding standards
└── tests/                      # 🧪 Test documentation
    ├── README.md
    ├── QUICK_START_TESTS.md
    └── ...
```

### 🎯 Benefits
- **Clearer Organization** : API documentation separated from general guides
- **Better Navigation** : Intuitive structure for developers
- **Professional Standards** : Follows industry conventions for API documentation
- **Easier Maintenance** : Logical grouping of related documentation

## [2.1.0] - 2025-07-27

### 🏗️ Architecture
- **Complete Project Reorganization** : Restructured project architecture for better maintainability
- **Documentation Centralization** : Moved all documentation to `docs/` folder
- **Test Infrastructure** : Centralized test files and documentation
- **Professional Structure** : Improved project organization following best practices

### 📚 Documentation
- **New Documentation Structure** :
  - `docs/README.md` - Central documentation index
  - `docs/CHANGELOG.md` - Version history
  - `docs/STYLE_GUIDE.md` - Code style guidelines
  - `docs/QUICK_START_TESTS.md` - Quick test guide
  - `docs/tests/` - Test documentation organized by category
- **Updated Main README** : Modernized with emojis, better structure, and clear navigation
- **French Localization** : All documentation now in French for better accessibility

### 🧪 Testing Infrastructure
- **Comprehensive Test Suite** : Added 262 tests (254 passing, 8 skipped)
- **Widget Test Coverage** :
  - **Button Widgets** : 59 tests (56 pass, 3 skipped)
    - `IconButton` : 17 tests (16 pass, 1 skipped)
    - `DateButton` : 20 tests (19 pass, 1 skipped)
    - `LoaderButton` : 22 tests (21 pass, 1 skipped)
  - **Label Widgets** : 70 tests (67 pass, 3 skipped)
    - `ClickableTagLabel` : 17 tests (14 pass, 3 skipped)
    - `FramedLabel` : 15 tests ✅
    - `HoverLabel` : 20 tests ✅
    - `IndicatorLabel` : 18 tests ✅
  - **Input Widgets** : 112 tests (111 pass, 1 skipped)
    - `AutoCompleteInput` : 28 tests ✅
    - `PasswordInput` : 35 tests ✅
    - `SearchInput` : 30 tests ✅
    - `TabReplaceTextEdit` : 19 tests (18 pass, 1 skipped)
  - **Misc Widgets** : 41 tests ✅
    - `CircularTimer` : 11 tests ✅
    - `OptionSelector` : 10 tests ✅
    - `ToggleIcon` : 12 tests ✅
    - `ToggleSwitch` : 8 tests ✅
- **Test Organization** :
  - `tests/run_tests.py` - Centralized test runner
  - `tests/conftest.py` - Pytest configuration and fixtures
  - `tests/unit/` - Unit tests organized by widget category
- **Test Documentation** : Complete documentation for all test categories

### 🔧 Configuration
- **Updated pyproject.toml** :
  - French description and improved keywords
  - Enhanced classifiers for better PyPI visibility
  - Development status moved to Beta
  - Better dependency organization
- **Enhanced .gitignore** : Comprehensive coverage for Python projects
- **Updated MANIFEST.in** : Proper file inclusion for distribution

### 🐛 Bug Fixes
- **Qt Event Handling** : Fixed issues with mock events in tests
- **Import Errors** : Corrected QEvent import from PySide6.QtCore
- **Test Reliability** : Improved test stability and error handling
- **Accessibility Tests** : Fixed focus policy validation in tests

### 🎯 Features Tested
- **Widget Properties** : Getters, setters, validation, signals
- **Event Handling** : Mouse, keyboard, paint, resize events
- **Qt Signals** : 6 different signals tested across widgets
- **Widget Interactions** : Toggle behavior, hover effects, focus management
- **Icon Management** : QIcon, files, SVG handling
- **State Transitions** : Status changes, color updates, alignments
- **Qt Integration** : Fixtures, mocks, isolation

### 📁 New Project Structure
```
ezqt_widgets/
├── README.md                    # Main README
├── docs/                       # 📚 Centralized documentation
│   ├── README.md              # Documentation index
│   ├── CHANGELOG.md           # Version history
│   ├── STYLE_GUIDE.md         # Style guide
│   ├── QUICK_START_TESTS.md   # Quick test guide
│   └── tests/                 # Test documentation
├── tests/                      # 🧪 Centralized tests
│   ├── run_tests.py           # Test runner
│   ├── conftest.py            # Pytest configuration
│   └── unit/                  # Unit tests
└── ezqt_widgets/              # 📦 Source code
```

### 🚀 Usage
- **Test Execution** : `python tests/run_tests.py --type unit`
- **Documentation** : Navigate via `docs/README.md`
- **Development** : `pip install -e ".[dev]"`

### 📊 Statistics
- **Total Tests** : 262 (254 pass, 8 skipped)
- **Coverage Estimate** : 27-90% per widget
- **Widgets Tested** : 15 widgets (3 button, 4 label, 4 input, 4 misc)
- **Test Categories** : Unit tests, property tests, event tests, signal tests

---

## [2.0.0] - 2025-07-26

### 🚀 Added
- **PySide6 6.9.1 Support** : Complete migration to the latest stable version of PySide6
- **Type Hints Improvements** : Utilization of new PySide6 6.9.1 typing features
- **Windows ARM64 Support** : Compatibility with new Windows architectures
- **New APIs** : Support for `QMessageLogger` and other new features
- **Enhanced Deployment Tools** : Support for `--flatpak`, `--standalone` and `pyproject.toml`

### 🔧 Changed
- **Major Version** : Upgrade from 1.0.9 to 2.0.0 to reflect major changes
- **PySide6 Dependency** : Updated from `6.7.3` to `>=6.9.1,<7.0.0`
- **Development Status** : Moved from "Alpha" to "Beta" (3 → 4)
- **Code Structure** : Complete uniformization of all widgets

### 🧹 Cleaned
- **Unused Imports** : Removed all unused imports from all widgets
  - `Callable` removed from `icon_button.py`, `password_input.py`, `hover_label.py`, `search_input.py`, `toggle_switch.py`, `date_button.py`, `loader_button.py`
  - `QAction` removed from `password_input.py` and `search_input.py`
  - `QSizePolicy` removed from `date_button.py` and `loader_button.py`
  - `QPropertyAnimation` and `QEasingCurve` removed from `loader_button.py`
  - `datetime` removed from `date_button.py`

### 📝 Documentation
- **README.md** : Updated with new PySide6 version and added Changelog section
- **pyproject.toml** : Complete project configuration update
- **Uniformized Comments** : Standardization of all comments according to `icon_button.py` model

### 🔄 Refactored
- **Widget Structure** : Complete reorganization with standardized sections:
  - `# INITIALIZATION`
  - `# PROPERTIES`
  - `# UTILITY FUNCTIONS`
  - `# EVENT FUNCTIONS`
  - `# OVERRIDE FUNCTIONS`
  - `# STYLE FUNCTIONS`

### 🐛 Fixed
- **Error Handling** : Improved robustness of icon loading
- **Performance Optimizations** : Enhanced animations and rendering
- **Compatibility** : Fixed compatibility issues with PySide6 6.9.1

### 📦 Updated Widgets
All widgets have been uniformized and optimized:

#### Buttons (`button/`)
- ✅ `icon_button.py` - Reference model
- ✅ `date_button.py` - Comment uniformization
- ✅ `loader_button.py` - Import cleanup

#### Inputs (`input/`)
- ✅ `auto_complete_input.py` - Uniform structure
- ✅ `password_input.py` - Improved icon management
- ✅ `search_input.py` - Interface optimization
- ✅ `tab_replace_textedit.py` - Enhanced event handling

#### Labels (`label/`)
- ✅ `clickable_tag_label.py` - Improved user interface
- ✅ `framed_label.py` - Simplified structure
- ✅ `hover_label.py` - Optimized icon handling
- ✅ `indicator_label.py` - More maintainable code

#### Misc (`misc/`)
- ✅ `circular_timer.py` - Enhanced animations
- ✅ `option_selector.py` - Smoother interface
- ✅ `toggle_icon.py` - Optimized state management
- ✅ `toggle_switch.py` - Improved graphical rendering

### 🔧 Technical Improvements
- **Icon Management** : Enhanced support for SVG, URL and local icons
- **Animations** : Optimized transitions and visual effects
- **Events** : More robust user interaction handling
- **Styles** : Improved visual consistency

### 📋 Migration
- **Backward Compatibility** : Widgets remain compatible with existing applications
- **Stable API** : No public API changes, only internal improvements
- **Performance** : Performance improvements thanks to PySide6 6.9.1 optimizations

---

## [1.0.9] - 2025-01-19

### 🔧 Changed
- Minor fixes and optimizations
- Documentation improvements

### 🐛 Fixed
- Fixed minor bugs in widgets
- Improved overall stability

---

## [1.0.0] - 2025-07-24

### 🚀 Added
- Initial version of EzQt_Widgets
- Complete collection of custom widgets for PySide6
- Comprehensive documentation and usage examples
- Support for PySide6 6.7.3

### 📦 Included Widgets
- Custom buttons (IconButton, DateButton, LoaderButton)
- Advanced inputs (PasswordInput, SearchInput, AutoCompleteInput, TabReplaceTextEdit)
- Interactive labels (ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel)
- Utility components (CircularTimer, OptionSelector, ToggleIcon, ToggleSwitch)

---

## Change Types

- **🚀 Added** : New features
- **🔧 Changed** : Changes in existing functionality
- **🐛 Fixed** : Bug fixes
- **🧹 Cleaned** : Removal of obsolete or unnecessary code
- **📝 Documentation** : Documentation updates
- **🔄 Refactored** : Code restructuring without functional changes
- **📦 Updated Widgets** : Widget-specific modifications
- **🔧 Technical Improvements** : Optimizations and technical enhancements
- **📋 Migration** : Migration instructions and notes 