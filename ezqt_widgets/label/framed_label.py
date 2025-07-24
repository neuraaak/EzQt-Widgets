# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////

# IMPORT BASE
# ///////////////////////////////////////////////////////////////

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import (
    Qt,
    Signal,
)
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
)

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

## ==> GLOBALS
# ///////////////////////////////////////////////////////////////

## ==> FUNCTIONS
# ///////////////////////////////////////////////////////////////

## ==> VARIABLES
# ///////////////////////////////////////////////////////////////

# CLASS
# ///////////////////////////////////////////////////////////////


class FramedLabel(QFrame):
    """
    FramedLabel is a flexible label widget based on QFrame, designed for advanced styling and layout in Qt applications.

    This widget encapsulates a QLabel inside a QFrame, allowing you to benefit from QFrame's styling and layout capabilities
    while providing a simple interface for text display, alignment, and dynamic style updates.

    Features:
        - Property-based access to the label text (text) and alignment (alignment)
        - Emits a textChanged(str) signal when the text changes
        - Allows custom stylesheet injection for advanced appearance
        - Suitable for use as a header, section label, or any context where a styled label is needed

    Parameters
    ----------
    text : str, optional
        The initial text to display in the label (default: "").
    parent : QWidget, optional
        The parent widget (default: None).
    alignment : Qt.AlignmentFlag, optional
        The alignment of the label text (default: Qt.AlignmentFlag.AlignCenter).
    style_sheet : str, optional
        Custom stylesheet to apply to the QFrame (default: None, uses transparent background).
    *args, **kwargs :
        Additional arguments passed to QFrame.

    Properties
    ----------
    text : str
        Get or set the label text.
    alignment : Qt.AlignmentFlag
        Get or set the label alignment.

    Signals
    -------
    textChanged(str)
        Emitted when the label text changes.
    """

    textChanged = Signal(str)

    # INITIALIZATION
    # ///////////////////////////////////////////////////////////////

    def __init__(
        self,
        text="",
        parent=None,
        alignment=Qt.AlignmentFlag.AlignCenter,
        style_sheet=None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setProperty("type", "FramedLabel")

        # // STYLE SHEET
        self.setStyleSheet(style_sheet or "background-color: transparent;")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # //////

        # // LAYOUT SETUP
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(alignment)
        # //////

        # // LABEL SETUP
        self.label = QLabel(text, self)
        self._alignment = alignment
        self.label.setAlignment(alignment)
        layout.addWidget(self.label)
        # //////

    # PROPERTY FUNCTIONS
    # ///////////////////////////////////////////////////////////////

    @property
    def text(self) -> str:
        """Get or set the label text."""
        # // GET TEXT
        return self.label.text()
        # //////

    @text.setter
    def text(self, value: str) -> None:
        """Set the label text."""
        # // SET TEXT
        if not isinstance(value, str):
            value = str(value)
        if value != self.label.text():
            self.label.setText(value)
            self.textChanged.emit(value)
        # //////

    @property
    def alignment(self) -> Qt.AlignmentFlag:
        """Get or set the alignment of the label."""
        # // GET ALIGNMENT
        return self._alignment
        # //////

    @alignment.setter
    def alignment(self, value: Qt.AlignmentFlag) -> None:
        """Set the alignment of the label."""
        # // SET ALIGNMENT
        self._alignment = value
        self.label.setAlignment(value)
        # Optionally update layout alignment as well
        if self.layout():
            self.layout().setAlignment(value)
        # //////

    # STYLE FUNCTIONS
    # ///////////////////////////////////////////////////////////////

    def refresh_style(self) -> None:
        """Refresh the widget's style (useful after dynamic stylesheet changes)."""
        # // REFRESH STYLE
        self.style().unpolish(self)
        self.style().polish(self)
        # //////
