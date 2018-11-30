import 'whatwg-fetch';
import Config from './config';


const ProductAPIClient = {
    products: null,
    productDetail: null,

    getCookie: name => {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    getProducts: _ => {
        const url = `/api/products/list`;

        return fetch(url, {
                    credentials: 'same-origin',
                    headers: {
                      'Content-Type': 'application/json',
                      'x-csrftoken': ProductAPIClient.getCookie('csrftoken')
                    },
                })
                .then(response => {
                    if (response.status === 200) return response.json();
                })
                .then(products => {
                    ProductAPIClient.products = products;
                    return products;
                })
                .catch(e => false);
    },

    getProductDetail: id => {
        const url = `/api/products/list/${id}`;

        return fetch(url, {
                    credentials: 'same-origin',
                    headers: {
                      'Content-Type': 'application/json',
                      'x-csrftoken': ProductAPIClient.getCookie('csrftoken')
                    },
                })
                .then(response => {
                    if (response.status === 200) return response.json();
                })
                .then(product => {
                    ProductAPIClient.productDetail = product;
                    return product;
                })
                .catch(e => false);
    }

};

export default ProductAPIClient;