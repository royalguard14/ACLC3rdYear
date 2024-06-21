function addUser() {
    let name = document.getElementById('name').value;
    let birthdate = document.getElementById('birthdate').value;
    let birthplace = document.getElementById('birthplace').value;
    let education = document.getElementById('education').value;

    let nameParts = name.split(", ");
    let lastName = nameParts[0].toLowerCase();
    let firstAndMiddle = nameParts[1].split(" ");
    let firstName = firstAndMiddle.slice(0, -1).join(" ").toLowerCase();
    let middleInitial = firstAndMiddle[firstAndMiddle.length - 1];

    var userData = {
        fName: lastName,
        gName: firstName,
        mName: middleInitial,
        bdate: birthdate,
        bplace: birthplace,
        education: education
    }

    var storedData = JSON.parse(sessionStorage.getItem('userData')) || [];
    storedData.push(userData);
    sessionStorage.setItem('userData', JSON.stringify(storedData));
    document.getElementById('name').value = '';
    document.getElementById('birthdate').value = '';
    document.getElementById('birthplace').value = '';
    document.getElementById('education').value = '';
    updateTable();
}

function updateTable() {
    var tableBody = document.getElementById('userinfoBody');
    tableBody.innerHTML = '';
    var storedData = JSON.parse(sessionStorage.getItem('userData')) || [];
    storedData.forEach(function(user) {
        var row = tableBody.insertRow();
        var fnameCell = row.insertCell(0);
        var gnameCell = row.insertCell(1);
        var mnameCell = row.insertCell(2);
        var printCell = row.insertCell(3);
        var deleteCell = row.insertCell(4);

        fnameCell.textContent = user.fName;
        gnameCell.textContent = user.gName;
        mnameCell.textContent = user.mName;
        
        
        var printButton = document.createElement('button');
        printButton.textContent = 'Print';
        printButton.onclick = function() {

            var storedData = JSON.parse(sessionStorage.getItem('userData')) || [];
            var userDetails = storedData[storedData.length - 1]; 


            var url = 'index2.html?';
            for (var key in userDetails) {
                if (userDetails.hasOwnProperty(key)) {
                    url += encodeURIComponent(key) + '=' + encodeURIComponent(userDetails[key]) + '&';
                }
            }
            url = url.slice(0, -1); 


            window.location.href = url;
        };

        printCell.appendChild(printButton);

        var deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = function() {


        };
        deleteCell.appendChild(deleteButton);
    });
}

updateTable();

function clearData() {
    sessionStorage.removeItem('userData');
    updateTable();
}
