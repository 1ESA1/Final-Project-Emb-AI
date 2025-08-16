/**
 * Runs sentiment analysis on the text input provided by the user.
 * Retrieves the value from the input element with id "textToAnalyze",
 * sends it to the server via an XMLHttpRequest, and displays the response
 * in the element with id "system_response".
 */
let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
