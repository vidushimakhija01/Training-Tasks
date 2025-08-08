let display = document.getElementById("display");
function appendValue(value){
    display.value += value
}
function clearDisplay(){
    display.value = '';
}
function deleteLast(){
    display.value = display.value.slice(0,-1);
}
function calculate() {
    try {
        const result = math.evaluate(display.value);
        if (!isFinite(result) || isNaN(result)) {
            display.value = 'Error : Division by 0';
        } else {
            display.value = result;
        }
    } catch (error) {
        display.value = 'Error';
    }
}
