alert("I Love Flutter");
var button = document.getElementById("btn");
//getElementByI
//每秒执行一次，若按钮状态为可用，进行点击
setInterval(function() {
    if (button.disabled == false) {
        button.click();

    }
},
1000);