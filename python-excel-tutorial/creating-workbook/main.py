from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

# Adding rows
ws.append(["Make", "Model"])
ws.append(["Toyota", "Supra"])

wb.save("cars.xlsx")