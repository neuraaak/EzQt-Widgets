# EzQt Widgets – Style Guide

## Sommaire

### **Inputs**
- [AutoCompleteInput](#1-autocompleteinput)
- [PasswordInput](#2-passwordinput)
- [SearchInput](#3-searchinput)
- [TabReplaceTextEdit](#4-tabreplacetextedit)

### **Labels**
- [HoverLabel](#5-hoverlabel)
- [IndicatorLabel](#6-indicatorlabel)

### **Boutons**
- [DateButton](#7-datebutton)
- [LoaderButton](#8-loaderbutton)
- [IconButton](#9-iconbutton)

### **Divers**
- [Bonnes pratiques](#bonnes-pratiques)

---

Ce document définit les conventions de style (QSS) pour les widgets custom du projet EzQt Widgets.

## Principes généraux
- Utiliser des couleurs, bordures et arrondis cohérents pour tous les widgets.
- Privilégier les sélecteurs QSS spécifiques pour chaque composant custom.
- Centraliser les couleurs et espacements pour faciliter la maintenance.

---

## 1. AutoCompleteInput

[⬆️ Retour en haut](#sommaire) 

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

[⬆️ Retour en haut](#sommaire) 

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

[⬆️ Retour en haut](#sommaire) 

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

[⬆️ Retour en haut](#sommaire) 

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

[⬆️ Retour en haut](#sommaire) 

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

[⬆️ Retour en haut](#sommaire) 

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

## 7. DateButton

[⬆️ Retour en haut](#sommaire) 

### QSS recommandé
```css
/* Widget principal */
DateButton {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
    selection-color: #ffffff;
    selection-background-color: #0078d4;
}
DateButton:hover {
    background-color: #2d2d2d;
    border: 1px solid #666666;
    border-radius: 4px 4px 4px 4px;
}
DateButton:focus {
    background-color: #2d2d2d;
    border: 1px solid #0078d4;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Les propriétés de type sont automatiquement définies dans le code.

---

## 8. LoaderButton

[⬆️ Retour en haut](#sommaire) 

### QSS recommandé
```css
/* Widget principal */
LoaderButton {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
    selection-color: #ffffff;
    selection-background-color: #0078d4;
}
LoaderButton:hover {
    background-color: #2d2d2d;
    border: 1px solid #666666;
    border-radius: 4px 4px 4px 4px;
}
LoaderButton:focus {
    background-color: #2d2d2d;
    border: 1px solid #0078d4;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration
- Adapter les couleurs selon la charte graphique de votre application.
- Les propriétés de type sont automatiquement définies dans le code.

--- 

## 9. IconButton

[⬆️ Retour en haut](#sommaire) 

### QSS recommandé
```css
/* Widget principal */
IconButton {
    background-color: #2d2d2d;
    border: 1px solid #444444;
    border-radius: 4px 4px 4px 4px;
    selection-color: #ffffff;
    selection-background-color: #0078d4;
}
IconButton:hover {
    background-color: #2d2d2d;
    border: 1px solid #666666;
    border-radius: 4px 4px 4px 4px;
}
IconButton:focus {
    background-color: #2d2d2d;
    border: 1px solid #0078d4;
    border-radius: 4px 4px 4px 4px;
}
```

### Conseils d'intégration

- Adapter les couleurs selon la charte graphique de votre application.
- Les propriétés de type sont automatiquement définies dans le code.

--- 

## Bonnes pratiques

[⬆️ Retour en haut](#sommaire) 

- Les propriétés de type sont automatiquement définies dans le code des widgets.
- Documenter chaque section de QSS dans ce fichier.
- Tester l'apparence sur différents OS et thèmes Qt.
- Utiliser des couleurs cohérentes pour la sélection (selection-color et selection-background-color). 

