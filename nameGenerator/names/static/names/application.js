function copyText() {
    var text = document.getElementById("copy").innerHTML;
    navigator.clipboard.writeText(text);
    document.getElementById("copied").innerHTML = "Copied !"
}

function removeCopied() {
    document.getElementById("copied").innerHTML = ""
}