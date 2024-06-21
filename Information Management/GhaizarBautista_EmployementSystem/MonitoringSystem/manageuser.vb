Public Class manageuser

    Private Sub chkShowpass_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles chkShowpass.CheckedChanged
        Try
            If chkShowpass.CheckState = CheckState.Checked Then
                txtpass.UseSystemPasswordChar = False
            Else
                txtpass.UseSystemPasswordChar = True
            End If
        Catch ex As Exception

        End Try
    End Sub

    Private Sub tstripList_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tstripList.Click
        Try
            Panel1.BringToFront()
            Panel1.Dock = DockStyle.Fill
            Panel2.SendToBack()
            Panel2.Dock = DockStyle.None
            sql = "SELECT user_id as Id,name as Name,username as Username, type as Type FROM  tbluser  "
            reloadDtg(sql, dtglist)

            cleartext(GroupBox1)
            loadautonumber("user", txtId)
        Catch ex As Exception
            Me.Text = ex.Message
        End Try
    End Sub

    Private Sub tstripAdd_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tstripAdd.Click
        Try
            Panel2.BringToFront()
            Panel2.Dock = DockStyle.Fill
            Panel1.SendToBack()
            Panel1.Dock = DockStyle.None


            cleartext(GroupBox1)
            loadautonumber("user", txtId)
        Catch ex As Exception
            Me.Text = ex.Message
        End Try
    End Sub

    Private Sub btnsave_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnsave.Click
        Try

            For Each ctrl As Control In GroupBox1.Controls
                If ctrl.GetType Is GetType(TextBox) Then
                    If ctrl.Text = "" Then
                        MsgBox("One of the box is empty. It needed to be filled up.", MsgBoxStyle.Exclamation)
                        Return
                    End If
                End If
                If ctrl.GetType Is GetType(ComboBox) Then
                    If ctrl.Text = "----Select-----" Then
                        MsgBox("You have to set the correct information.", MsgBoxStyle.Exclamation)
                        Return
                    End If
                End If
            Next
            
            sql = "SELECT * FROM tbluser WHERE user_id='" & txtId.Text & "'"
            reloadtxt(sql)

            If dt.Rows(0).Item("user_id") = txtId.Text Then
                sql = "UPDATE tbluser SET name='" & txtname.Text & "' ,username='" & txtusername.Text & "',pass=sha1('" & txtpass.Text & "'),type='" & cboType.Text & "'  WHERE userid ='" & txtId.Text & "'"
                updates(sql, txtname.Text)

            End If
            cleartext(GroupBox1)
            loadautonumber("user", txtId)
        Catch ex As Exception

            For Each ctrl As Control In GroupBox1.Controls
                If ctrl.GetType Is GetType(TextBox) Then
                    If ctrl.Text = "" Then
                        MsgBox("One of the box is empty. It needed to be filled up.", MsgBoxStyle.Exclamation)
                        Return
                    End If
                End If
                If ctrl.GetType Is GetType(ComboBox) Then
                    If ctrl.Text = "----Select-----" Then
                        MsgBox("You have to set the correct information.", MsgBoxStyle.Exclamation)
                        Return
                    End If
                End If
            Next
            If txtpass.Text <> txtrpass.Text Then
                MsgBox("Password does not match.", MsgBoxStyle.Exclamation)
                Return
            End If

            sql = "INSERT INTO tbluser (user_id,name,username,pass,type)" & _
               " VALUES ('" & txtId.Text & "','" & txtname.Text & "','" & txtusername.Text & "',sha1('" & txtpass.Text & "'),'" & cboType.Text & "')"
            create(sql, txtname.Text)
            updateautonumber("user")
            cleartext(GroupBox1)
            loadautonumber("user", txtId)
        End Try
    End Sub

    Private Sub txtsearch_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles txtsearch.TextChanged
        sql = "SELECT user_id as Id,name as Name, username as Username, type as Type" & _
        " FROM  tbluser  WHERE user_id Like '%" & txtsearch.Text & "%'"
        reloadDtg(sql, dtglist)
    End Sub

    Private Sub btnUpdate_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnUpdate.Click
        Try
            Panel2.BringToFront()
            Panel2.Dock = DockStyle.Fill
            Panel1.SendToBack()
            Panel1.Dock = DockStyle.None
            txtId.Text = dtglist.CurrentRow.Cells(0).Value
            sql = "SELECT * FROM tbluser WHERE user_id ='" & txtId.Text & "'"
            reloadtxt(sql)

            With dt.Rows(0)
                txtname.Text = .Item("name")
                txtusername.Text = .Item("username")
                'txtpass.Text = .Item("pass")
                'cboType.Text = .Item("type")
            End With
        Catch ex As Exception
            Me.Text = ex.Message
        End Try
    End Sub

    Private Sub btndelete_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btndelete.Click
        Try
            sql = "DELETE FROM tbluser WHERE user_id ='" & dtglist.CurrentRow.Cells(0).Value & "'"
            deletes(sql, dtglist.CurrentRow.Cells(2).Value)

            sql = "SELECT user_id as Id,name as Name,username as Username, type as Type FROM  tbluser  "
            reloadDtg(sql, dtglist)

            cleartext(GroupBox1)
            loadautonumber("user", txtId)
        Catch ex As Exception
            Me.Text = ex.Message
        End Try
    End Sub
     
    Private Sub manageuser_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        txtId.Enabled = False
        Call tstripList_Click(sender, e)
        loadautonumber("user", txtId)
    End Sub

    Private Sub ToolStrip1_ItemClicked(ByVal sender As System.Object, ByVal e As System.Windows.Forms.ToolStripItemClickedEventArgs) Handles ToolStrip1.ItemClicked

    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) 
        Me.Close()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Me.Close()
    End Sub

    Private Sub txtId_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles txtId.TextChanged

    End Sub

    Private Sub GroupBox1_Enter(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GroupBox1.Enter

    End Sub
End Class