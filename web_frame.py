import webview
import urllib.request


def show_web_view(data = None):
    def expose(w: webview.Window):
        w.evaluate_js('document.body.hidden = document.documentElement.style.backgroundColor="black";')
        req = urllib.request.urlopen('https://c.gethopscotch.com/api/v1/projects/test')
        project = req.read().decode('UTF-8')
        w.evaluate_js(f'localStorage.projectFromStorage = JSON.stringify({data or project})')
        w.evaluate_js('setTimeout(() => location.reload(), 5)')
        w.evaluate_js('document.body.onclick = () => location.reload()')
        w.set_title('Untitled Project')

    window = webview.create_window('Loading Project...', 'https://ae-hopscotch.github.io/hs-tools/play-project/?play=1&hide=%23fullscreen-button&bgColor=black')
    webview.start(expose, window)
