Public Class Form1

    Private Sub customizeDesign()
        pnl_emp_sub.Visible = False
        pnl_leave_sub.Visible = False
        pnl_report_sub.Visible = False
        pnn_search_sub.Visible = False
    End Sub

    Private Sub hideSubMenu()
        If pnl_emp_sub.Visible = True Then pnl_emp_sub.Visible = False
        If pnl_leave_sub.Visible = True Then pnl_leave_sub.Visible = False
        If pnl_report_sub.Visible = True Then pnl_report_sub.Visible = False
        If pnn_search_sub.Visible = True Then pnn_search_sub.Visible = False
    End Sub

    Private Sub showSubMenu(ByVal subMenu As Panel)
        If subMenu.Visible = False Then
            hideSubMenu()
            subMenu.Visible = True
        Else
            subMenu.Visible = False
        End If
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        customizeDesign()
    End Sub

    Private Sub IconButton2_Click(sender As Object, e As EventArgs) Handles IconButton2.Click
        showSubMenu(pnl_emp_sub)
    End Sub

    Private Sub IconButton5_Click(sender As Object, e As EventArgs) Handles IconButton5.Click
        showSubMenu(pnl_leave_sub)
    End Sub

    Private Sub IconButton11_Click(sender As Object, e As EventArgs) Handles IconButton11.Click
        showSubMenu(pnn_search_sub)
    End Sub

    Private Sub IconButton14_Click(sender As Object, e As EventArgs) Handles IconButton14.Click
        showSubMenu(pnl_report_sub)
    End Sub

    Private Sub IconButton3_Click(sender As Object, e As EventArgs) Handles IconButton3.Click
        With New frmemployee
            .Show()
            .Focus()
        End With
        hideSubMenu()
    End Sub

    Private Sub IconButton4_Click(sender As Object, e As EventArgs) Handles IconButton4.Click
        With frmlistemployee
            .Show()
            .Focus()
        End With
        hideSubMenu()
    End Sub

    Private Sub IconButton6_Click(sender As Object, e As EventArgs) Handles IconButton6.Click
        With frmleave
            .Show()
            .Focus()
        End With
        hideSubMenu()
    End Sub

    Private Sub IconButton7_Click(sender As Object, e As EventArgs) Handles IconButton7.Click
        With frmLeaveAbsence
            .Show()
            .Focus()
        End With
        hideSubMenu()
    End Sub

    Private Sub IconButton9_Click(sender As Object, e As EventArgs) Handles IconButton9.Click
        With frmdepartment
            .Show()
            .Focus()
        End With
        hideSubMenu()
    End Sub

    Private Sub IconButton10_Click(sender As Object, e As EventArgs) Handles IconButton10.Click
        With frmsettings
            .Show()
            .Focus()
        End With
    End Sub

    Private Sub IconButton12_Click(sender As Object, e As EventArgs) Handles IconButton12.Click
        With frmSearchList
            .ShowDialog()
        End With
    End Sub

    Private Sub IconButton13_Click(sender As Object, e As EventArgs) Handles IconButton13.Click
        With frmEmpDepartment
            .ShowDialog()
        End With
    End Sub


    Private Sub IconButton17_Click(sender As Object, e As EventArgs) Handles IconButton17.Click
        With frmSearch
            .ShowDialog()
        End With
    End Sub

    Private Sub IconButton15_Click(sender As Object, e As EventArgs) Handles IconButton15.Click
        frmPrints.Show()
        frmPrints.Focus()
        sql = "SELECT  e.`EMPID`, concat( `emp_fname`,' ', `emp_lname`,' ', `emp_mname`) as 'Name' ,`emp_sex`,(`d_rate` * 14) as 'TwooWeeksSalary', `position`, `DEPARTMENT` FROM `employee` e ,`employee_workinfo` we  WHERE e.`EMPID`=we.`EMPID`"
        'reports(sql, "allemployees", frmPrints.CrystalReportViewer1)
    End Sub

    Private Sub IconButton16_Click(sender As Object, e As EventArgs) Handles IconButton16.Click
        With frmreports
            .Show()
            .Focus()
        End With
    End Sub
End Class
