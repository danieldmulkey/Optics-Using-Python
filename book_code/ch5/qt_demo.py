import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from .qt_demo_layout import Ui_MainWindow
import paraxial.sources
import paraxial.surfaces


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Gaussian Beam Calculator")
        self.ui.CalculateButton.clicked.connect(self.calculate)

    def calculate(self):
        self.ui.statusbar.clearMessage()
        try:
            λ, dist, R, w, z, zR = self.grab_values()
        except ValueError as e:
            self.ui.statusbar.showMessage(f"Error in values: {e}")
            self.clear_labels()
            return

        try:
            gb = paraxial.sources.GaussianBeam(wavelength=λ, R=R, w=w, z=z, zR=zR)
        except ValueError as e:
            self.ui.statusbar.showMessage(
                f"Error in creating beam: {e}"
            )
            self.clear_labels()
            return

        gb = paraxial.surfaces.Transfer(dist) @ gb
        self.update_labels(gb)

    def grab_values(self):
        R = None
        w = None
        z = None
        zR = None

        counter = 0
        if self.ui.RadiusCheck.isChecked():
            R = self.ui.RadiusSpin.value() * 1e-3
            counter += 1
        if self.ui.SizeCheck.isChecked():
            w = self.ui.SizeSpin.value() * 1e-3
            counter += 1
        if self.ui.PositionCheck.isChecked():
            z = self.ui.PositionSpin.value() * 1e-3
            counter += 1
        if self.ui.RayleighCheck.isChecked():
            zR = self.ui.RayleighSpin.value() * 1e-3
            counter += 1
        if counter != 2:
            raise ValueError(
                f"Please select 2 parameters, not {counter}"
            )

        λ = self.ui.WavelengthSpin.value() * 1e-9
        dist = self.ui.DistanceSpin.value() * 1e-3
        return λ, dist, R, w, z, zR

    def update_labels(self, gb):
        self.ui.RadiusLabel.setText(f"{(gb.R) * 1e3:g}")
        self.ui.SizeLabel.setText(f"{abs(gb.w) * 1e3:g}")
        self.ui.PositionLabel.setText(f"{(gb.z) * 1e3:g}")
        self.ui.RayleighLabel.setText(f"{abs(gb.zR) * 1e3:g}")
        self.ui.WaistLabel.setText(f"{abs(gb.w0) * 1e3:g}")
        self.ui.DivergenceLabel.setText(f"{abs(gb.divergence) * 1e3:g}")

    def clear_labels(self):
        self.ui.RadiusLabel.setText("___")
        self.ui.SizeLabel.setText("___")
        self.ui.PositionLabel.setText("___")
        self.ui.RayleighLabel.setText("___")
        self.ui.WaistLabel.setText("___")
        self.ui.DivergenceLabel.setText("___")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
