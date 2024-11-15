const gas_btn = document.getElementById("gas_btn")
const rpms_div = document.getElementById("rpms")
gas_btn.style.color = "red"


function createTimer() {

}

// Create timer to get duration
    // https://stackoverflow.com/questions/42636442/start-timer-on-mousedown-function-and-show-it-in-div
    // gas_btn.addEventListener('mousedown', () => {

    // })
    // gas_btn.addEventListener('mouseup', () => {})

//Create a function to calculate t-postion from duration

gas_btn.addEventListener('click', () => {

    fetch("/pedal", {body: JSON.stringify({ duration: 1.2, t_position: 0.7})})
      .then((response) => response.json())
      .then((result) => {
        rpms = result.rotations
      })
    // create a function to display rpms value in 'rpms_div'
    
    // example: displayCart(cart)
    // example: displayOrderTotal(orderTotal)
  });