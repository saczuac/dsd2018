import $ from 'jquery';
import h from 'hyperscript';

import ProductAPIClient from './products';
import BonitaAPIClient from './bonita';


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

const showDone = (ok=true) => {
  const detailHtml = $('#product-detail');
  detailHtml.empty();

  let okForm = h(`div#product-form`,[
    h('div', [
      h('h4.group', `COMPRA ${ok ? 'REALIZADA' : 'CANCELADA'}`),
    ]),
  ]);

  detailHtml.append(okForm);
}

const doBuy = _ => {
  console.log('DO BUY');

  BonitaAPIClient.confirmTask().then(ok => ok && showDone());
}

const cancelBuy = _ => {
  console.log('CANCEL BUY');

  BonitaAPIClient.confirmTask("false").then(ok => ok && showDone(false));
}

const startProcess = _ => {
  const coupon = $('#coupon').val();

  const productForm = $('#product-form');
  productForm.empty();

  const price = 'calculando...';

  const detailHtml = $('#product-detail');

  let buyForm = h(`div#product-form`,[
    h('div', [
      h('h4.group#final', `PRECIO FINAL: ${price}`),
      h('input.btn.btn-default#buyBtn', {
        'type': 'submit',
        'value': 'CONFIRMAR COMPRA',
        onclick: e => {
          doBuy()
        },
      }),
    ]),
    h('div', [
      h('input.btn.btn-default#cancelBtn', {
        'type': 'submit',
        'value': 'CANCELAR COMPRA',
        onclick: e => {
          cancelBuy()
        },
      }),
    ]),
  ]);

  detailHtml.append(buyForm);

  const productId = window.location.href.split('/').slice(-1)[0];

  console.log(`start process, coupon: ${coupon} product_id: ${productId}`);

  BonitaAPIClient.startProcess(productId ,coupon).then(ok => {
    if (ok) {
      setTimeout(_=> {
        BonitaAPIClient.getVariable("precio_final").then(finalPrice => {
          $("#final").html(`PRECIO FINAL: ${finalPrice}`);
        })
      }, 1000)
    } 
  })


}

const showBuyForm = _ => {
  const detailHtml = $('#product-detail');

  let buyForm = h(`div#product-form`,[
    h('div', [
      h('span.span-cupon', 'Ingrese cupón en caso de tener'),
      h('input.form-control#coupon', {
        'type': 'text'
      }),
      h('input.btn.btn-default#calculate', {
        'type': 'submit',
        'value': 'CONTINUAR COMPRA',
        onclick: e => {
          startProcess()
        },
      }),
    ])
  ]);

  detailHtml.append(buyForm);
}

// FETCH PRODUCTS IF LIST
if (window.location.pathname == '/') {
  fetchProducts();
} else {
  showBuyForm();
}
