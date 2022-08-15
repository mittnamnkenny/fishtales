// Remove flash message alert after 2.5 seconds
document.addEventListener('DOMContentLoaded', removeAlerts);

function removeAlerts() {
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
}

module.exports = removeAlerts;
