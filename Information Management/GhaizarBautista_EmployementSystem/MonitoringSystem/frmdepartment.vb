Public Class frmdepartment
    Private Sub btndeptSave_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btndeptSave.Click
        sql = "INSERT INTO `tbldepartment` (`DEPARTMENT`) VALUES ('" & txtdepartment.Text & "')"
        create(sql, "New Department")
        Call btndeptLoad_Click(sender, e)
    End Sub

    Dim departmentid As Integer = 0
    Private Sub btndeptLoad_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btndeptLoad.Click
        sql = "SELECT ID,`DEPARTMENT` FROM `tbldepartment` "
        reloadDtg(sql, dtgdeptlist)
        txtdepartment.Clear()
        dtgdeptlist.Columns(0).Visible = False
    End Sub

    Private Sub btndeptUpdate_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btndeptUpdate.Click
        sql = "UPDATE `tbldepartment`  SET `DEPARTMENT`='" & txtdepartment.Text & "' WHERE `ID`=" & departmentid
        updates(sql, "Department")
        Call btndeptLoad_Click(sender, e)
    End Sub

    Private Sub btndeptDelete_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btndeptDelete.Click
        sql = "DELETE FROM `tbldepartment` WHERE `ID`='" & dtgdeptlist.CurrentRow.Cells(0).Value & "'"
        deletes(sql, dtgdeptlist.CurrentRow.Cells(1).Value)
        Call btndeptLoad_Click(sender, e)
    End Sub


    Private Sub dtgdeptlist_DoubleClick(ByVal sender As Object, ByVal e As System.EventArgs) Handles dtgdeptlist.DoubleClick
        Try
            departmentid = dtgdeptlist.CurrentRow.Cells(0).Value
            txtdepartment.Text = dtgdeptlist.CurrentRow.Cells(1).Value
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub

End Class