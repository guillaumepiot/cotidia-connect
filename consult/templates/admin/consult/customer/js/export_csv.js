function (data, queryString) {
  window.open("{% url 'consult-admin:customer-export-csv' %}" + queryString)
}
