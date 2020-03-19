const api_url = 'http://127.0.0.1:8000/api/shop_view/'

new Vue({
    el: '#shop_vue',
    data: {
        products: []
    },
    created: function () {
        const vm = this;
        axios.get(api_url)
        .then(function (response) {
        vm.products = response.data
        })
    }
}
)