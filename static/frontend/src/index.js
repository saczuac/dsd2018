import $ from 'jquery';
import h from 'hyperscript';

import ProductAPIClient from './products';


const showDetailOfProduct = product => {
    console.log('SHOW DETAIL of: ', product)
    window.location.href = `/buy/${product.id}`
}


const drawProducts = products => {
    const productList = $('#product-list');
    productList.empty(); // empty it first

    products.forEach(product => {
      let li = h(`div#product-item-${product.id}.product-item.col-sm-4`,[
        h('a', {
          onclick: e => {
            showDetailOfProduct(product)
          }
        }, [
          h('div.product-info.thumbnail', [
            h('div.caption', [
                h('h4.group.inner.list-group-item-heading', `${product.name}`),
                h('p.group.inner.list-group-item-text', `Price: ${product.price}`),
                h('p.group.inner.list-group-item-text', `Product Type: ${product.product_type}`)
            ])
          ])
        ])
      ]);

      productList.append(li);
    });
}

const fetchProducts = _ => {
  ProductAPIClient.getProducts().then(products => {
      console.log(products, 'PRODUCTOS DESDE API');

      products && drawProducts(products);
  })
}

// FETCH PRODUCTS IF LIST
window.location.pathname == '/' && fetchProducts();
