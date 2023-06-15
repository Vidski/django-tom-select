DjangoTomSelect = {
  registerAll: () => {
    let allElements = Array.from(document.getElementsByClassName('django-tom-select'))
    for (element of allElements) {
      if (element.classList.contains('django-tom-select-heavy')) {
        DjangoTomSelect.initHeavy(element)
      } else {
        DjangoTomSelect.init(element)
      }
    }
  },
  init: (element) => {
    new TomSelect(element, this.getDataOptions(element))
  },
  initHeavy: (element) => {
    let defaultSettings = this.getDataOptions(element)
    let settings = {
      ...defaultSettings,
      openOnFocus: false,
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
  },
  getDataOptions: (element) => {
    let plugins = []
    if (element.multiple)
      plugins[0] = 'remove'

    return {
      plugins: plugins,
      loadThrottle: 200,
      // onItemAdd reset input
      onItemAdd: function () {
        this.setTextboxValue('')
      },
    }
  }
}

window.addEventListener('DOMContentLoaded', (event) => {
  DjangoTomSelect.registerAll()
  // HTMX Support
  if (typeof htmx === 'object') {
    htmx.onLoad((elt) => {
      DjangoTomSelect.registerAll()
    })
  }
})
