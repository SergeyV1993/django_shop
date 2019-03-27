$(document).ready(function(){
    $('.cart').on('click', function(e){
        e.preventDefault();
        product_id = $(this).attr('data-id');
        alert(product_id);
       // data = {
        //    product_id: product_id
        //};
        //$.ajax({
         //   type: "GET",
         //   url: '{% url "add_to_cart" %}',
         //   data: data,
          //  success: function(data){
           //    $("#cart_count").html(data.cart_total)
            //}
        //})
    })
});