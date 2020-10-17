var stripe = Stripe('pk_test_51HcoaDIIdYahhqUdvMw04DLbfOoWv6UJj1omy0JzXc9FvrRHrU3c67yUFXil6a2RAzYJojQyDt2GGLKkzK21wWUa0025puWbnc');
var elements = stripe.elements();
var style = {
    base: {
        color: "#32325d",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
          color: "#32325d"
        }
      },
      invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#fa755a",
        iconColor: "#fa755a"
      }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");
card.on("change", function (event) {
      // Disable the Pay button if there are no card details in the Element
      document.querySelector("button").disabled = event.empty;
      document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
    });

var form = document.getElementById('payment-form');
var order_id = document.getElementById("myVar").value;

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    fetch('/api/items/' + order_id + '/buy', {
        method: 'GET',
    }).then(function (response) {
        return response.json();
    }).then(function (session) {
        return payWithCard(stripe, card, session)
    })
});

var payWithCard = function (stripe, card, session) {
    loading(true);
    stripe.confirmCardPayment(session.client_secret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: 'Jenny Rosen'
                }
            }
        }).then(function(result) {
        if (result.error) {
            console.log(result.error.message);
            showError(result.error.message)
          } else {
            if (result.paymentIntent.status === 'succeeded') {
                orderComplete(result.paymentIntent.id)
            }
          }
        });
}

var orderComplete = function(paymentIntentId) {
  loading(false);
  document
    .querySelector(".result-message a")
    .setAttribute(
      "href",
      "https://dashboard.stripe.com/test/payments/" + paymentIntentId
    );
  document.querySelector(".result-message").classList.remove("hidden");
  document.querySelector("button").disabled = true;
};

// Show the customer the error from Stripe if their card fails to charge

var showError = function(errorMsgText) {
  loading(false);
  var errorMsg = document.querySelector("#card-error");
  errorMsg.textContent = errorMsgText;
  setTimeout(function() {
    errorMsg.textContent = "";
  }, 4000);
};

// Show a spinner on payment submission
var loading = function(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("button").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("button").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
};

