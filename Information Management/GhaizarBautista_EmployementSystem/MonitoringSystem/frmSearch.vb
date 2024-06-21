Imports System.Data.SqlClient
Imports System.Drawing.Printing

Public Class frmSearch
    Dim WithEvents PD As New PrintDocument
    Dim PPD As New PrintPreviewDialog
    Dim longpaper As Integer

    Private Sub txtEmpID_TextChanged(sender As Object, e As EventArgs) Handles txtEmpID.TextChanged
        sql = "SELECT `EMPID` AS 'Employee Id', `emp_fname` as 'First Name', `emp_lname` as 'Last Name', `emp_mname` AS 'Middle Name' " &
              "FROM `employee` WHERE `EMPID` LIKE '%" & txtEmpID.Text & "%' OR `emp_fname` LIKE '%" & txtEmpID.Text & "%' " &
              "OR `emp_lname` LIKE '%" & txtEmpID.Text & "%' OR `emp_mname` LIKE '%" & txtEmpID.Text & "%'"
        reloadDtg(sql, dtgemplist)
    End Sub

    Private Sub frmSearch_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        sql = "SELECT `EMPID` AS 'Employee Id', `emp_fname` as 'First Name', `emp_lname` as 'Last Name', `emp_mname` AS 'Middle Name' FROM employee"
        reloadDtg(sql, dtgemplist)
    End Sub

    Private Sub PD_BeginPrint(sender As Object, e As Printing.PrintEventArgs) Handles PD.BeginPrint
        Dim pagesetup As New PageSettings
        pagesetup.PaperSize = New PaperSize("Custom", 1300, 850)
        PD.DefaultPageSettings = pagesetup
    End Sub

    Private Sub PD_PrintPage(sender As Object, e As PrintPageEventArgs) Handles PD.PrintPage
        Dim f8 As New Font("Calibri", 8, FontStyle.Regular)
        Dim f10 As New Font("Calibri", 10, FontStyle.Regular)
        Dim f10b As New Font("Calibri", 10, FontStyle.Bold)
        Dim f16b As New Font("Calibri", 16, FontStyle.Bold)
        Dim f14 As New Font("Calibri", 14, FontStyle.Regular)
        Dim f12 As New Font("Calibri", 12, FontStyle.Regular)
        Dim heading As New Font("Times New Roman", 16, FontStyle.Underline)

        'Dim leftMargin As Integer = PD.DefaultPageSettings.Margins.Left
        Dim leftMargin As Integer = 50
        Dim centerMargin As Integer = PD.DefaultPageSettings.PaperSize.Height / 2
        Dim rightMargin As Integer = PD.DefaultPageSettings.PaperSize.Width - 50

        Dim right As New StringFormat
        Dim center As New StringFormat
        right.Alignment = StringAlignment.Far
        center.Alignment = StringAlignment.Center

        Dim line As String
        line = "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        e.Graphics.DrawString("Employee 201 File Report", f16b, Brushes.Black, centerMargin, 20, center)
        e.Graphics.DrawString("ZEAR DEVELOPER", f10, Brushes.Black, centerMargin, 45, center)

        e.Graphics.DrawString(line, f10, Brushes.Black, 0, 65)
        e.Graphics.DrawString("Company Name: Zear Company ", f12, Brushes.Black, leftMargin, 85)
        e.Graphics.DrawString("Employee No: " & dgprint.CurrentRow.Cells(0).Value, f12, Brushes.Black, leftMargin, 105)
        Dim fullname = dgprint.CurrentRow.Cells(2).Value & ", " & dgprint.CurrentRow.Cells(1).Value & " " & dgprint.CurrentRow.Cells(3).Value.ToString().Substring(0, 1) & "."
        e.Graphics.DrawString("Employee Name: " & fullname, f12, Brushes.Black, leftMargin, 125)


        e.Graphics.DrawString(line, f10, Brushes.Black, 0, 145)
        e.Graphics.DrawString("Basic Information ", heading, Brushes.Black, leftMargin, 170)
        e.Graphics.DrawString("Date of Birth: " & dgprint.CurrentRow.Cells(7).Value, f12, Brushes.Black, leftMargin, 205)
        e.Graphics.DrawString("Birth Place: " & dgprint.CurrentRow.Cells(8).Value, f12, Brushes.Black, leftMargin, 225)
        e.Graphics.DrawString("Gender :  " & dgprint.CurrentRow.Cells(9).Value, f12, Brushes.Black, leftMargin, 245)
        e.Graphics.DrawString("Marital Status : " & dgprint.CurrentRow.Cells(6).Value, f12, Brushes.Black, leftMargin, 265)
        e.Graphics.DrawString("Address : " & dgprint.CurrentRow.Cells(4).Value, f12, Brushes.Black, leftMargin, 285)
        e.Graphics.DrawString("Contact No : " & dgprint.CurrentRow.Cells(5).Value, f12, Brushes.Black, leftMargin, 305)

        e.Graphics.DrawString(line, f10, Brushes.Black, 0, 325)
        e.Graphics.DrawString("Payroll Information ", heading, Brushes.Black, leftMargin, 350)
        e.Graphics.DrawString("Department : " & dgprint.CurrentRow.Cells(22).Value, f12, Brushes.Black, leftMargin, 385)
        e.Graphics.DrawString("Sub Department : ", f12, Brushes.Black, leftMargin, 405)
        e.Graphics.DrawString("Rank : ", f12, Brushes.Black, leftMargin, 425)
        e.Graphics.DrawString("Position : " & dgprint.CurrentRow.Cells(19).Value, f12, Brushes.Black, leftMargin, 445)
        e.Graphics.DrawString("Date Hired : " & dgprint.CurrentRow.Cells(21).Value, f12, Brushes.Black, leftMargin, 465)
        e.Graphics.DrawString("Last Date : ", f12, Brushes.Black, leftMargin, 485)
        e.Graphics.DrawString("Tax Status : ", f12, Brushes.Black, leftMargin, 505)
        e.Graphics.DrawString("Basic Pay Amount : " & dgprint.CurrentRow.Cells(17).Value, f12, Brushes.Black, leftMargin, 525)
        e.Graphics.DrawString("Pay Rate Type : " & dgprint.CurrentRow.Cells(18).Value, f12, Brushes.Black, leftMargin, 545)
        e.Graphics.DrawString("Payment Method : ", f12, Brushes.Black, leftMargin, 565)
        e.Graphics.DrawString("Bank Route : ", f12, Brushes.Black, leftMargin, 585)
        e.Graphics.DrawString("Account Type : ", f12, Brushes.Black, leftMargin, 605)
        e.Graphics.DrawString("Payroll Group : " & dgprint.CurrentRow.Cells(23).Value, f12, Brushes.Black, leftMargin, 625)
        e.Graphics.DrawString("Default Project : ", f12, Brushes.Black, leftMargin, 645)
        e.Graphics.DrawString("Time Sheet Approval : ", f12, Brushes.Black, leftMargin, 665)
        e.Graphics.DrawString("Overtime Approval : ", f12, Brushes.Black, leftMargin, 685)
        e.Graphics.DrawString("COS Approval Group : ", f12, Brushes.Black, leftMargin, 705)

    End Sub

    Private Sub dtgemplist_CellContentClick(sender As Object, e As DataGridViewCellEventArgs) Handles dtgemplist.CellContentClick

        sql = "Select e.*, ew.* From employee e Join employee_workinfo ew ON e.EMPID = ew.EMPID Where e.EMPID Like '%" & dtgemplist.CurrentRow.Cells(0).Value & "%';"
        reloadDtg(sql, dgprint)

        PPD.Document = PD
        PPD.ShowDialog()
    End Sub
End Class
