$(document).ready(function () {
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;

        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
           
        }
    });
});
 
$(document).ready(function () {
    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value) ? 0 : value;

        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addtocartbtn').click(function (e) { 
        e.preventDefault();
    
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "/add-to-cart/",  
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken': token
            },
            success: function (response) {
                console.log('Success Response:', response);
                if (response.status === 'Product added successfully') {
                    alertify.success(response.status);  // Show success message
                    updateCartCount(); // Update cart count
                } else {
                    alertify.error('Unexpected response from the server.');
                }
            },
            error: function (xhr, status, error) {
                console.log(error);
                alertify.error('An error occurred while adding to cart.');
            }
        });
    });
    
    // Function to update the cart count dynamically
    $(document).ready(function () {
        // Function to update cart count in the navbar
        function updateCartCount() {
            $.ajax({
                method: "GET",
                url: "/cart-count/",  // URL of your 'cart_count' view
                success: function (response) {
                    $('#cart-count').text(response.count);  // Update cart count in the navbar
                }
            });
        }
    
        // Call this function on page load to set the cart count initially
        updateCartCount();
    });
    
    
    $('.addtowishlist').click(function (e) { 
        e.preventDefault();
    
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

       $.ajax({
            method: "POST",
            url: "/add-to-wishlist/",  
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': token
            },
            
            success: function (response) {
                console.log('Success Response:', response);
                if (response.status) {
                    alertify.success(response.status);  // Show success message with Bootstrap's alert system
                } 
                else {
                    alertify.error('Unexpected response from the server.');
                }
            },
            // error: function (xhr, status, error) {
            //     console.log(error);
            //     alertify.error('An error occurred while adding to cart.');
            // }
        });
    });
    
    $('.changequantity').click(function (e)  { 
        e.preventDefault();
    
        // Fetch product details
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        // Perform AJAX request to update quantity
        $.ajax({
            method: "POST",
            url: "/update-cart/",  
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken': token
            },
            success: function (response) {
                console.log('Success Response:', response);
                
                if (response.status === 'Updated Successfully') {
                    alertify.success(response.status);  // Show success message
                } else {
                    alertify.error(response.message || 'Unexpected response from the server.');
                }
    
                
            },
            error: function (xhr, status, error) {
                console.log('AJAX Error:', error);
                alertify.error('An error occurred while updating the quantity. Please try again.');
            }
        });
    });
    
    $(document).on('click', '.delete-cart-item', function (e) { 
        e.preventDefault();
    
        // Fetch product details and CSRF token
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        // Perform AJAX request to delete item
        $.ajax({
            method: "POST",
            url: "/delete-cart-item/",
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': token
            },
            success: function (response) {
                console.log('Success Response:', response);
                
                if (response.status === 'Item Deleted Successfully') {
                    alertify.success(response.status);  // Show success message
                } else {
                    alertify.error(response.message || 'Unexpected response from the server.');  // Show error message
                }
    
                // Reload only the cart data without refreshing the entire page
                $('.cartdata').load(location.href + " .cartdata");
            },
            error: function (xhr, status, error) {
                console.log('AJAX Error:', error);
                alertify.error('An error occurred while deleting the item. Please try again.');
            }
        });
        
});
    
    
    
        
    


    $(document).on('click', '.delete-wishlist-item', function (e) { 
        e.preventDefault();
    
        // Fetch product details and CSRF token
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        // Perform AJAX request to delete item
        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item/",
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': token
            },
            success: function (response) {
                console.log('Success Response:', response);
                alertify.success(response.status);  // Show success message
               // Reload only the cart data without refreshing the entire page
                $('.wishdata').load(location.href + " .wishdata");
            },
        });
        
    });
    
    
    

});  
