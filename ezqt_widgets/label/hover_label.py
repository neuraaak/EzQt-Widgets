# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////

# IMPORT BASE
# ///////////////////////////////////////////////////////////////

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import (
    Signal,
    Qt,
    QSize,
    QRect,
)
from PySide6.QtWidgets import (
    QLabel,
)
from PySide6.QtGui import (
    QPainter,
    QIcon,
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


class HoverLabel(QLabel):
    """
    HoverLabel is an interactive QLabel that displays a floating icon when hovered, and emits a signal when the icon is clicked.

    This widget is useful for adding contextual actions or visual cues to labels in a Qt interface.

    Features:
        - Displays a custom icon on hover, with configurable opacity, size, and color overlay
        - Emits a hoverIconClicked signal when the icon is clicked
        - Handles mouse events and cursor changes for better UX
        - Text and icon can be set at construction or via properties

    Parameters
    ----------
    parent : QWidget, optional
        The parent widget (default: None).
    icon : QIcon or str, optional
        The icon to display on hover (QIcon or path to icon file).
    text : str, optional
        The label text (default: "").
    opacity : float, optional
        The opacity of the hover icon (default: 0.5).
    icon_size : QSize or tuple, optional
        The size of the hover icon (default: QSize(16, 16)).
    icon_color : QColor or str, optional
        Optional color overlay to apply to the icon (default: None).
    *args, **kwargs :
        Additional arguments passed to QLabel.

    Properties
    ----------
    opacity : float
        Get or set the opacity of the hover icon.
    hover_icon : QIcon
        Get or set the icon displayed on hover.
    icon_size : QSize
        Get or set the size of the hover icon.
    icon_color : QColor or str or None
        Get or set the color overlay of the hover icon.

    Signals
    -------
    hoverIconClicked()
        Emitted when the hover icon is clicked.
    """

    hoverIconClicked = Signal()  # Signal personnalisé

    # INITIALIZATION
    # ///////////////////////////////////////////////////////////////

    def __init__(
        self,
        parent=None,
        icon=None,
        text="",
        opacity=0.5,
        icon_size=QSize(16, 16),
        icon_color=None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(text or "", parent, *args, **kwargs)
        self.setProperty("type", "HoverLabel")
        self._hover_icon = QIcon(icon) if icon else None
        self.show_hover_icon = False
        self._opacity = opacity
        self._icon_size = (
            QSize(*icon_size)
            if isinstance(icon_size, (tuple, list))
            else QSize(icon_size)
        )
        self._icon_color = icon_color
        self.setMouseTracking(True)

    # PROPERTY FUNCTIONS
    # ///////////////////////////////////////////////////////////////

    @property
    def opacity(self) -> float:
        """Get or set the opacity of the hover icon."""
        return self._opacity

    @opacity.setter
    def opacity(self, value: float) -> None:
        """Set the opacity of the hover icon."""
        self._opacity = float(value)
        self.update()

    @property
    def hover_icon(self) -> QIcon:
        """Get or set the icon displayed on hover."""
        return self._hover_icon

    @hover_icon.setter
    def hover_icon(self, value) -> None:
        """Set the icon displayed on hover. Accepts QIcon or str (path). Raises TypeError otherwise."""
        if value is None:
            self._hover_icon = None
        elif isinstance(value, QIcon):
            self._hover_icon = value
        elif isinstance(value, str):
            icon = QIcon(value)
            if icon.isNull():
                raise ValueError(f"Invalid icon path: {value}")
            self._hover_icon = icon
        else:
            raise TypeError("hover_icon must be a QIcon, a path string, or None.")
        self.update()

    @property
    def icon_size(self) -> QSize:
        """Get or set the size of the hover icon."""
        return self._icon_size

    @icon_size.setter
    def icon_size(self, value) -> None:
        if isinstance(value, QSize):
            self._icon_size = value
        elif isinstance(value, (tuple, list)) and len(value) == 2:
            self._icon_size = QSize(*value)
        else:
            raise TypeError(
                "icon_size must be a QSize or a tuple/list of two integers."
            )
        self.update()

    @property
    def icon_color(self):
        """Get or set the color overlay of the hover icon (QColor, str, or None)."""
        return self._icon_color

    @icon_color.setter
    def icon_color(self, value):
        self._icon_color = value
        self.update()

    # EVENT FUNCTIONS
    # ///////////////////////////////////////////////////////////////

    def mouseMoveEvent(self, event) -> None:
        """Handle mouse movement events."""
        vertical_offset = 5
        icon_size = self._icon_size
        icon_x = self.width() - icon_size.width() - 4
        icon_y = (self.height() - icon_size.height()) // 2 + vertical_offset
        icon_rect = QRect(icon_x, icon_y, icon_size.width(), icon_size.height())
        if (
            self.show_hover_icon
            and self._hover_icon
            and icon_rect.contains(event.pos())
        ):
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        else:
            self.setCursor(Qt.CursorShape.ArrowCursor)
        super().mouseMoveEvent(event)

    # ///////////////////////////////////////////////////////////////

    def mousePressEvent(self, event) -> None:
        """Handle mouse press events."""
        vertical_offset = 5
        icon_size = self._icon_size
        icon_x = self.width() - icon_size.width() - 4
        icon_y = (self.height() - icon_size.height()) // 2 + vertical_offset
        icon_rect = QRect(icon_x, icon_y, icon_size.width(), icon_size.height())
        if (
            self.show_hover_icon
            and self._hover_icon
            and icon_rect.contains(event.pos())
        ):
            self.hoverIconClicked.emit()
        super().mousePressEvent(event)

    # ///////////////////////////////////////////////////////////////

    def enterEvent(self, event) -> None:
        """Handle enter events."""
        self.show_hover_icon = True
        self.update()  # Demande de redessiner le widget

    # ///////////////////////////////////////////////////////////////

    def leaveEvent(self, event) -> None:
        """Handle leave events."""
        self.show_hover_icon = False
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.update()

    # UI FUNCTIONS
    # ///////////////////////////////////////////////////////////////

    def paintEvent(self, event) -> None:
        """Paint the widget."""
        super().paintEvent(event)
        if self.show_hover_icon and self._hover_icon:
            painter = QPainter(self)
            painter.setOpacity(self._opacity)
            vertical_offset = 5
            icon_size = self._icon_size
            icon_x = self.width() - icon_size.width() - 4
            icon_y = (self.height() - icon_size.height()) // 2 + vertical_offset
            icon_rect = QRect(icon_x, icon_y, icon_size.width(), icon_size.height())
            icon_pixmap = self._hover_icon.pixmap(icon_size)
            # Optionally apply a color overlay
            if self._icon_color:
                from PySide6.QtGui import QColor, QPixmap, QPainter as QPainter2

                overlay = QPixmap(icon_pixmap.size())
                overlay.fill(Qt.transparent)
                painter2 = QPainter2(overlay)
                color = QColor(self._icon_color)
                painter2.setCompositionMode(
                    QPainter2.CompositionMode.CompositionMode_Source
                )
                painter2.fillRect(overlay.rect(), color)
                painter2.setCompositionMode(
                    QPainter2.CompositionMode.CompositionMode_DestinationIn
                )
                painter2.drawPixmap(0, 0, icon_pixmap)
                painter2.end()
                icon_pixmap = overlay
            painter.drawPixmap(icon_rect, icon_pixmap)

    # STYLE FUNCTIONS
    # ///////////////////////////////////////////////////////////////

    def refresh_style(self) -> None:
        """Refresh the widget's style (useful after dynamic stylesheet changes)."""
        # // REFRESH STYLE
        self.style().unpolish(self)
        self.style().polish(self)
        # //////
