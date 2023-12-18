# import pandas as pd
#
# data = {
#   "1": ['calories',420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390],
#   "2": ['duration',50, 40, 45,420, 380, 390,420, 380, 390,420, 380, 390],
#   "3": ['flavour', 420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390],
#   "4": ['texture', 420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390],
#   "5": ['color', 50, 40, 45,420, 380, 390,420, 380, 390,420, 380, 390],
#   "6": ['height', 420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390],
#   "7": ['width', 420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390]
# }
#
# #load data into a DataFrame object:
# data_frame = pd.DataFrame(data)
#
# from reportlab.lib.pagesizes import letter, A4
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from reportlab.lib import colors
# pdf_name = SimpleDocTemplate("pdf_name.pdf", pagesize=letter)
# table_data = []
# for i, row in data_frame.iterrows():
#     table_data.append(list(row))
# table = Table(table_data)
# table_style = TableStyle([
#     ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#     ('FONTSIZE', (0, 0), (-1, 0), 14),
#     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#     ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
#     ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
#     ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
#     ('FONTSIZE', (0, 1), (-1, -1), 12),
#     ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
# ])
# table.setStyle(table_style)
# pdf_table = []
# pdf_table.append(table)
# pdf_name.build(pdf_table)




