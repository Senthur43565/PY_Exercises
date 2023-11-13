
// Create an empty shopping cart object
const shoppingCart = {};

// Add a click event listener to all "Add to Cart" buttons
const addToCartButtons = document.querySelectorAll('.product .btn');
addToCartButtons.forEach(button => {
  button.addEventListener('click', addToCart);
});

// Function to add a product to the shopping cart
function addToCart(event) {
  const product = event.target.closest('.product'); // Get the product container
  const productName = product.querySelector('h3').textContent; // Get the product name
  const productPrice = product.querySelector('p').textContent; // Get the product price

  // Check if the product is already in the cart; if not, initialize the quantity to 1
  if (!shoppingCart[productName]) {
    shoppingCart[productName] = {
      price: productPrice,
      quantity: 1,
    };
  } else {
    // If the product is already in the cart, increase the quantity
    shoppingCart[productName].quantity++;
  }

  // You can also update the UI to show the user that the product has been added to the cart
  // For example, you can update a counter that shows the number of items in the cart

  // Display a message or perform any other action to indicate that the product has been added to the cart
  alert(`Added ${productName} to the cart.`);
}

// Function to update the cart display
function updateCartDisplay() {
  // Implement this function to display the cart content in the UI
  // You can create a separate cart display element and update its content with the cart data
}
