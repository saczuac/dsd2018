import 'whatwg-fetch';
import Config from './config';


const ProductAPIClient = {
    products: null,
    productDetail: null,

    getProducts: _ => {
        const url = `/api/products/list`;

        return fetch(url, {
                    credentials: 'same-origin',
                    headers: {
                      'Content-Type': 'application/json',
                      // 'x-csrftoken': cookies.get('csrftoken')
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
                      // 'x-csrftoken': cookies.get('csrftoken')
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