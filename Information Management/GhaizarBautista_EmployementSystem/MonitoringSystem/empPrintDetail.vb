Imports System.Drawing.Printing

Public Class empPrintDetail
    Dim WithEvents PD As New PrintDocument
    Dim PPD As New PrintPreviewDialog
    Dim longpaper As Integer
    Private Sub PD_BeginPrint(sender As Object, e As PrintEventArgs) Handles PD.BeginPrint
        Dim pagesetup As New PageSettings
        pagesetup.PaperSize = New PaperSize("Legal", 850, 1300)
        PD.DefaultPageSettings = pagesetup

    End Sub

    Private Sub PD_PrintPage(sender As Object, e As PrintPageEventArgs) Handles PD.PrintPage
        Dim f8 As New Font("Calibri", 8, FontStyle.Regular)
        Dim f10 As New Font("Calibri", 10, FontStyle.Regular)
        Dim f10b As New Font("Calibri", 10, FontStyle.Bold)
        Dim f14 As New Font("Calibri", 14, FontStyle.Regular)


        Dim leftMargin As Integer = PD.DefaultPageSettings.Margins.Left
        Dim centerMargin As Integer = PD.DefaultPageSettings.PaperSize.Width / 2
        Dim rightMargin As Integer = PD.DefaultPageSettings.PaperSize.Width

        Dim right As New StringFormat
        Dim center As New StringFormat
        right.Alignment = StringAlignment.Far
        center.Alignment = StringAlignment.Center


        Dim line As String
        line = "-------------------------------------------------"
        e.Graphics.DrawString("EMPLOYEE", f10, Brushes.Black, centerMargin, 5, center)
        e.Graphics.DrawString("ZEAR DEVELOPER", f10, Brushes.Black, centerMargin, 25, center)
    End Sub
End Class