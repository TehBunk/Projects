
def clicked(app):
    acc = app.comboBox.currentText()
    ticker = app.lineEdit_ticker.text()
    price = app.doubleSpinBox_price.value()
    qty = app.doubleSpinBox_qty.value()

    app.comboBox.currentText()
    app.lineEdit_ticker.clear()
    app.doubleSpinBox_price.clear()
    app.doubleSpinBox_qty.clear()

    print(f"{acc} {ticker} {price} {qty}")
