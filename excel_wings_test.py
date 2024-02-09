import xlwings as xw
wb=xw.Book('TestJoan.xlsm')
ws = wb.sheets['ItemList']
ws.range('A21').value = 'Hello, Excel!'
ws.range('B1:C4').value = 'SUP DOG'
ws.cells(3,5).value = 12   # tambien recibe la columna con letra  (1,"E")
ws.range("H2").value = [["col name 1", "col name 2"],[1,2],[3,4],[5,6]]
ws.range("H10").value = [1,2,3,4,5,6,7]