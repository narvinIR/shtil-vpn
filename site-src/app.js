// Кнопка «Скачать» сама выбирает файл. Порядок тот же, что на sub.ndvsdom54.ru/get:
// строка браузера → отсутствие касаний (значит пульт) → имя видеоядра (Safari на Apple
// врёт «Intel», поэтому процессор угадываем по нему, а не по строке браузера).
(function () {
  var buttons = document.querySelectorAll('[data-download]');
  if (!buttons.length) return;

  var files = JSON.parse(buttons[0].dataset.files);
  var labels = JSON.parse(buttons[0].dataset.labels);
  var ua = navigator.userAgent.toLowerCase();
  var TV = /android tv|androidtv|google tv|googletv|smart[ -]?tv|bravia|shield|crkey|aft|hbbtv|tizen|web0s|netcast/;

  function appleSilicon() {
    try {
      var gl = document.createElement('canvas').getContext('webgl');
      var info = gl && gl.getExtension('WEBGL_debug_renderer_info');
      if (!info) return true;
      return /apple/i.test(gl.getParameter(info.UNMASKED_RENDERER_WEBGL));
    } catch (e) {
      return true;
    }
  }

  var key;
  if (ua.indexOf('android') > -1 || TV.test(ua)) {
    var isTv = TV.test(ua) || ua.indexOf('mobile') === -1 || navigator.maxTouchPoints === 0;
    key = isTv ? 'tv' : 'android';
  } else if (ua.indexOf('windows') > -1) {
    key = 'windows';
  } else if (ua.indexOf('macintosh') > -1 && ua.indexOf('mobile') === -1) {
    key = appleSilicon() ? 'mac' : 'macintel';
  } else if (/iphone|ipad|ipod/.test(ua)) {
    key = 'ios';
  } else {
    key = 'android';
  }

  Array.prototype.forEach.call(buttons, function (btn) {
    btn.href = files[key];
    btn.textContent = labels[key];
  });
})();
