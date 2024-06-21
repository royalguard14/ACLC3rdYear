Public Class frmsettings
    Dim positionID As Integer = 0
    Dim departmentid As Integer = 0
    Private Sub npositionsave_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles npositionsave.Click
        Try
            sql = "INSERT INTO `tblsettings` (`DESCRIPTION`, `FORTHE`) VALUES ('" & txtposition.Text & "','Position')"
            create(sql, "New Position")
            Call btnpositionload_Click(sender, e)
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub

    Private Sub btnpositionload_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnpositionload.Click
        Try
            sql = "SELECT ID,`DESCRIPTION` as Position FROM `tblsettings` WHERE `FORTHE`='Position'"
            reloadDtg(sql, dtglistposition)
            txtposition.Clear()
            dtglistposition.Columns(0).Visible = False
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub

    Private Sub npositionupdate_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles npositionupdate.Click
        sql = "UPDATE `tblsettings` SET `DESCRIPTION`='" & txtposition.Text & "' WHERE  `ID`=" & positionID
        updates(sql, "Position")
        Call btnpositionload_Click(sender, e)
    End Sub

    Private Sub npositiondelete_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles npositiondelete.Click
        sql = "DELETE FROM `tblsettings` WHERE `ID`=" & dtglistposition.CurrentRow.Cells(0).Value
        deletes(sql, "Position")
        Call btnpositionload_Click(sender, e)
    End Sub

    Private Sub dtglistposition_DoubleClick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles dtglistposition.DoubleClick
        Try
            positionID = dtglistposition.CurrentRow.Cells(0).Value
            txtposition.Text = dtglistposition.CurrentRow.Cells(1).Value
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub
    ''' <summary>
    ''' for the departments
    ''' </summary>
    ''' <param name="sender"></param>
    ''' <param name="e"></param>
    ''' <remarks></remarks>


    Private Sub frmsettings_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class