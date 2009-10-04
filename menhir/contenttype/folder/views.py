import grok
from dolmen.app.layout import View
from base import IFolder
from zope.component import getMultiAdapter


class FullRenderingView(View):
    grok.context(IFolder)
    grok.title('Summary view')

    def render(self):
        self.update()
        final = []
        for item in self.items:
            view = getMultiAdapter((item, self.request), name="index")
            final.append(view.render())
        return '\n'.join(final)

    def update(self):
        self.items = self.context.values()
