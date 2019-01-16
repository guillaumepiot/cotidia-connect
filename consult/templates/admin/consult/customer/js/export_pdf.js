function (data, queryString) {
  window.open("{% url 'consult-admin:customer-export-pdf' %}" + queryString)
}
