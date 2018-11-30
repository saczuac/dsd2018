import 'whatwg-fetch';


const BonitaAPIClient = {
    caseId: null,

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

    confirmTask: (confirm="true") => {
        const url = `/api/bonita/confirm`;

        const data = {
            confirm,
            case_id: BonitaAPIClient.caseId
        }

        return fetch(url, {
                    method: "POST",
                    credentials: 'same-origin',
                    body: JSON.stringify(data),
                    headers: {
                      'Content-Type': 'application/json',
                      'x-csrftoken': BonitaAPIClient.getCookie('csrftoken')
                    },
                })
                .then(response => {
                    if (response.status === 200) return response.json();
                })
                .catch(e => false);
    },

    startProcess: (productId, couponNumber) => {
        const url = `/api/bonita/start`;

        const data = {
            "product_id": productId,
            "coupon_number": couponNumber
        }

        return fetch(url, {
                    method: "POST",
                    credentials: 'same-origin',
                    body: JSON.stringify(data),
                    headers: {
                      'Content-Type': 'application/json',
                      'x-csrftoken': BonitaAPIClient.getCookie('csrftoken')
                    },
                })
                .then(response => {
                    if (response.status === 200) return response.json();
                })
                .then(data => {
                    // Set case_id
                    BonitaAPIClient.caseId = data.case_id;
                    return data;
                })
                .catch(e => false);
    },

    getVariable: (variableName="precio_final") => {
        const url = `/api/bonita/variable?v_name=${variableName}&case_id=${BonitaAPIClient.caseId}`;

        return fetch(url, {
                    credentials: 'same-origin',
                    headers: {
                      'Content-Type': 'application/json',
                      'x-csrftoken': BonitaAPIClient.getCookie('csrftoken')
                    },
                })
                .then(response => {
                    if (response.status === 200) return response.json();
                })
                .then(data => {
                    return data[variableName];
                })
                .catch(e => false);
    },

};

export default BonitaAPIClient;