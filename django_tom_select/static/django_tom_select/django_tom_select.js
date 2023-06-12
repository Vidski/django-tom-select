window.addEventListener('DOMContentLoaded', (event) => {

  let getDataOptions = function (element) {
    let attribute = element.getAttribute('data-allow-empty-option')
    let allowEmptyOption = false

    if (attribute !== null) {
      allowEmptyOption = attribute === 'true'
    }

    return {
      loadThrottle: 200,
    }
  }

  let init = function (element) {
    new TomSelect(element, getDataOptions(element))
  }

  var initHeavy = function (element) {
    var defaultSettings = getDataOptions(element)
    var settings = {
      ...defaultSettings,
      openOnFocus: false,
      render: {
        item: function (data, escape) {
          return '<div class="bg-yellow-100 text-yellow-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-yellow-900 dark:text-yellow-300">' + escape(data.text) + '</div>'
        }
      },
      load: function (query, callback) {
        let url = `${element.getAttribute('data-ajax--url')}?term=${encodeURIComponent(query)}&field_id=${element.getAttribute('data-field_id')}`
        fetch(url)
          .then(response => response.json())
          .then(json => {
            callback(json.results)
          }).catch(() => {
          callback()
        })
      },
    }
    new TomSelect(element, settings)
  }

  var allElements = Array.from(document.getElementsByClassName('django-tom-select'))
  for (element of allElements) {
    if (element.classList.contains('django-tom-select-heavy')) {
      initHeavy(element)
    } else {
      init(element)
    }
  }
})
