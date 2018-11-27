import $ from 'jquery';
import h from 'hyperscript';

import ProductAPIClient from './products';


const showDetailOfProduct = product => {
    console.log('SHOW DETAIL of: ', product)
}


const drawProducts = products => {
    const productList = $('#product-list');
    productList.empty(); // empty it first

    products.forEach(product => {
      let li = h(`li#product-item-${product.id}.product-item`,[
        h('a', {
          onclick: e => {
            showDetailOfProduct(product)
          }
        }, [
          h('div.product-info', [
            h('div.product-name', `${product.name}`),
            h('div.product-cost-price', `${product.cost_price}`),
            h('div.product-sale-price', `${product.sale_price}`),
            h('div.product-type', `${product.product_type}`)
          ])
        ])
      ]);

      productList.append(li);
    });
}

ProductAPIClient.getProducts().then(products => {
    console.log(products, 'PRODUCTOS DESDE API');

    products && drawProducts(products);
})
