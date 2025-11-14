from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

# Crear aplicación
app = QApplication(sys.argv)

# Crear ventana
ventana = QWidget()
ventana.setWindowTitle("Mi primera ventana PyQt5")
ventana.setGeometry(100, 100, 400, 300)  # x, y, ancho, alto

# Crear widgets
label = QLabel("¡Hola, mundo!")
boton = QPushButton("Haz clic aquí")

def saludar():
    print("¡Hola desde el botón!")

boton.clicked.connect(saludar)

# Layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(boton)
ventana.setLayout(layout)

# Mostrar ventana
ventana.show()
sys.exit(app.exec_())
