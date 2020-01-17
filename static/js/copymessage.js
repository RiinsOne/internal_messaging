function copyToClipboard(element) {
  var text = $(element).clone().find('br').prepend('\r\n').end().text()
  element = $('<textarea>').appendTo('body').val(text).select()
  document.execCommand('copy')
  element.remove()
}
