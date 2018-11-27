import 'whatwg-fetch';
import Config from './config';


const ProductAPIClient = {
    products: null,

    getProducts: _ => {
        const url = `${Config.server.url}/api/products/products/`;

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

};

export default ProductAPIClient;