# EzQt Widgets – Style Guide

Ce document définit les conventions de style (QSS) pour les widgets custom du projet EzQt Widgets.

## Principes généraux
- Utiliser des couleurs, bordures et arrondis cohérents pour tous les widgets.
- Privilégier les sélecteurs QSS spécifiques pour chaque composant custom.
- Centraliser les couleurs et espacements pour faciliter la maintenance.

---

## 1. AutoCompleteInput

### QSS recommandé
```css
/* Widget principal */
AutoCompleteInput {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
    selection-color: #ffffff;
    selection-background-color: #0078d4;
}
AutoCompleteInput:hover {
    background-color: #2d2d2d;
    border: 1px solid #666666;
    border-radius: 4px 4px 4px 4px;
}
AutoCompleteInput:focus {
    background-color: #2d2d2d;
    border: 1px solid #0078d4;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Les propriétés de type sont automatiquement définies dans le code.

---

## 2. PasswordInput

### QSS recommandé
```css
/* Widget principal */
PasswordInput QWidget {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
}

/* Champ de saisie */
PasswordInput QLineEdit {
    background-color: transparent;
    border: none;
    border-radius: 4px 4px 4px 4px;
    padding: 0px 4px 4px 4px;
    selection-color: #ffffff;
    selection-background-color: #0078d4;
}
PasswordInput QLineEdit:hover {
    background-color: transparent;
    border: none;
    border-radius: 4px 4px 4px 4px;
}
PasswordInput QLineEdit:focus {
    background-color: transparent;
    border: none;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Le padding à droite est géré automatiquement pour l'icône.
- Les propriétés de type sont automatiquement définies dans le code.

---

## 3. SearchInput

### QSS recommandé
```css
/* Widget principal */
SearchInput {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
    selection-color: #ffffff;
    selection-background-color: #0078d4;
}
SearchInput:hover {
    background-color: #2d2d2d;
    border: 1px solid #666666;
    border-radius: 4px 4px 4px 4px;
}
SearchInput:focus {
    background-color: #2d2d2d;
    border: 1px solid #0078d4;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Les propriétés de type sont automatiquement définies dans le code.

---

## 4. TabReplaceTextEdit

### QSS recommandé
```css
/* Widget principal */
TabReplaceTextEdit {
    background-color: #2d2d2d;
    border-radius: 5px;
    padding: 10px;
    selection-color: #ffffff;
    selection-background-color: #0078d4;
}
TabReplaceTextEdit QScrollBar:vertical {
    width: 8px;
}
TabReplaceTextEdit QScrollBar:horizontal {
    height: 8px;
}
TabReplaceTextEdit:hover {
    border: 2px solid #666666;
}
TabReplaceTextEdit:focus {
    border: 2px solid #0078d4;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Les scrollbars sont personnalisées pour une meilleure intégration.
- Les propriétés de type sont automatiquement définies dans le code.

---

## 5. HoverLabel

### QSS recommandé
```css
/* Widget principal */
HoverLabel {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Les propriétés de type sont automatiquement définies dans le code.

---

## 6. IndicatorLabel

### QSS recommandé
```css
/* Widget principal */
IndicatorLabel {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Les propriétés de type sont automatiquement définies dans le code.

---

## Bonnes pratiques
- Les propriétés de type sont automatiquement définies dans le code des widgets.
- Documenter chaque section de QSS dans ce fichier.
- Tester l'apparence sur différents OS et thèmes Qt.
- Utiliser des couleurs cohérentes pour la sélection (selection-color et selection-background-color). 