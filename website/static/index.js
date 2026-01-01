function deletePassword() {
    fetch('/delete-password', {
        method: 'POST',
        body: JSON.stringify({passwordID: PasswordID})
    }).then((_res) => { // Handle the response
        window.location.href = "/";  // Refresh the page after deletion
    })
}