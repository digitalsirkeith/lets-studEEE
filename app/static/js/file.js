document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#photo").onchange = function () {
        document.querySelector("#file-name").textContent = this.files[0].name;
    }
});