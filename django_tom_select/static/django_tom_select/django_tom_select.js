DjangoTomSelect = {
  registerAll: () => {
    const elements = Array.from(document.querySelectorAll('.django-tom-select'))
    elements.forEach((element) =>
      element.classList.contains('django-tom-select-heavy')
        ? DjangoTomSelect.initHeavy(element)
        : DjangoTomSelect.init(element)
    )
  },
  unregisterAll: () => {
    const elements = Array.from(document.querySelectorAll('.django-tom-select'))
    elements.forEach((element) =>
      element.tomselect = null
    )
  },
  init: (element) => {
    new TomSelect(element, DjangoTomSelect.getDataOptions(element))
  },
  initHeavy: (element) => {
    let defaultSettings = DjangoTomSelect.getDataOptions(element)
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
      plugins[0] = 'remove_button'

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
    htmx.on('htmx:beforeSwap', (elt) => {
      DjangoTomSelect.unregisterAll()
    })
    htmx.on('htmx:afterSwap', (elt) => {
      DjangoTomSelect.registerAll()
    })
  }
})
